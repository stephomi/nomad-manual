# Translation sync

The locales in `docs/i18n/` match the English pages as of the commit that last changed this file.
To see what the next sync has to translate:

```sh
git diff $(git log -1 --format=%H -- .agents/translations.md) -- docs/*.md
```

Last sync: 2026-11-19, all 22 locales, all pages, retranslated from scratch (not a diff). UI labels
now follow the app's own translations (`.agents/labels.py`), and each locale has its theme strings
in `docs/.vitepress/locales/<locale>.json`. Next syncs go back to the diff.

Choices made during that pass, to keep in later syncs:
- Address form follows the app's help texts: formal in de, cs, ru, tr, id, zh (您), ja (です/ます);
  informal elsewhere (tu, tú, du, je, ty...).
- `pt` is Brazilian Portuguese, like the app.
- Labels the app doesn't translate (`Overall Subdivision`, `Log events`, `Head`, `(All)`...) are
  translated naturally or built from translated parts; product and algorithm names stay English.
- Where the app's string is stale or wrong (the bottom bar / floating windows headings still say
  "Add shortcuts...", `history.replay.reverse` in ko/zh), the page uses plain wording instead.
