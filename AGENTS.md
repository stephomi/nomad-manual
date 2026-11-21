# Nomad Sculpt Manual

User manual for Nomad Sculpt, published at https://nomadsculpt.com/manual/. Built with VitePress.
The manual is maintained by AI agents: English is the source, and agents translate it into 22
locales in a sync pass before publishing. There is no external translation service.

## Scope

- Edit only this repository.
- The Nomad app repository (`../nomad`) is for reference: reading UI code, checking feature behavior,
  and running the app to take screenshots. Never modify it, except its AI API (`.agents/ai.py`,
  `.agents/ai-api.md`, `src/gui/GuiApiAI.cpp`) when screenshots need it; build it only in an
  isolated worktree linked under `../nomad/build*` (the `ai=` option needs that path).
- UI labels and their help texts live in `../nomad/assets/locales/english.strings`: the best source
  when describing an option.

## Layout

- `docs/*.md`: English pages, the source of truth.
- `docs/i18n/<locale>/*.md`: translations, one file per English page, same file names.
  Locales: `ar cs de es fr he hi id it ja ko ms nl pl pt ru sv th tr vi zh-hans zh-hant`.
- `docs/images/*.webp`: screenshots. `docs/icons/*.webp`: UI icons.
- `docs/videos/<name>.mp4` (Git LFS) with a `<name>.webp` poster next to it.
- `docs/public/`: logos, favicon.
- `docs/.vitepress/config.mts`: site config, sidebar order, locales, custom image/video rendering,
  offline (MPA) link rewriting.
- `docs/.vitepress/theme/`: theme extension (image zoom) and CSS.

## Commands

```sh
npm install
npm run dev       # local preview
npm run build     # output in ../dist/manual
npm run pdf
```

`IS_MPA` (offline build) and `ONLY_EN` (skip translations, faster dev) are flags at the top of
`config.mts`. Leave them `false` in commits.

## Tone

Match the existing pages when adding or rewriting text:

- Friendly and plain, addressed to the reader as "you". Explains like an experienced user helping a
  newcomer, not like a spec. Short encouragement is fine ("It's worth persisting!").
- Practical: say what the option does, then when or why you'd use it. Workflow advice and
  comparisons with other apps (ZBrush, Blender, 2d paint apps) go in `::: tip` boxes.
- Option sections are short: a `###` heading named like the UI label, then one to three sentences.
  Lists of modes use `` * `Name` - description ``. Menus with many actions use a table with an icon
  column.
- Each page starts with its icon title, a one-line summary of the menu, then an overview screenshot.
- Write "3d" and "2d" in lowercase, as the rest of the manual does.

## Writing pages

- Every heading carries an explicit anchor: `## Radius {#radius}`. Lowercase, hyphens, unique in the
  page (a repeat gets `-1`, as in `{#stroke-1}`).
- **Never rename or remove an existing anchor.** The app links straight to some of them (for example
  `faq#how-to-restore-my-purchase`), and pages link to each other's anchors. When a heading's text
  changes, keep its old anchor.
- Page title: the first heading, optionally with an icon: `# ![](/icons/pencil.webp) Stroke {#stroke}`.
  The sidebar reads it from there.
- Links between pages: `[Layers](layers.md#layers)`. Same page: `[Trim](#trim)`.
- Images: `![](/images/name.webp)`. Icons: `![](/icons/name.webp)`. Videos: `![](/videos/name.mp4)`,
  rendered as a `<video>` with the matching `.webp` as poster.
- Icons are inverted in light mode. Colored icons that must not be inverted are listed in the
  `colored` array in `config.mts`; add new colored icons there.
- UI labels go in backticks with their English app name: `` `Auto validate` ``.
- Callouts: `::: tip`, `::: warning`, `::: danger`, `::: details`, each closed with `:::`. An optional
  title follows the type: `::: tip New to Nomad?`.
- New page: add it to `order` in `config.mts` (same position as its menu in the app's top bar).
  No locale copy is needed: until a locale has the page, its sidebar shows the English title and
  links to the English page. The sync pass creates the translated pages.

## Translations

Work on English only. The locales are updated in one sync pass, when the user asks for it or before
publishing, so text that is still being revised is translated once, from its final version.

The sync point is the last commit that changed `.agents/translations.md`. A sync:

1. Lists what changed since then:
   `git diff $(git log -1 --format=%H -- .agents/translations.md) -- docs/*.md`
   (plus uncommitted changes, with `git diff HEAD -- docs/*.md`).
2. Applies those changes to every locale, split across parallel agents by locale group. Each agent
   follows `.agents/translate.md` (its brief: label lookup, structure rules, style). The theme's own
   strings (search box, page footer...) are in `docs/.vitepress/locales/<locale>.json`, same keys
   as `en.json`.
3. Runs `python3 .agents/check_i18n.py` (structure of every page against English), the anchor check
   below, and `npm run build`.
4. Updates the date in `.agents/translations.md`, so the user's next commit becomes the new sync
   point.

Pure English fixes (typos, grammar) that don't change the meaning need no translation.

A translated page mirrors its English page line for line in structure:

- Same headings, in the same order and count. Translate the heading text; copy the `{#anchor}` verbatim.
- Same images, icons, videos, tables (rows and columns), lists, and callouts.
- Link text is translated; link targets (`page.md#anchor`) are copied verbatim.
- Backticked UI labels are written as the app shows them in that language, from its own
  translations: `python3 .agents/labels.py <locale> "<English label>"` (several keys can share a
  label: pick the one whose key fits the menu or tool). Page titles and menu names in the text
  follow the app too. Anything the app doesn't translate (file formats, key names, paths, values)
  stays as on the English page.
- Callout types (`tip`, `warning`...) stay as they are; a callout title is translated.
- Arabic and Hebrew are right-to-left; the config handles it, write the Markdown normally.

After editing, check that every locale has the same heading count and anchors as English:

```sh
for f in docs/*.md; do
  en=$(grep -o '{#[^}]*}' "$f")
  for l in docs/i18n/*/; do [ "$(grep -o '{#[^}]*}' "$l$(basename "$f")")" = "$en" ] || echo "mismatch: $l$(basename "$f")"; done
done
```

## Screenshots

- Taken in the Nomad app, driven through `../nomad/.agents/ai-api.md`. Running Nomad for manual
  screenshots is allowed.
- Stop the Nomad you started (`python3 ../nomad/.agents/ai.py stop`) before ending your turn, and
  check none is left (`pgrep -fl 'Nomad ai='`). The user can't tell otherwise whether it's in use.
- Workflow and capture helper: `.agents/screenshots.md` and `.agents/shot.py`. Videos:
  `.agents/videos.md`.
- Only the projects in the `manual` folder of the Nomad user folder may be used:
  `~/Downloads/data_nomad/cache/projects/manual/*.nom`. A fresh scene is fine too. Never open other
  projects. Never Nomad's default sphere (Files > New), and spread the models across images: pick
  the one that shows the page's feature (a stroke for Stroke, the painted bust for Paint...).
- Save as `docs/images/<page>_<topic>.webp`, matching the existing names. Every image goes through
  `.agents/webp.py` (shot.py and extras.py call it): width capped at 1440 px, lossy WebP 90 or
  lossless when that is as small. Encode from the raw capture only: re-encoding an already lossy
  image loses quality each time. Icons stay lossless (`.agents/icons.py`).
- Replace an outdated screenshot in place under the same file name, so no page needs editing.
- Delete images that no page references any more.

Nomad colors: `#262322`, `#363230`, accent `#ebbe6c`.
