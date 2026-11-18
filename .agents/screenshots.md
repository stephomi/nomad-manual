# Screenshot redo

Tracking the screenshots in `docs/images` to retake at 2x. Check items off as they land; remove the
file once every list is done.

## How to retake

- Start Nomad: `python3 ../nomad/.agents/ai.py start`, then `{"do":"window","size":[1440,900]}`.
  The `ai=` option only works for a binary under `../nomad/build*` (dev mode check).
- Load a project from `~/Downloads/data_nomad/cache/projects/manual/` with an `import` step,
  `"replace": true`. To sculpt, select a mesh first: the dragon project opens with a group selected,
  and a drag then orbits the camera. The default sphere (Files > New, confirm `Yes`) sculpts at once.
- `python3 .agents/shot.py <name> --panel <title>` writes `docs/images/<name>.webp` at 2x. A panel
  taller than the window is scrolled and stitched. `--full --highlight <title>` makes a page
  overview: a wide yellow halo around that panel, matching the original manual's overviews.
- `python3 .agents/overviews.py [name ...]` retakes the 14 page overviews in one go (fresh session).
- A panel's title can change with its tab (History panel, Settings tab: the panel is "Settings").

## Done

Overviews and 1x panels from the first pass are all retaken (2x, current UI), plus grading_off/on
and pixel_off/on (woman project). Annotated images were redrawn with ImageMagick in the Nomad accent
`#ebbe6c`: interface_overview1, topology_primitive_screenshot, symmetry_button,
tools_shape_selector_panel.

ssgi_off/on: the user's scene `ssgi_room.nom` in the manual projects folder (built from
`.agents/scenes/ssgi_room.py`), captured with its own camera and lighting: load it, set Max frame
sampling to 200, park the pointer, `--rect 430,130,640,615`, toggle the SSGI checkbox.

All overviews and the grading/pixel pairs were retaken on 2026-11-19 with accumulated renders
(`capture` now waits for the post-process samples) at Max frame sampling 200. The 14 page overviews,
Shading, Camera and Background included, share one style: the old manual's wide yellow halo, no
dimming. Each one has a scene that fits its page (user request, 2026-11-19: not the same dragon
everywhere): a fresh zigzag stroke for Stroke, a mirrored stroke with the symmetry line for
Symmetry, the painted bust for Paint, wireframe for Topology and Settings, the reference image for
Background, a selected gold ring for Material... Scene, setup and teardown of each overview are in
`.agents/overviews.py`. The SSGI room is too grainy for a full-window overview.

Never the default sphere (Files > New), and not the dragon everywhere: spread the manual projects
across images. `.agents/extras.py` retakes the non-overview shots that show a model: Layers crops
(boring head, which has smile/detail/pink paint layers), History list (elephant strokes), and the
annotated images (interface_overview1 on the viking, tool_left_panel on Dracula,
tools_settings_menu on the viking, symmetry_button on the woman).

The 26 soft ~500px panels (topology_*, file_*, material_*, scene_boolean_menu,
scene_primitive_curve, interface_bindings_context, interface_bottom_toolbar) were retaken at 2x on
2026-11-19. Topology and Files images are cut from stitched panel captures at their divider lines;
material_textures and material_texture_panel use `.agents/scenes/textured_sphere.py`.

A sharpness check (detail lost when an image is halved) found no other soft UI image: the remaining
low scores are images with large flat areas, sharp at 1:1. Images whose UI is outdated but sharp
are not tracked yet: a per-page audit against the app is the next step.

Material spheres (dielectric_*, metal_*) are 512x512 renders, fine as they are.

## Text out of date with the UI

Updated (English and all locales): the points below. Interface sub-images interface_menu,
interface_shortcuts, interface_add_shortcuts_window, interface_toolbox and interface_transparent were
retaken for it. Still to check against the app: the Gesture, Bindings and Debug tabs of interface.md,
the Path flyout of the Tube and Lathe toolbars, and the Radial repeater's new Warp, Alternate and
Randomize buttons.

