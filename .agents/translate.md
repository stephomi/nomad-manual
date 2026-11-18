# Translating pages

Brief for an agent translating English pages (`docs/<page>.md`) into one locale
(`docs/i18n/<locale>/<page>.md`). Read `AGENTS.md` first (Tone, Writing pages, Translations).

## How

- Translate from the English page only. When a full pass is asked for, write each page from
  scratch: the old translations are machine translations, don't reuse their wording.
- Write files with the Write and Edit tools only, never through the shell (no `cat >`, heredoc,
  `sed -i`, `tee`, scripts that write files).
- Long pages: a single Write that is too long can fail. Write the page in parts: Write the first
  part ending with the line `<!-- continue -->`, then Edit that line into the next part (ending with
  the marker again), and remove the marker with the last part.
- When done, run `python3 .agents/check_i18n.py <locale> --page <page>` for each page and fix
  every reported problem.

## What to keep identical

- Structure, line for line: same headings in the same order and level, same images, icons, videos,
  tables (rows and columns), lists (same item count), callouts, `<span class="...">`, HTML blocks.
- `{#anchor}` after each heading: copied verbatim, never translated.
- Link targets (`page.md#anchor`, `#anchor`, URLs): copied verbatim. Link text is translated.
- Image and video paths, code blocks, file paths, file formats (OBJ, STL...), key names (Ctrl,
  Shift, ⌘), product names (Nomad, ZBrush, Blender, Procreate, Quad Remesher), email addresses, and
  people's names (the video grid on the home page).
- HTML comments (the home page has one): copied verbatim.
- Callout types (`tip`, `warning`, `danger`, `details`) stay; a callout title is translated.
- "3d" and "2d" stay lowercase.

## UI labels and terms

- Backticked UI labels are written as the app shows them in this language. Look them up in the
  app's own translations:
  `python3 .agents/labels.py <locale> "Radius" "Lock + radius"`. Several keys can share one
  English label; pick the key whose prefix fits the menu or tool being described (`tool.radius`
  on a tool page, `curve.radius` for curves...). Keep the backticks.
- A label the app doesn't have (no match): try its parts (`Cut • Mirror` is two labels), or
  `--grep` a word of it. If still nothing, the English page is naming something in its own words
  (`Top menus`, `Visibility`): translate it naturally, with the app's terms where they apply.
  Values, file formats, key names, paths stay as in English.
- Table cells naming an action (first column of action tables) are UI labels too.
- Page titles, menu names and tab names in the prose follow the app (`--grep` the menu name, e.g.
  `menu.` keys), so the sidebar reads like the app's top bar.
- Trap: the Topology menu's name is the key `topology`. `menu.topology` ("Misc") is the Misc tab
  inside it, not the menu.
- Recurring concepts in the prose (mask, face group, layer, stroke, falloff, alpha, voxel remesher,
  multiresolution, decimate, symmetry, gizmo, repeater, matcap, post process...) use the app's term
  for them, the same word on every page.
- Address the reader the way the app's help texts do (formal or informal "you"): check a few with
  `python3 .agents/labels.py <locale> --grep "you can" --help-texts`.

## Style

- Natural, friendly, plain, as a native experienced user explaining to a newcomer. Not word for
  word: rephrase so it reads as if written in this language. Keep the meaning and every detail.
- Use the conventions of the language: punctuation and spacing (French spaces before `:` and `?`,
  full-width punctuation in Chinese and Japanese), quotes, number formats inside prose.
- `pt` is Brazilian Portuguese (as the app). `zh-hans` simplified Chinese, `zh-hant` traditional
  Chinese (Taiwan usage). `ar` and `he` are right-to-left: write the Markdown normally.
