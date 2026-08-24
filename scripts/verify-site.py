#!/usr/bin/env python3
"""Offline correctness checks for the finmedtech.co.uk static site (TSW-630).

This repo's whole job is serving the right document at the right URL, so that is what
this asserts. Every check reasons about the repo's own files and `vercel.json` — there
are NO network calls, deliberately:

  * a PR's changes are not deployed yet, so curling production would assert the OLD
    state and pass on a broken diff;
  * network checks are flaky in CI and turn a correctness gate into a coin flip.

What determines behaviour after deploy is the file tree plus the redirect table, and
both are right here.

Run:  python3 scripts/verify-site.py     (exit 0 = pass, 1 = failures printed)
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TS = "https://taxswipe.co.uk"

failures: list[str] = []
checks = 0


def check(ok: bool, label: str, detail: str = "") -> None:
    global checks
    checks += 1
    if ok:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}")
        if detail:
            print(f"       {detail}")
        failures.append(label)


# --- vercel.json ------------------------------------------------------------------

print("vercel.json")
try:
    CFG = json.loads((ROOT / "vercel.json").read_text())
    check(True, "vercel.json parses as JSON")
except Exception as exc:  # noqa: BLE001 - report any parse error verbatim
    check(False, "vercel.json parses as JSON", str(exc))
    print("\nCannot continue without a parseable redirect table.")
    sys.exit(1)

REDIRECTS = CFG.get("redirects", [])
check(bool(REDIRECTS), "vercel.json declares redirects")


def to_regex(source: str) -> re.Pattern:
    """Vercel `:path*` matches zero or more trailing segments."""
    return re.compile("^" + re.escape(source).replace(r"/:path\*", "(?:/.*)?") + "$")


COMPILED = [(to_regex(r["source"]), r) for r in REDIRECTS]


def resolve(path: str):
    """First matching rule wins — Vercel evaluates the array in order."""
    for rx, rule in COMPILED:
        if rx.match(path):
            return rule["destination"], rule.get("permanent", False)
    return None, None


# --- redirect table ---------------------------------------------------------------
#
# The stale-Terms defect (TSW-620) was that a legacy route served a local document
# instead of taxswipe.co.uk. These assertions are that defect, pinned.

print("\nredirect table — legacy TaxSwipe routes")
EXPECTED = {
    "/taxswipe/terms": f"{TS}/terms",
    "/taxswipe/terms.html": f"{TS}/terms",
    "/taxswipe/privacy": f"{TS}/privacy",
    "/taxswipe/privacy.html": f"{TS}/privacy",
    "/taxswipe": f"{TS}/",
    "/taxswipe/": f"{TS}/",
    "/taxswipe/index.html": f"{TS}/",
    "/taxswipe/anything-else": f"{TS}/",
    "/taxnav/terms": f"{TS}/terms",
    "/taxnav/privacy": f"{TS}/privacy",
    "/taxnav": f"{TS}/",
    "/taxnav/anything-else": f"{TS}/",
}
for route, want in EXPECTED.items():
    got, permanent = resolve(route)
    check(got == want, f"{route} -> {want}", f"resolved to {got!r}")
    if got == want:
        check(permanent is True, f"{route} is a permanent redirect", f"permanent={permanent!r}")

print("\nredirect table — routes that must NOT be redirected away")
for route in ("/", "/privacy-policy", "/terms-of-use", "/bp-tracker", "/bp-tracker/privacy-policy"):
    got, _ = resolve(route)
    check(got is None, f"{route} is served, not redirected", f"unexpectedly redirects to {got!r}")

print("\nredirect table — no TaxSwipe legal document is served from this repo")
for stale in ("taxswipe/terms.html", "taxswipe/privacy.html", "taxswipe/index.html"):
    check(not (ROOT / stale).exists(), f"{stale} does not exist", "a redirect shadows it, but the file must be gone (TSW-620)")


# --- route resolution -------------------------------------------------------------

HTML_FILES = sorted(
    p for p in ROOT.rglob("*.html")
    if ".git" not in p.parts and "node_modules" not in p.parts
)


def route_exists(path: str) -> bool:
    """Does this site path serve something? `cleanUrls` means /foo -> foo.html."""
    if resolve(path)[0] is not None:
        return True                      # a redirect rule handles it
    rel = path.strip("/")
    if rel == "":
        return (ROOT / "index.html").exists()
    for candidate in (f"{rel}.html", f"{rel}/index.html", rel):
        if (ROOT / candidate).exists():
            return True
    return False


print("\ninternal links in served HTML resolve")
seen: set[tuple[str, str]] = set()
for html in HTML_FILES:
    rel_name = html.relative_to(ROOT).as_posix()
    for href in re.findall(r'href="(/[^"]*)"', html.read_text()):
        key = (rel_name, href)
        if key in seen:
            continue
        seen.add(key)
        check(route_exists(href), f"{rel_name} -> {href}", "no file and no redirect rule serves this path")


# --- documented URLs --------------------------------------------------------------
#
# This is the check that catches the TSW-620 README error: `/privacy` was documented
# as the company Privacy Policy, but the file is privacy-policy.html, so it 404s.

print("\nfinmedtech.co.uk URLs documented in Markdown resolve")
for md in sorted(p for p in ROOT.glob("*.md")):
    text = md.read_text()
    for url in sorted(set(re.findall(r"finmedtech\.co\.uk(/[a-zA-Z0-9/._-]*)", text))):
        path = url.rstrip(".,)")
        check(route_exists(path), f"{md.name} documents {path}", "documented URL resolves to nothing — wrong path?")


# --- result -----------------------------------------------------------------------

print("\n" + "-" * 60)
if failures:
    print(f"FAILED  {len(failures)} of {checks} checks")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print(f"PASSED  {checks} checks")