Not updated yet (seen in the 2026-11-19 retakes):
- topology.md: Voxel has Thicken thin parts, Holes (Fill/Shape), Sharp edges/Sharp border/Keep
  groups; DynTopo detail options changed; Misc is Holes (with Face Group Mixed/New/Reuse, Detail,
  Bridge), Force Manifold (Delete small faces), Triplanar; Decimate has Preserve boundary (Hole,
  Face Group, UV); Quad Remesh lists Quad Remesher, AutoRemesher, Instant Mesh, QuadriFlow; UV Unwrap
  has UVAtlas and BFF with Inspect; Bake has Bake → Texture (8k, Displacement), Reproject → Vertex,
  Bake → VDM; the bake gear popup has Use multires, Smooth base, Search distance, Projection.
- files.md: Files tab has Scope (Internal/In Place), Overwrite; Export lists NOMAD/glTF/OBJ/FBX/PLY/
  STL/USD with Include, One file per object, Embed history/assets; Render has Heightmap, Focus.
- material.md: types Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.
- interface.md: a binding's context menu has Sticky keys (Auto/Hold/Toggle/Quick Press) and Hold
  Revert, replacing "Toggle shortcut on key tap".
- scene.md: Boolean popup adds Thicken thin parts, Holes, Sharp edges/border, Keep groups separate.

- history.md: the Settings tab now has Restore camera, Save history, RAM limit, Storage limit and
  Undo warning; the "Include actions" toggles moved to icons at the bottom of the History tab.
- interface.md: the menu has Interface, Shortcuts, Gesture, Bindings and Debug tabs; Interface has
  Appearance and Layout sub-tabs, colors are a "Colors" grid with Accent, Base, Text opacity, Toggles,
  Checkbox, Tabs. Debug has its own sub-tabs (UV, Shading, FPS, Turntable, Interface...).
- scene.md: Add menu top row is On gizmo, Select gizmo, Advanced; UVs moved next to Primitive; new
  Text, VDM, Shadow Catcher primitives, Surface repeater, Environment light.
- topology.md: the tabs are two rows (adds Decimate, Quad Remesh, UV Unwrap, Bake); the toolbar's
  "…" popup no longer shows the Topology section.
- tools.md: shape choices (Lasso, Polygon, Line, Band, Rect, Ellipse) are a popup from the left
  toolbar, with stroke types (Dot, Smooth, Smudge, Roll, Lock…); Tube and Lathe curve options moved
  into a Curve popup (Edit: Hold, Closed, Keep drawing, Accuracy), Snap has an Offset button.

## Capture tips

- Set PostProcess `Max frame sampling` to 200 after loading a project: `capture` waits for all the
  samples, and 200 is clean.
- Park the pointer outside the window before capturing (`{"do":"drag","points":[[1300,880],
  [1600,1100]],"hover":true}`): the brush ring stays wherever the pointer last was in the viewport.
- Make Clay active with `set` on the toolbox Clay button (`value: true`), not the `tool_clay`
  action: the action toggles back to the previous tool when Clay is already active.
- Close each menu after its shot and check no titled panel is left (`find` `type: panel`): a left
  menu stays open behind a right one. Toggling Topology after switching its tab can reopen it on Misc.
- Scroll a panel to the top (`scroll` `to: 0`) before an overview: panels keep their scroll.
- A menu action can switch the menu's tab instead of closing it (`menu_topology` flips Misc and
  Multires), and escape closes no menu: click the active top bar button (y 0, value true) instead.
- Never click a button that opens a native file dialog (an empty Material texture slot, Open,
  Import...): it blocks Nomad and the API until the session is killed. Bring files in with the
  `import` step instead (a glTF carries its textures).
- Saving a project writes to the sandbox (`data_nomad/cache/tmp_session/argB/`), not the user's
  projects: fine to do, it gives the Files panel a thumbnail.

- A loaded project restores its saved tool (often Transform) a few frames after `import`: send
  `tool_clay` again just before capturing, or the Transform gizmo and toolbar show up.
- Post-process quick buttons at the panel bottom only jump to a section; the section's header
  checkbox turns the effect on.
- `"in": "<title>"` fails when a tab shares the panel title (Files): use the panel id.
- The Mask toolbox context menu doesn't close with escape; tap empty viewport space.
