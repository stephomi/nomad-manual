#!/usr/bin/env python3
import os
import re
from typing import List, Dict, Tuple

EN_DIR    = "docs"
I18N_DIR = "docs/i18n"

HEAD    = re.compile(r'^(#+)\s+(.*)$')
ANCHOR = re.compile(r'\s*\{#([^}]+)\}\s*$')
ICON    = re.compile(r'^!\[[^\]]*\]\([^)]+\)\s*')

try:
    langs = [
        d for d in os.listdir(I18N_DIR)
        if os.path.isdir(os.path.join(I18N_DIR, d))
    ]
except FileNotFoundError:
    langs = []

def norm(a: str) -> str:
    """Normalizes text into a URL-friendly anchor string."""
    a = a.lower()
    a = re.sub(r'[^a-z0-9-]+', '-', a)
    a = re.sub(r'-+', '-', a)
    return a.strip('-')

def find_anchor(line: str) -> str | None:
    """Extracts custom anchor from a heading line."""
    m = ANCHOR.search(line)
    return m.group(1) if m else None

for fname in os.listdir(EN_DIR):
    if not fname.endswith(".md"):
        continue

    en_path = os.path.join(EN_DIR, fname)
    
    try:
        with open(en_path, encoding="utf8") as f:
            en_lines = f.read().splitlines()
    except Exception as e:
        print(f"Error reading {en_path}: {e}")
        continue

    # Stores essential EN heading data: (line_index, final_anchor)
    # The list index is the heading's ordinal position (0, 1, 2, ...)
    en_heading_data: List[Tuple[int, str]] = []

    # --- Pass 1: Collect all EN headings and determine anchors ---
    for i, line in enumerate(en_lines):
        m = HEAD.match(line)
        if not m:
            continue

        final_anchor = None
        
        # 1. Check for custom anchor
        a = find_anchor(line)
        if a:
            final_anchor = norm(a)
        else:
            # 2. Generate from EN heading text
            text = m.group(2)
            text = ICON.sub("", text)
            text = ANCHOR.sub("", text)
            text = text.strip()
            
            if text:
                final_anchor = norm(text)
        
        if final_anchor:
            en_heading_data.append((i, final_anchor))

    if not en_heading_data:
        continue

    # --- Pass 2: Rewrite EN with its own anchors (Still requires line index) ---
    en_anchors_by_line: Dict[int, str] = {idx: anchor for idx, anchor in en_heading_data}
    
    out_en = []
    for i, line in enumerate(en_lines):
        if i in en_anchors_by_line and HEAD.match(line):
            # Strip any existing anchor and append the final EN anchor
            line_no_anchor = ANCHOR.sub("", line).rstrip()
            out_en.append(f"{line_no_anchor} {{#{en_anchors_by_line[i]}}}")
        else:
            out_en.append(line)
            
    try:
        with open(en_path, "w", encoding="utf8") as f:
            f.write("\n".join(out_en))
        print("fixed:", en_path)
    except Exception as e:
        print(f"Error writing to {en_path}: {e}")


    # --- Pass 3: Rewrite ALL i18n using EN anchors (Position-based match) ---
    en_heading_count = len(en_heading_data)
    
    for lang in langs:
        path = os.path.join(I18N_DIR, lang, fname)
        if not os.path.exists(path):
            continue
            
        try:
            with open(path, encoding="utf8") as f:
                i18n_lines = f.read().splitlines()
        except Exception as e:
            print(f"Error reading {path}: {e}")
            continue

        i18n_heading_lines: List[Tuple[int, str]] = [] # Stores (line_index, raw_heading_line)
        
        # 1. Find all heading lines in the i18n file and store by position
        for i, line in enumerate(i18n_lines):
            if HEAD.match(line):
                i18n_heading_lines.append((i, line))
        
        i18n_heading_count = len(i18n_heading_lines)
        
        # 2. Check and warn if heading counts are mismatched
        if i18n_heading_count != en_heading_count:
            print(f"⚠️ WARNING: Skipping {path} due to heading count mismatch.")
            print(f"   EN has {en_heading_count} headings, {lang} has {i18n_heading_count}. Anchors are unreliable.")
            continue # Skip to the next language file

        # 3. Apply EN anchors based on position (index 0 gets EN index 0 anchor, etc.)
        i18n_overwrite_map: Dict[int, str] = {} # line_index -> final_anchor_string
        
        for pos in range(en_heading_count):
            en_anchor = en_heading_data[pos][1] # Get the final anchor string from EN
            i18n_line_idx = i18n_heading_lines[pos][0] # Get the actual line index from i18n
            
            i18n_overwrite_map[i18n_line_idx] = en_anchor

        # 4. Rewrite i18n file
        out_i18n = []
        for i, line in enumerate(i18n_lines):
            if i in i18n_overwrite_map:
                # This line is a heading in i18n that needs an enforced anchor
                
                # Strip any existing anchor and enforce the EN anchor
                line_no_anchor = ANCHOR.sub("", line).rstrip()
                en_anchor_string = i18n_overwrite_map[i]
                
                out_i18n.append(f"{line_no_anchor} {{#{en_anchor_string}}}")
            else:
                out_i18n.append(line)
        
        try:
            with open(path, "w", encoding="utf8") as f:
                f.write("\n".join(out_i18n))
            print("fixed:", path)
        except Exception as e:
            print(f"Error writing to {path}: {e}")


print("done")