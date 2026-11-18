# Page audit (started 2026-11-19)

Every English page checked against the current app: text updated (options added, removed, renamed),
images retaken when they show old UI. English only; translations follow in the next full sync.

Snapshots of each menu (option list with help texts, stitched capture) are made with
`.agents/snapshot.py` into a scratch folder; agents update the text from them.

| Page | Menu | Text | Images |
| :--- | :--- | :--- | :--- |
| index | - | done (no change) | - |
| gettingstarted | - | done | kept: head1/2 renders |
| files | Files (Files, Render, Link) | done | done (file_preset_preview unchecked) |
| scene | Scene, Add, Primitive, repeaters | done | done, except boolean_* and the toolbar gif |
| topology | Topology (9 tabs) | done | done |
| material | Material | done | done |
| shading | Shading | done | done |
| postprocess | PostProcess | done | done (postprocess_overview kept) |
| background | Background | done | done, except background_reference |
| camera | Camera | done | done |
| stroke | Stroke (Stroke, Alpha, Falloff, Filter) | done | done |
| pressure | Stroke > Pressure | done | done |
| painting | Paint | done | done |
| symmetry | Symmetry | done | done |
| layers | Layers | done | done |
| settings | Settings | done | done |
| interface | Interface (Gesture, Bindings, Debug left) | done | done, except shortcuts (iOS) |
| tools | toolbox, each tool's settings | done | done, except Quad Remesher (paid) |
| history | History | done | done |
| faq | - | done | - |
| tips | - | done | kept: tips_lighting_* renders |

Videos were not audited; known outdated: tool_selector_mask (removed tool), tip_pimples_reproject
(old menu location), the Getting Started clips (old UI).

## Images flagged as outdated

- scene: scene_repeater_combine (old tree rows, old Curve toolbar), scene_primitive_array (old
  toolbar), scene_primitive_toolbar.gif (old primitive toolbar, animated), boolean_union /
  boolean_subtract / boolean_intersect (old tree rows, minor).
- interface: interface_gesture_matrix (5 rows, now 14; air stroke now its own section),
  interface_gesture_mask (old Shortcut Mask/SelMask radio), interface_gesture_togglemask (now
  Long press - Sculpt / Toggle), interface_gesture_threefingers (Off is now No, minor),
  interface_bindings (4 tabs, old header), interface_bindings_advanced (old options),
  shortcuts (⌘ overlay over a very old UI; iOS only, hard to retake on desktop).
- shading: shading_extra_controls (old light editor), shading_lights_toolbar (likely, Spot toolbar).
- postprocess: postprocess_quality (old Full Resolution), postprocess_overview (minor, old chrome).
- painting: paint_intensity, paint_material, paint_presets, paint_sliders (minor);
  paint_triplanar_settings unverified.
- layers: layers_overview, layers_menu (minor), layers_more, layers_advanced, layers_expand,
  layers_preview, layers_thickness, layers_smoothness, layers_edgeloop. Needs a mesh with layers.
- background: background_selector (old radio style), background_reference (no Post process).
- material: material_triplanar (label now `Uniform (hardness)`).
- camera: camera_list (old look, content same); camera_rotation_ortho_view sits under First Person.
- files: file_preset_preview (preset browser now Open/Add + Poly Haven, unconfirmed).
- stroke: stroke_radius, stroke_randomize, stroke_alpha, falloff_menu, filter_menu,
  filter_protect_area, stroke_depthmask; minor: alpha_scaling, alpha_scaling_y, stroke_tiling.
- pressure: pressure_menu.
- symmetry: symmetry_mirroring, symmetry_edit.
- settings: settings_display_settings, settings_indicator, settings_wireframe (unverified),
  settings_grid, settings_snapcube.
- tools: tools_menu (old toolbox), tool_left_panel, tools_settings_menu, tool_smooth_settings,
  tool_mask_toolbar, tool_mask_settings, tool_gizmo_settings, tool_quadremesher,
  tool_quadremesher_toolbar; video tool_selector_mask (SelMask tool removed, merged into Mask).
  Not judged: tool_gizmo (diagram), tool_tube_new, tool_tube_toolbar, tool_lathe_top_toolbar.
- gettingstarted: gettingstarted_head1/2 (old UI around the sculpt, low priority).
- tips: tips_lighting_* (old 1.85 UI around valid renders); video tip_pimples_reproject (old
  Misc → Reproject location).

