#!/usr/bin/env python3
import os
import re
import json
from urllib.request import urlopen, Request

# load .env
if os.path.exists(".env"):
    for line in open(".env"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ[k.strip()] = v.strip().strip('"').strip("'")

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL_NAME")

HEAD = re.compile(r'^(#+)\s+(.*)$')

def get_prompt(fname, lang):
    return f"""\
Context: This markdown file is part of a 3D sculpting / rendering manual (Nomad Sculpt).
Filename: {fname}

Translate only the heading LABEL from English to {lang}.
Do NOT translate or modify the icon starting with ![](...)
Do NOT generate, modify, or remove anchors.
Your output MUST be a JSON list of translated headings only.
Each output item must include the leading hashes and icon if present, but NOT anchors.

Example format (headings only):
[
  "# Mon titre",
  "## ![](/icons/x.webp) Lumière",
  "### Paramètres du matériau"
]
"""

langs = [
    "fr","zh-hans","zh-hant","es","de","cs","nl","sv","it","pl",
    "pt","ja","ko","th","vi","ms","id","hi","ru","tr","ar","he"
]

def anchor_from_english(label):
    return re.sub(r'[^a-z0-9\- ]+', '', label.lower()).replace(" ", "-")

def translate_file(fname, labels_full, lang):
    prompt = [
        {"role": "system", "content": get_prompt(fname, lang)},
        {"role": "user", "content": json.dumps(labels_full)}
    ]
    data = json.dumps({"model": MODEL, "messages": prompt}).encode("utf8")
    req = Request(
        "https://api.openai.com/v1/chat/completions",
        data=data,
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {API_KEY}"}
    )
    raw = urlopen(req).read().decode("utf8")
    res = json.loads(raw)
    return json.loads(res["choices"][0]["message"]["content"])


for lang in langs:
    print(f"\033[32m---- {lang} ----\033[0m")

    for fname in os.listdir("docs"):
        if not fname.endswith(".md"):
            continue

        src = open(f"docs/{fname}", encoding="utf8").read().splitlines()
        tgt_path = f"docs/i18n/{lang}/{fname}"
        if not os.path.exists(tgt_path):
            continue
        tgt = open(tgt_path, encoding="utf8").read().splitlines()

        labels_full = []     # full heading "# + icon + label" (NO anchor)
        labels_clean = []    # raw english label without "#" / icon / anchor

        for line in src:
            m = HEAD.match(line)
            if m:
                full = m.group(0)
                full = re.sub(r'\s*\{#.*\}$', '', full)
                labels_full.append(full)

                label = m.group(2)
                label = re.sub(r'\s*\{#.*\}$', '', label)
                labels_clean.append(label)

        if not labels_full:
            continue

        print(f"\033[36m- file: {fname}\033[0m")

        translated_headings = translate_file(fname, labels_full, lang)

        if len(translated_headings) != len(labels_full):
            print("\033[31mCOUNT MISMATCH, SKIPPING FILE\033[0m", fname, len(translated_headings), len(labels_full))
            continue

        ti = 0
        out = []
        for line in tgt:
            m = HEAD.match(line)
            if m:
                tr_full = translated_headings[ti]
                en_label = labels_clean[ti]
                label_no_icon = re.sub(r'^!\[[^\]]*\]\([^)]+\)\s*', '', en_label)
                anchor = anchor_from_english(label_no_icon)
                out.append(f"{tr_full} {{#{anchor}}}")
                ti += 1
            else:
                out.append(line)

        open(tgt_path, "w", encoding="utf8").write("\n".join(out))
        print("fixed:", tgt_path)

print("done")
