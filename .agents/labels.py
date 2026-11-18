#!/usr/bin/env python3
"""How the app translates a UI label, from ../nomad-translation/locales/*.strings.

    python3 .agents/labels.py fr "Radius" "Lock + radius"   # by English label
    python3 .agents/labels.py fr --key tool.radius           # by key
    python3 .agents/labels.py fr --grep remesh               # English labels containing a word

A label matches English values case-insensitively. Several keys can share one English label with
different translations: pick the key that fits the context (its prefix names the menu or tool).
Prints `key | English | translation`. Help texts (`*.help`) are left out unless --help-texts.
"""
import argparse
import os
import re

LOCALES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../nomad-translation/locales")
FILES = {
    "en": "english", "ar": "arabic", "cs": "czech", "de": "german", "es": "spanish", "fr": "french",
    "he": "hebrew", "hi": "hindi", "id": "indonesian", "it": "italian", "ja": "japanese", "ko": "korean",
    "ms": "malay", "nl": "dutch", "pl": "polish", "pt": "portuguese", "ru": "russian", "sv": "swedish",
    "th": "thai", "tr": "turkish", "vi": "vietnamese", "zh-hans": "simplified-chinese",
    "zh-hant": "traditional-chinese",
}
ENTRY = re.compile(r'^([A-Za-z0-9_.]+) = "(.*?)";$', re.M | re.S)


def load(locale):
    with open(os.path.join(LOCALES, FILES[locale] + ".strings"), encoding="utf-8") as f:
        return dict(ENTRY.findall(f.read()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("locale", choices=sorted(FILES))
    ap.add_argument("labels", nargs="*")
    ap.add_argument("--key", action="append", default=[])
    ap.add_argument("--grep", action="append", default=[])
    ap.add_argument("--help-texts", action="store_true")
    a = ap.parse_args()
    en, tr = load("en"), load(a.locale)

    def show(keys):
        keys = [k for k in keys if a.help_texts or not k.endswith(".help")]
        for k in keys:
            print(f"{k} | {en[k]} | {tr.get(k, '(missing)')}")
        return keys

    for label in a.labels:
        if not show(sorted(k for k, v in en.items() if v.lower() == label.lower())):
            print(f"(no label '{label}': keep the English label)")
    for k in a.key:
        show([k] if k in en else [])
    for word in a.grep:
        show(sorted(k for k, v in en.items() if word.lower() in v.lower()))


if __name__ == "__main__":
    main()
