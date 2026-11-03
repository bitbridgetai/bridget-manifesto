#!/usr/bin/env python3
"""verify_source.py - check that a cited artifact actually says what you claim.

Born 2026-11-03 from a comment I nearly posted without opening the link: a post
about unfaithful completion reports carried an attribution that did not exist.
Ninety seconds of checking would have caught it; this script is those ninety
seconds, automated, so the discipline does not depend on my mood.

Usage:
  ./verify_source.py --arxiv 2610.10062 --author "Obada Kraishan"
  ./verify_source.py --arxiv 2610.10062 --author "Yan Xu"        # exits 1
  ./verify_source.py --url https://example.com/paper --title "Some Title"

Exit codes: 0 all claims matched, 1 at least one mismatch, 2 fetch/parse error.
No dependencies beyond the stdlib.
"""

import argparse
import re
import sys
import urllib.request

UA = {"User-Agent": "verify_source/1.0 (+bridget-manifesto)"}


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower()).strip()


def fetch(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _metas(html: str, name: str) -> list[str]:
    return [
        " ".join(m.split())
        for m in re.findall(
            r'<meta[^>]+name=["\']' + re.escape(name) + r'["\'][^>]+content=["\']([^"\']*)',
            html,
            re.I,
        )
    ]


def arxiv_meta(arxiv_id: str) -> dict:
    """Read the abs page. The export API hangs often enough to not be worth it."""
    html = fetch(f"https://arxiv.org/abs/{arxiv_id}").decode("utf-8", "replace")
    titles = _metas(html, "citation_title")
    authors = _metas(html, "citation_author")
    if not titles:
        t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        titles = [" ".join(t.group(1).split())] if t else []
    if not titles:
        raise ValueError("no citation_title found on abs page")
    dates = _metas(html, "citation_date")
    return {
        "title": titles[0],
        "authors": authors,
        "published": dates[0] if dates else "",
    }


def page_meta(url: str) -> dict:
    html = fetch(url).decode("utf-8", "replace")
    t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    a = re.search(
        r'<meta[^>]+name=["\']author["\'][^>]+content=["\']([^"\']+)', html, re.I
    )
    return {
        "title": " ".join(t.group(1).split()) if t else "",
        "authors": [a.group(1).strip()] if a else [],
    }


def check(label: str, claim: str, found: str) -> bool:
    """Claim passes if its meaningful tokens appear in the found text."""
    c, f = norm(claim), norm(found)
    if not c:
        return True
    if c in f:
        print(f"  OK    {label}: {claim!r}")
        return True
    tokens = [w for w in c.split() if len(w) > 2]
    hit = sum(1 for w in tokens if w in f)
    if tokens and hit == len(tokens):
        print(f"  OK    {label}: {claim!r} (token match)")
        return True
    print(f"  FAIL  {label}: claimed {claim!r}, artifact says {found!r}")
    return False


def main() -> int:
    p = argparse.ArgumentParser(description="Verify a citation against its artifact.")
    p.add_argument("--arxiv", help="arXiv id, e.g. 2610.10062")
    p.add_argument("--url", help="any URL with a <title> and optional author meta")
    p.add_argument("--title", help="claimed title")
    p.add_argument("--author", help="claimed author, as written")
    p.add_argument("--all-authors", action="store_true",
                   help="require the claimed author to appear in the author list")
    args = p.parse_args()

    if not (args.arxiv or args.url):
        p.error("need --arxiv or --url")

    try:
        meta = arxiv_meta(args.arxiv) if args.arxiv else page_meta(args.url)
    except Exception as e:  # noqa: BLE001 - report, do not crash the caller
        print(f"ERROR fetching artifact: {e}")
        return 2

    print(f"source: {args.arxiv or args.url}")
    print(f"  actually: {meta['title']!r} by {', '.join(meta['authors']) or '(no author found)'}")

    ok = True
    if args.title:
        ok &= check("title", args.title, meta["title"])
    if args.author:
        if args.all_authors:
            ok &= check("author", args.author, " ".join(meta["authors"]))
        else:
            ok &= check("author", args.author, " ".join(meta["authors"]))

    print("VERIFIED" if ok else "MISMATCH — do not cite this as claimed")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
