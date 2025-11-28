#!/usr/bin/env bash
set -e

# load API key + model from .env
source .env

langs=(
    "fr"
    "zh-hans"
    "zh-hant"
    "es"
    "de"
    "cs"
    "nl"
    "sv"
    "it"
    "pl"
    "pt"
    "ja"
    "ko"
    "th"
    "vi"
    "ms"
    "id"
    "hi"
    "ru"
    "tr"
    "ar"
    "he"
)

prompt_common="
You are a professional technical translator.
Preserve ALL Markdown formatting exactly.
Do NOT summarize, reorder or comment.
Output ONLY the translated Markdown.

For headings, translate it but keep anchor intact in English.
If there is no anchor add it.
For example if you have
# my title
It should become
# mon-titre {#my-title}
# mi-titulo {#my-title}
"

for lang in "${langs[@]}"; do
    mkdir -p "docs/$lang"

    for f in docs/*.md; do
        base=$(basename "$f")
        out="docs/$lang/$base"

        {
            echo "Translate the following Markdown document into: $lang."
            echo
            printf "%s" "$prompt_common"
        } >prompt.md

        chatgpt-md-translator "$f" --out "$out"
    done
done

rm -f prompt.md
echo "done"
