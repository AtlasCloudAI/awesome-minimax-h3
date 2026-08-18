#!/usr/bin/env python3
"""Find H3 projects that are not on the list yet and are worth a look.

This never edits the list. Curation needs a human: the bar is partly
"does it do something nothing else here does", which no query can answer.
Output is a review queue, written to discovery-report.md.

Everything already listed, everything on the denylist, anything under the
entry bar and anything matching the block-terms is filtered out first, so
the queue stays short enough to actually read.
"""
from __future__ import annotations

import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3lib as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fetch = H.Fetcher()

GH_QUERIES = [
    "minimax-h3 in:name",
    "minimaxh3 in:name",
    '"minimax h3" in:description',
    '"MiniMax-H3" in:readme',
    "h3 comfyui minimax in:name,description",
]


def known_keys() -> tuple[set[str], set[str]]:
    data = H.load(os.path.join(ROOT, "data/ecosystem.json"))
    keys = {H.item_key(i) for _, _, i in H.iter_items(data)}
    deny = H.load(os.path.join(ROOT, "data/denylist.json"))
    denied, owners = H.split_denylist(deny)
    return keys | denied, owners


def looks_like_h3(*texts: str) -> bool:
    """Guard against 'h3' matching unrelated things (h3 geospatial, HTTP/3…)."""
    blob = " ".join(t for t in texts if t).lower()
    if "minimax" in blob and "h3" in blob:
        return True
    return "minimax-h3" in blob or "minimaxh3" in blob or "hailuo" in blob


def discover_github(known: set[str], owners: set[str]) -> list[dict]:
    seen: dict[str, dict] = {}
    for q in GH_QUERIES:
        params = urllib.parse.urlencode(
            {"q": q, "sort": "stars", "order": "desc", "per_page": 100})
        st, d = fetch.github(f"search/repositories?{params}")
        if st != 200 or not d:
            print(f"  ! github search failed ({st}) for: {q}", file=sys.stderr)
            continue
        for r in d.get("items", []):
            seen[r["full_name"]] = r

    out = []
    for full, r in seen.items():
        key = "gh:" + full.lower()
        desc = r.get("description") or ""
        if key in known or H.owner_of("gh", full) in owners:
            continue
        if not looks_like_h3(full, desc, " ".join(r.get("topics", []))):
            continue
        if (term := H.blocked(full, desc)):
            continue
        if r["stargazers_count"] < H.THRESHOLDS["github"]:
            continue
        if r.get("archived"):
            continue
        out.append({
            "kind": "gh", "name": full, "url": r["html_url"],
            "metric": f"{r['stargazers_count']}★", "sort": r["stargazers_count"],
            "desc": desc[:160], "updated": (r.get("pushed_at") or "")[:10],
            "fork": bool(r.get("fork")),
        })
    return out


def discover_hf(known: set[str], owners: set[str]) -> list[dict]:
    out = []
    for api, kind, floor_field in (("models", "hf", "likes"), ("spaces", "hfs", "likes")):
        for query in ("MiniMax-H3", "minimax h3"):
            params = urllib.parse.urlencode(
                {"search": query, "limit": 100, "sort": "likes", "direction": -1})
            st, d = fetch.hf(f"{api}?{params}")
            if st != 200 or not d:
                print(f"  ! hf {api} search failed ({st})", file=sys.stderr)
                continue
            for m in d:
                ident = m["id"]
                key = f"{kind}:{ident.lower()}"
                if key in known or H.owner_of(kind, ident) in owners:
                    continue
                tags = " ".join(m.get("tags", []))
                if not looks_like_h3(ident, tags):
                    continue
                if H.blocked(ident, tags):
                    continue
                likes = m.get(floor_field) or 0
                if likes < H.THRESHOLDS["hf"]:
                    continue
                base = "https://huggingface.co/" + ("" if kind == "hf" else "spaces/")
                metric = f"{likes}♥"
                if kind == "hf" and (m.get("downloads") or 0) > 0:
                    metric += f" · {m['downloads']}↓"
                out.append({
                    "kind": kind, "name": ident, "url": base + ident,
                    "metric": metric, "sort": likes,
                    "desc": (m.get("pipeline_tag") or "") + " " + tags[:120],
                    "updated": (m.get("lastModified") or "")[:10], "fork": False,
                })
                known.add(key)
    return out


