# App translation issues

Found in `../nomad/assets/locales/*.strings` during the 2026-11-19 retranslation of the manual. The
manual shows the app's labels, so fixing one here means updating the matching locale page at the
next sync (search the page for the old label).

## Several locales

- Bottom bar / floating windows shortcut labels are stale translations of the old "Add shortcuts..."
  strings (seen in it, es, ru, pl, vi, ko, th, tr, hi, ar; likely all). The pages use plain wording.
- `history.replay.reverse` is the multires "reverse subdivision" text in ko ("세분화 되돌리기"),
  zh-hans ("取消分割") and zh-hant ("反細分").
- `menu.shortcuts` and `menu.bindings` share one translation in fr, es, pt (Raccourcis / Atajos /
  Atalhos).
- Spot and Point lights share one word in cs ("Bodové") and id ("Titik").
- No translation anywhere: `Log events`, `Overall Subdivision`, the Head primitive, `(All)`, `On`,
  `Maximize`, `Preset...`, `Fix...`.

## Per locale

- ar: `tool.gizmo` is "أداة" ("tool"); Cursor and Indicator both "المؤشر"; Shading and Vignette both
  "التظليل"; hole `Fill` "املىء" looks misspelled (املأ); two words for Intensity.
- cs: run-together labels "SkupinaPovrch", "SmazatVrstva", "OdebratNepoužité"; typo "Přischnout"
  (Transform snap).
- de: "Ebene" for both layer and symmetry plane; `tool.layer` "Ebene" vs the Layers menu "Layer".
- es: "Multiresolución" vs "multirresolución"; gesture label `crear` in lowercase.
- he: Flatten "החלק" (reads as smooth), Relax "רוגע" (calm), Repeater "שכפול" (duplication);
  `topology.remesh` still English.
- hi: Tangents "छेड़छाड़" (tampering); Vignette "बेलबूटे" (embroidery); typo "सभी पैंट करें" (पेंट);
  Override roughness "पेंटिंग ओवरराइड करें"; Add and Join both "जोड़ें"; mask both मास्क and मुखौटा;
  texture spelled two ways.
- id: mask is "Topeng", "Masker" or "Mask" depending on the screen; Relax "Santai", Quads
  "Empat Sisi".
- it: Offset and Displacement both "Spostamento"; Falloff has two translations.
- ja: Surface repeater `Every` and `Spacing` both "間隔"; Golden ratio "黃金比" uses 黃 (黄).
- ko: Tube `Post subdivision` misspelled "포스트 서비디비전".
- ms: "Remes voxel" (Remesh?); vertex both "verteks" and "bucu"; Smooth both Lancar and Licin, Move
  both Alih and Gerak.
- pl: weak fits: Bake "Zastosuj", Depth filter "Maskowanie głębokości", Point light
  "Wielokierunkowe", Lathe Focus "Ostrość", Grain "Tekstura".
- pt: Tiling "Matrização".
- ru: Flatten tool "Свести слои" (flatten layers); typo "Дали базируются на..." (Detail based on);
  odd: "Синхронизация клавиши" (Sync shortcut), "Топология закрепленного" (Connected topology).
- sv: typos "Lagerren filtrering", "Jamförd skala" (Jämförd); odd: "Rymd" (Space), "Slö
  repsstabilisator", "Blomma" (Bloom), "Dämpa ljud" (Denoiser); two words for falloff
  (Avtoning/Avmattning) and remesh (Remesha/Omnäta).
- th: Include actions "ได้แก่ การดำเนินการ" ("namely, actions").
- tr: Debug "Ayıkla", Logs "Kayıtları", wireframe "Genel taslak" (usual: tel kafes), pivot "Eksen"
  (also axis).
- vi: falloff mixed (Giảm dần / độ rơi).
- zh-hans: `material.normal` "法線" uses a traditional character (法线); Delete Layer tool "擦除", the
  same word as Paint's Erase.