Batch 1 retaken (2026-11-19): all layers, paint, shading, postprocess_quality, background_selector,
material_triplanar, camera_list. Skipped: background_reference (setting a reference image needs
the native file dialog; `import` of a PNG doesn't set it).

Batch 2 retaken (2026-11-19): stroke, pressure, symmetry, settings, tools (except Quad Remesher),
interface gesture/bindings, scene_primitive_array, scene_repeater_combine. Skipped:
tool_quadremesher and tool_quadremesher_toolbar (Quad Remesher is a paid add-on, the sandbox shows
a purchase cart), boolean_union/subtract/intersect (before/after renders, minor), shortcuts (iOS),
scene_primitive_toolbar.gif (animated), gettingstarted_head1/2 and tips_lighting_* (keep).
falloff_menu shows the dev-only `Shift` slider (ai= sessions run in dev mode).

## Follow-ups

- scene.md Curve repeater text: toolbar now has Show, Sym, Warp, Pivot, Rotate, Alternate, Spiral,
  Randomize (see scene_primitive_curve).
- topology.md was restructured to follow the tabs (Decimate, Quad Remesh, UV Unwrap, Bake are `##`
  sections now): the translation sync has to restructure the locale pages the same way.
- topology.md: old gear-menu anchors now sit on short "Options" headings; `Thicken thin parts` and
  Quad Remesher gear options described from code or listed by name only.
- stroke.md: falloff `Shift` slider left out (dev-only in source); `Lock + radius` got a new anchor
  `{#lock-radius}`. pressure.md: "Allow unrecognized pressure" is gone, its anchor moved to
  `Limit pressure at 100%`. settings.md: roll hint wording and cursor color meanings inferred.
- Icons refreshed (2026-11-19) from ../nomad/tools/icons: SVGs rasterized by Inkscape at 64px
  (tool_gizmo 128px), painted tool PNGs shaved 7% per side like conv-icons.py and resized to 128px,
  painted PNG wins over an SVG of the same name. Colored ones are in the `colored` list of
  config.mts. 285 unused icons deleted; tool_maskSelector kept (removed tool, no master).
- Quad Remesher retaken on boringhead.nom: in an ai= session, the cart button's `Unlock (purchase,
  restore, trial)` runs a dummy remesh that unlocks it when this Mac has an Exoside license.
- background_reference retaken: `dragon_reference.nom` (user's, manual folder) holds the reference
  settings but not the image, only its name `IMG_3307.png`. Copy the dragon render there first:
  `~/Downloads/data_nomad/cache/tmp_session/argB/backgrounds/IMG_3307.png` (the ai= sandbox user
  folder), start Nomad, open the .nom, import dragon.nom with `"replace": false`, select the dragon
  group, then Background panel scrolled to the bottom; crop 2300x1490+120+190.
- The sandbox settings now hide viewport icons (Scene panel: light/camera/repeater filters off,
  Advanced > Icons `Opacity` 0). Turn them back on for a shot that should show them.
- tools.md: Clay has no settings panel (the snapshot showed Move's); SelMask merged into Mask;
  Polish, Elastic, Arrange, Lattice descriptions partly from source; Quad Remesher `Reset` sub mode
  and the Clone/Instance "Repeater" relabel left out; Tube/Lathe top toolbars not audited.
- Run a cross-page link check at the end (several pages linked to anchors that didn't exist).
- interface.md: left out dev-only Debug options (UI Picking, Simulate trial, Show icons); Gesture
  "Node editing" and "On tap" described from source; Tool Radius drag modes not explained.
- gettingstarted.md lists `Logs` as a default bottom bar button (GuiQuick.cpp makes it default with
  no dev condition): ask the user whether release builds show it.
- transform.md and operation.md added (2026-11-19), from GuiTransform.cpp / GuiOperation.cpp and
  their strings. From code, not seen in use: the Pivot bake (SceneBaker BAKE_PIVOT), the Offset
  layer filter (Operation.cpp bRelayer), when the Skew row and the Local/World selector show.
  Not translated yet: locale sidebars link to the English pages until the sync pass.
- pressure.md deleted (2026-11-19, user request): a short duplicate of stroke.md#pressure. The home
  page rows of every locale point to stroke.md#pressure.
- Images not retaken earlier, done 2026-11-19: file_preset_preview (crop of the preset popup),
  boolean_union/subtract/intersect (box + low-poly sphere, Object ID shading, wireframe; tree rows +
  before + after), scene_primitive_toolbar.webp (still of the Box toolbar, replaces the gif in
  English; scene.md toolbar text updated), postprocess_overview (viking, toggle_postprocess off/on),
  gettingstarted_head1/2 (the sculpts cropped out of the old UI), tips_lighting_* (rebuilt on the
  elephant in a new scene: default env, tone mapping 1.5, env 0.25/330, directional light 1.8, head
  and body Opaque -> Subsurface + spot 20 behind the ears, final = tone/SSAO/curvature/bloom/vignette;
  SSGI left out, it stays grainy with this lighting). Only `shortcuts` (iPadOS ⌘ overlay) is left:
  it needs a real iPad.
- tools.md tool families follow Tool::linearColor; style.css has dark and light variants.
- Heading icons (2026-11-19): ~230 headings got the icon the app shows for that element (button,
  tab, section title, preIcon), mapped from src/gui; `.agents/icons.py` renders masters. Left out:
  icons drawn after a label (postIcon), runtime icons (current tool, generated cut icons), option
  rows without one icon. Stroke menu icon is `brush` (was pencil); scene "Add view" is now `Camera`.
  The locales get the icons at the translation sync.
- faq.md rigging answer could mention the face group Pose tap action.
- files.md: USD `Instance`/`Repeater` and Live sync `Working view` inferred from code.
- camera.md: `Center view when zooming out` described from a code comment.
- painting.md: triplanar `Vertex` button described from Paint.cpp.
- shading.md: light toolbar bullets from GuiLight::getWidgets, unverified on screen.
- scene.md: `Thicken thin parts` described from code (no help string); Delete keeps children
  (from Node::pop()).