def discover_civitai(known: set[str], owners: set[str]) -> list[dict]:
    out = []
    for params in ({"query": "minimax h3", "limit": 100, "sort": "Most Downloaded", "nsfw": "false"},
                   {"tag": "minimax h3", "limit": 100, "sort": "Most Downloaded", "nsfw": "false"}):
        st, d = fetch.civitai("models?" + urllib.parse.urlencode(params))
        if st != 200 or not d:
            print(f"  ! civitai search failed ({st})", file=sys.stderr)
            continue
        for m in d.get("items", []):
            mid = str(m.get("id"))
            key = "civitai:" + mid
            creator = ((m.get("creator") or {}).get("username") or "").lower()
            if key in known or (creator and creator in owners):
                continue
            name = m.get("name") or ""
            # Civitai hosts many multi-model collections that merely mention
            # MiniMax; require H3 in the title itself.
            if "h3" not in name.lower():
                continue
            if m.get("nsfw") or m.get("poi") or (m.get("nsfwLevel") or 0) > 1:
                continue
            if H.blocked(name, " ".join(m.get("tags", []))):
                continue
            dl = (m.get("stats") or {}).get("downloadCount") or 0
            if dl < H.THRESHOLDS["civitai"]:
                continue
            out.append({
                "kind": "civitai", "name": name[:80],
                "url": f"https://civitai.com/models/{mid}",
                "metric": f"{dl}↓", "sort": dl,
                "desc": m.get("type") or "", "updated": "", "fork": False,
            })
            known.add(key)
    return out


def main() -> int:
    known, owners = known_keys()
    print(f"{len(known)} keys already listed or denied; "
          f"{len(owners)} blocked publishers", flush=True)

    found = []
    for name, fn in (("GitHub", discover_github), ("Hugging Face", discover_hf),
                     ("Civitai", discover_civitai)):
        rows = fn(known, owners)
        print(f"  {name}: {len(rows)} candidates")
        found += rows

    found.sort(key=lambda r: -r["sort"])

    if not found:
        report = ("No new candidates above the entry bar this run. "
                  f"({H.today()})")
        open(os.path.join(ROOT, "discovery-report.md"), "w", encoding="utf-8").write(report + "\n")
        open(os.path.join(ROOT, "discovery-count.txt"), "w").write("0\n")
        print(report)
        return 0

    def cell(text: str) -> str:
        """Table-safe: names and descriptions here routinely contain pipes."""
        return (text or "").replace("|", "\\|").replace("\n", " ").strip()

    lines = [
        f"Automated sweep on {H.today()} found **{len(found)}** project(s) that are "
        "not on the list, not on the denylist, and clear the entry bar.",
        "",
        "Nothing here is added automatically — each still needs a human call on "
        "whether it does something no listed project already does, plus a category "
        "and an EN/ZH note.",
        "",
    ]
    for source, kind_set, cap in (("GitHub", {"gh"}, 25),
                                  ("Hugging Face", {"hf", "hfs"}, 15),
                                  ("Civitai", {"civitai"}, 10)):
        rows = [r for r in found if r["kind"] in kind_set]
        if not rows:
            continue
        lines += ["", f"### {source} ({len(rows)})", "",
                  "| Project | Popularity | Updated | What it says it does |",
                  "|---|---|---|---|"]
        for r in rows[:cap]:
            mark = " *(fork)*" if r["fork"] else ""
            lines.append(f"| [{cell(r['name'])}]({r['url']}){mark} | {r['metric']} | "
                         f"{r['updated'] or '—'} | {cell(r['desc']) or '—'} |")
        if len(rows) > cap:
            lines.append(f"\n…and {len(rows) - cap} more from {source}, "
                         "below these in popularity.")

    lines += [
        "",
        "---",
        "",
        "**To accept one:** add it to `data/ecosystem.json` with an `en` and `zh` note, "
        "then run `npm run generate`.",
        "",
        "**To reject one for good:** add its key to `data/denylist.json` with a reason "
        "and it will stop showing up here. Keys look like `gh:owner/repo`, "
        "`hf:owner/model`, `hfs:owner/space`, `civitai:12345`.",
    ]

    report = "\n".join(lines)
    open(os.path.join(ROOT, "discovery-report.md"), "w", encoding="utf-8").write(report + "\n")
    open(os.path.join(ROOT, "discovery-count.txt"), "w").write(f"{len(found)}\n")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
