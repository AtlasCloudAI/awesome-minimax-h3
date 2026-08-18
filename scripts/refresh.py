#!/usr/bin/env python3
"""Re-check every entry against the live APIs and update data/ecosystem.json.

Conservative by design:
  * A repo that 404s is hidden from the README immediately but only deleted
    after GRACE_DAYS, so an outage or a brief rename never loses an entry.
  * A link that returns 403 is NOT treated as dead — plenty of sites block
    automated requests. Only 404/410 counts.
  * Popularity dropping below the entry bar is reported, never auto-removed:
    star counts fluctuate and removal is a judgement call.
  * A Civitai entry that flips to NSFW is removed at once — that is policy,
    not a judgement call.
"""
from __future__ import annotations

import concurrent.futures as futures
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3lib as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data/ecosystem.json")

fetch = H.Fetcher()


def probe(item: dict) -> dict:
    """Returns {'state': 'ok'|'gone'|'unknown', ...fields to merge}."""
    kind = item["kind"]

    if kind == "gh":
        repo = item["url"].split("github.com/", 1)[-1].strip("/")
        st, d = fetch.github(f"repos/{repo}")
        if st in (404, 451):
            return {"state": "gone", "why": f"GitHub returned {st}"}
        if st != 200 or not d:
            return {"state": "unknown", "why": f"GitHub returned {st}"}
        out = {"state": "ok",
               "metrics": {"stars": d["stargazers_count"]},
               "updated": (d.get("pushed_at") or "")[:10]}
        # The API follows renames; adopt the new identity so links never rot.
        if d["full_name"].lower() != repo.lower():
            out["renamed_to"] = d["full_name"]
        out["archived"] = bool(d.get("archived"))
        return out

    if kind in ("hf", "hfs"):
        api = "models" if kind == "hf" else "spaces"
        ident = item["url"].split("huggingface.co/", 1)[-1]
        if kind == "hfs":
            ident = ident.split("spaces/", 1)[-1]
        ident = ident.strip("/")
        st, d = fetch.hf(f"{api}/{ident}")
        if st in (401, 404):
            return {"state": "gone", "why": f"Hugging Face returned {st}"}
        if st != 200 or not d:
            return {"state": "unknown", "why": f"Hugging Face returned {st}"}
        metrics = {"likes": d.get("likes")}
        if kind == "hf" and (d.get("downloads") or 0) > 0:
            metrics["downloads"] = d["downloads"]
        return {"state": "ok", "metrics": metrics,
                "updated": (d.get("lastModified") or "")[:10]}

    if kind == "civitai":
        mid = item["url"].rstrip("/").rsplit("/", 1)[-1]
        st, d = fetch.civitai(f"models/{mid}")
        if st == 404:
            return {"state": "gone", "why": "Civitai returned 404"}
        if st != 200 or not d:
            return {"state": "unknown", "why": f"Civitai returned {st}"}
        if d.get("nsfw") or d.get("poi"):
            return {"state": "policy", "why": "flipped to NSFW/POI on Civitai"}
        return {"state": "ok",
                "metrics": {"downloads": (d.get("stats") or {}).get("downloadCount")},
                "realname": d.get("name")}

    # Plain links: only an explicit 404/410 is disqualifying. Many good sites
    # answer 403 to anything that is not a browser.
    st, _ = fetch.get(item["url"], tries=3)
    if st in (404, 410):
        return {"state": "gone", "why": f"HTTP {st}"}
    if st == -1 or st >= 500:
        return {"state": "unknown", "why": f"HTTP {st}"}
    return {"state": "ok"}


