"""Shared helpers for the maintenance scripts.

Networking note: urllib's default opener honours HTTP_PROXY/HTTPS_PROXY. On a
dev machine behind a local proxy that is what makes these calls work; on a
GitHub Actions runner those variables are unset and the same code goes direct.
Do not "fix" this by forcing ProxyHandler({}).
"""
from __future__ import annotations

import json
import os
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

UA = "awesome-minimax-h3-maintenance (+https://github.com/AtlasCloudAI/awesome-minimax-h3)"

# Entry bar, kept in sync with README/CONTRIBUTING. Official picks are exempt.
THRESHOLDS = {"github": 50, "hf": 10, "civitai": 500}

# An entry that goes unreachable is hidden immediately but only deleted after
# this many days, so a transient outage never silently drops a good project.
GRACE_DAYS = 21

# Substrings that disqualify a project on sight. Matched case-insensitively
# against owner/repo/title/description. Deliberately blunt: this only gates
# *automated discovery*, and a false positive costs us one missed suggestion.
BLOCK_TERMS = (
    "nsfw", "porn", "hentai", "erotic", "eros", "nude", "naked", "uncensored",
    "heretic", "abliterated", "onlyfans", "sexy", "lewd", "fetish", "boob",
    "undress", "deepnude", "r18", "18plus", "adult-content",
    # Suggestive-but-flagged-SFW phrasings seen on Civitai's H3 pages.
    "ai girl", "fictional women", "waifu", "bikini", "lingerie",
)


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def days_since(iso: str) -> int:
    try:
        return (date.fromisoformat(today()) - date.fromisoformat(iso)).days
    except ValueError:
        return 0


def blocked(*texts: str) -> str | None:
    """Returns the offending term, or None."""
    blob = " ".join(t for t in texts if t).lower()
    for term in BLOCK_TERMS:
        if term in blob:
            return term
    return None


def _gh_cli_token() -> str:
    """Local convenience: Actions sets GITHUB_TOKEN, a dev machine has gh."""
    try:
        import subprocess
        out = subprocess.run(["gh", "auth", "token"], capture_output=True,
                             text=True, timeout=10)
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


class Fetcher:
    """HTTP with retries. Distinguishes 'the server said no' from 'we failed'."""

    def __init__(self, gh_token: str | None = None, hf_token: str | None = None):
        self.gh_token = gh_token or os.environ.get("GITHUB_TOKEN") or _gh_cli_token()
        self.hf_token = hf_token or os.environ.get("HF_TOKEN") or ""
        self.opener = urllib.request.build_opener()
        self.ctx = ssl.create_default_context()

    def _raw(self, url: str, headers: dict | None = None, method: str = "GET",
             timeout: int = 40) -> tuple[int, bytes]:
        req = urllib.request.Request(url, method=method,
                                     headers={"User-Agent": UA, **(headers or {})})
        resp = self.opener.open(req, timeout=timeout)
        return resp.status, resp.read()

    def get(self, url: str, headers: dict | None = None, tries: int = 4,
            method: str = "GET") -> tuple[int, bytes]:
        """(status, body). status -1 means we never got an answer.

        429 and 5xx are retried with backoff; 4xx is returned as-is because
        it is a real answer about the resource.
        """
        delay = 2.0
        last = -1
        for attempt in range(tries):
            try:
                return self._raw(url, headers, method)
            except urllib.error.HTTPError as e:
                last = e.code
                hdrs = e.headers or {}
                if e.code == 403 and str(hdrs.get("X-RateLimit-Remaining", "")) == "0":
                    reset = hdrs.get("X-RateLimit-Reset")
                    wait = 60.0
                    if reset and str(reset).isdigit():
                        wait = max(5.0, min(float(reset) - time.time() + 3, 120.0))
                    time.sleep(wait)
                    continue
                if e.code in (429, 500, 502, 503, 504):
                    # Respect Retry-After when the server sends one.
                    wait = e.headers.get("Retry-After") if e.headers else None
                    time.sleep(min(float(wait), 90) if wait and str(wait).isdigit() else delay)
                    delay *= 2
                    continue
                return e.code, b""
            except Exception:
                time.sleep(delay)
                delay *= 2
        return last, b""

    def json(self, url: str, headers: dict | None = None, tries: int = 4):
        st, body = self.get(url, headers, tries)
        if st != 200:
            return st, None
        try:
            return st, json.loads(body)
        except json.JSONDecodeError:
            return st, None

    # --- per-host wrappers -------------------------------------------------
    def github(self, path: str, tries: int = 4):
        h = {"Accept": "application/vnd.github+json"}
        if self.gh_token:
            h["Authorization"] = f"Bearer {self.gh_token}"
        return self.json(f"https://api.github.com/{path.lstrip('/')}", h, tries)

    def hf(self, path: str, tries: int = 4):
        h = {"Authorization": f"Bearer {self.hf_token}"} if self.hf_token else {}
        return self.json(f"https://huggingface.co/api/{path.lstrip('/')}", h, tries)

    def civitai(self, path: str, tries: int = 4):
        return self.json(f"https://civitai.com/api/v1/{path.lstrip('/')}", None, tries)


# --- data helpers ----------------------------------------------------------

def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def iter_items(data: dict):
    for section in data["sections"]:
        for group in section["groups"]:
            for item in group["items"]:
                yield section, group, item


def owner_of(kind: str, ident: str) -> str:
    """Publisher handle, lowercased. Empty when the source has no concept of one."""
    if kind in ("gh", "hf", "hfs") and "/" in ident:
        return ident.split("/", 1)[0].lower()
    return ""


def split_denylist(deny: dict) -> tuple[set[str], set[str]]:
    """(exact keys, blocked owners). Owner rules read `owner:<handle>`.

    Exact keys alone are not enough: a publisher of adult-oriented models only
    has to rename a repo to slip back into the discovery queue.
    """
    keys, owners = set(), set()
    for entry in deny.get("entries", []):
        key = entry["key"]
        (owners if key.startswith("owner:") else keys).add(
            key.split("owner:", 1)[-1] if key.startswith("owner:") else key)
    return keys, owners


def item_key(item: dict) -> str:
    """Stable identity across renames, for dedupe and the denylist."""
    kind = item.get("kind")
    if kind == "gh":
        return "gh:" + item["url"].split("github.com/", 1)[-1].strip("/").lower()
    if kind == "hf":
        return "hf:" + item["url"].split("huggingface.co/", 1)[-1].strip("/").lower()
    if kind == "hfs":
        return "hfs:" + item["url"].split("spaces/", 1)[-1].strip("/").lower()
    if kind == "civitai":
        return "civitai:" + item["url"].rstrip("/").rsplit("/", 1)[-1]
    return "url:" + item["url"].split("?", 1)[0].lower()


def display_name(item: dict, locale: str = "en") -> str:
    name = item.get("name")
    return name if isinstance(name, str) else name[locale]
