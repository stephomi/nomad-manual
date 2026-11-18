#!/usr/bin/env python3
"""Check that translated pages mirror their English page in structure.

    python3 .agents/check_i18n.py                 # every locale, every page
    python3 .agents/check_i18n.py fr de           # some locales
    python3 .agents/check_i18n.py fr --page tools.md

Compared, in order: headings (level + anchor), images/icons/videos, link targets, callouts,
tool family spans, list items, table rows, raw HTML tags. Also flags prose lines left identical to
the English (likely untranslated) and pages missing from a locale. Exit code 1 on any mismatch.
"""
import argparse
import glob
import os
import re
import sys

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../docs")

FEATURES = {
    "headings": (re.compile(r"^(#{1,6}) .*?(\{#[^}]+\})?\s*$", re.M), lambda m: m.group(1) + (m.group(2) or "")),
    "media": (re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)"), lambda m: m.group(1)),
    "links": (re.compile(r"(?<!!)\[(?:[^\]\[]|\[[^\]]*\])*\]\(([^)\s]+)\)"), lambda m: m.group(1)),
    "callouts": (re.compile(r"^:::[ \t]*(\w*)", re.M), lambda m: m.group(1) or "/"),
    "spans": (re.compile(r'<span class="([^"]+)"'), lambda m: m.group(1)),
    "list items": (re.compile(r"^\s*(?:[*-]|\d+\.) ", re.M), lambda m: "item"),
    "table rows": (re.compile(r"^\s*\|", re.M), lambda m: "row"),
    "html": (re.compile(r"<(div|iframe|style|br|h3)\b"), lambda m: m.group(1)),
}


def strip_code(text):
    return re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)


def features(text):
    text = strip_code(text)
    return {k: [f(m) for m in r.finditer(text)] for k, (r, f) in FEATURES.items()}


def prose(text):
    out = set()
    for line in strip_code(text).splitlines():
        s = line.strip()
        if len(s) > 40 and not s.startswith(("|", "!", "<", ":::", "#")) and re.search(r"[a-z]{3} [a-z]{3}", s):
            out.add(s)
    return out


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return f"#{i + 1}: en {x!r} vs {y!r}"
    return f"en has {len(a)}, translation {len(b)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("locales", nargs="*")
    ap.add_argument("--page", action="append", default=[])
    a = ap.parse_args()
    locales = a.locales or sorted(os.path.basename(d) for d in glob.glob(f"{DOCS}/i18n/*") if os.path.isdir(d))
    pages = [p if p.endswith(".md") else p + ".md" for p in a.page] or sorted(os.path.basename(f) for f in glob.glob(f"{DOCS}/*.md"))
    bad = 0
    for page in pages:
        en_text = open(f"{DOCS}/{page}", encoding="utf-8").read()
        en, en_prose = features(en_text), prose(en_text)
        for loc in locales:
            path = f"{DOCS}/i18n/{loc}/{page}"
            if not os.path.exists(path):
                print(f"{loc}/{page}: missing")
                bad += 1
                continue
            text = open(path, encoding="utf-8").read()
            tr = features(text)
            for k in FEATURES:
                if en[k] != tr[k]:
                    print(f"{loc}/{page}: {k} differ, {first_diff(en[k], tr[k])}")
                    bad += 1
            same = sorted(en_prose & prose(text))
            if same:
                print(f"{loc}/{page}: {len(same)} English line(s) left, e.g. {same[0][:80]!r}")
                bad += 1
    print("ok" if not bad else f"{bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