def main() -> int:
    data = H.load(DATA)
    items = [(s, g, i) for s, g, i in H.iter_items(data)]
    print(f"checking {len(items)} entries…", flush=True)

    with futures.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(lambda t: probe(t[2]), items))

    changed, renamed, hidden, restored, removed, unknown, below = [], [], [], [], [], [], []
    collapsed = []
    now = H.today()

    for (section, group, item), res in zip(items, results):
        name = H.display_name(item)
        state = res["state"]

        if state == "unknown":
            unknown.append((name, res.get("why", "")))
            continue

        if state == "policy":
            item["_delete"] = True
            removed.append((name, res["why"]))
            continue

        if state == "gone":
            if "unavailableSince" not in item:
                item["unavailableSince"] = now
                hidden.append((name, res.get("why", "")))
            elif H.days_since(item["unavailableSince"]) >= H.GRACE_DAYS:
                item["_delete"] = True
                removed.append((name, f"unreachable for {H.GRACE_DAYS}+ days"))
            continue

        # state == ok
        if item.pop("unavailableSince", None):
            restored.append(name)

        if res.get("renamed_to"):
            old = item["url"]
            item["url"] = "https://github.com/" + res["renamed_to"]
            if isinstance(item.get("name"), str):
                item["name"] = res["renamed_to"]
            renamed.append((old.split("github.com/")[-1], res["renamed_to"]))

        if "archived" in res:
            if res["archived"]:
                item["archived"] = True
            else:
                item.pop("archived", None)

        if res.get("realname"):
            item["realname"] = res["realname"]

        if "metrics" in res:
            new = {k: v for k, v in res["metrics"].items() if v is not None}
            old = item.get("metrics") or {}
            if new and new != old:
                delta = []
                for k, v in new.items():
                    prev = old.get(k)
                    if prev != v:
                        delta.append(f"{k} {prev if prev is not None else '—'}→{v}")
                    if (isinstance(prev, int) and isinstance(v, int)
                            and prev - v > 20 and v < prev * 0.6):
                        collapsed.append((name, f"{k} {prev}→{v}"))
                changed.append((name, ", ".join(delta)))
                item["metrics"] = new

        if "updated" in res and res["updated"]:
            item["updated"] = res["updated"]

        # Report-only: has this slipped under the bar we advertise? Skipped for
        # the Related lists section, which is navigation rather than curation.
        if not item.get("official") and section["id"] != "related":
            m = item.get("metrics") or {}
            bar = None
            if item["kind"] == "gh" and m.get("stars") is not None:
                bar = ("stars", m["stars"], H.THRESHOLDS["github"])
            elif item["kind"] in ("hf", "hfs") and m.get("likes") is not None:
                bar = ("likes", m["likes"], H.THRESHOLDS["hf"])
            elif item["kind"] == "civitai" and m.get("downloads") is not None:
                bar = ("downloads", m["downloads"], H.THRESHOLDS["civitai"])
            if bar and bar[1] < bar[2]:
                below.append((name, f"{bar[0]} {bar[1]} < {bar[2]}"))

    # A snapshot date is a promise that the whole list was checked. If too much
    # of the run failed, write nothing and fail loudly rather than publish a
    # date that half the entries did not earn.
    fail_ratio = len(unknown) / max(len(items), 1)
    if fail_ratio > 0.10:
        print(f"\nABORT: {len(unknown)}/{len(items)} entries "
              f"({fail_ratio:.0%}) could not be checked — data left untouched.",
              file=sys.stderr)
        for name, why in unknown[:15]:
            print(f"  - {name}: {why}", file=sys.stderr)
        return 1

    # Apply deletions, and record them so discovery never re-suggests them.
    deny = H.load(os.path.join(ROOT, "data/denylist.json"))
    denied = {e["key"] for e in deny["entries"]}
    for section in data["sections"]:
        for group in section["groups"]:
            keep = []
            for item in group["items"]:
                if item.pop("_delete", False):
                    key = H.item_key(item)
                    if key not in denied:
                        reason = next((r for n, r in removed if n == H.display_name(item)),
                                      "removed by automated refresh")
                        deny["entries"].append({"key": key, "name": H.display_name(item),
                                                "reason": reason, "date": now})
                        denied.add(key)
                    continue
                keep.append(item)
            group["items"] = keep
    H.save(os.path.join(ROOT, "data/denylist.json"), deny)

    live = sum(1 for _, _, i in H.iter_items(data) if "unavailableSince" not in i)
    data["meta"]["snapshot"] = now
    data["meta"]["total"] = live
    data["meta"]["officialPicks"] = sum(
        1 for _, _, i in H.iter_items(data)
        if i.get("official") and "unavailableSince" not in i)
    H.save(DATA, data)

    lines = [f"Refreshed {len(items)} entries on {now}. {live} live."]

    def block(title, rows, fmt):
        if not rows:
            return
        lines.append("")
        lines.append(f"**{title}** ({len(rows)})")
        lines.extend(fmt(r) for r in rows[:40])
        if len(rows) > 40:
            lines.append(f"…and {len(rows) - 40} more")

    block("Metrics changed", changed, lambda r: f"- {r[0]} — {r[1]}")
    block("Renamed", renamed, lambda r: f"- {r[0]} → {r[1]}")
    block("Newly unreachable (hidden, kept for %d days)" % H.GRACE_DAYS, hidden,
          lambda r: f"- {r[0]} — {r[1]}")
    block("Back online", restored, lambda r: f"- {r}")
    block("Removed", removed, lambda r: f"- {r[0]} — {r[1]}")
    block("⚠️ Popularity collapsed — check for purged fake stars", collapsed,
          lambda r: f"- {r[0]} — {r[1]}")
    block("Now below the entry bar (reported only, not removed)", below,
          lambda r: f"- {r[0]} — {r[1]}")
    block("Could not be checked this run (left untouched)", unknown,
          lambda r: f"- {r[0]} — {r[1]}")

    report = "\n".join(lines)
    print(report)
    with open(os.path.join(ROOT, "refresh-report.md"), "w", encoding="utf-8") as f:
        f.write(report + "\n")

    # A one-line commit subject for the workflow.
    bits = []
    if changed: bits.append(f"{len(changed)} metrics")
    if renamed: bits.append(f"{len(renamed)} renamed")
    if hidden: bits.append(f"{len(hidden)} unreachable")
    if restored: bits.append(f"{len(restored)} restored")
    if removed: bits.append(f"{len(removed)} removed")
    if collapsed: bits.append(f"{len(collapsed)} collapsed")
    subject = f"Refresh entry data ({', '.join(bits)})" if bits else "Refresh entry data"
    with open(os.path.join(ROOT, "refresh-subject.txt"), "w", encoding="utf-8") as f:
        f.write(subject + f" — {now}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
