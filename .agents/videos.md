# Videos

Clips in `docs/videos/<name>.mp4` (Git LFS) with a `<name>.webp` poster. The page shows them 360 css
px wide, 240 px min height, so they are 4:3 like the original iPad recordings.

## Recording

Screen recording isn't available to agents: Nomad saves the frames itself. The AI API's `record`
step (`../../.agents/ai-api.md`) writes one PNG per drawn frame; drags and camera moves feed one
event per frame, so the frames play back at 60 fps whatever the capture speed (~15 fps).

- Needs a Nomad build that has `record` (added 2026-11-19); the main `../../build` has it.
- One script per clip in `.agents/videos/<name>.py`: `setup` (load the project, prepare the scene,
  not recorded) and `record` (the clip). Rerun both for a retake: setup reloads from scratch.
  Scripts build their steps with `.agents/videos/clip.py` (`go`, `click`, `stroke`, `camera`), which
  keeps the moves hand-like.
- Window `[1200, 900]` (macOS clamps it to 1200×895), Post Process `Render resolution` x1 (x1.25
  renders banded shadows at that size).
- Post process off (user, 2026-11-20): a clip shows what a new user sees, and the manual projects
  are saved with it on (Dracula's has strong chromatic aberration, boringhead and elephant lighter
  fringes). Turn the whole post process off in setup after loading a project (`set` the main
  `Post Process` checkbox at the top of its panel to false; `toggle_postprocess` only toggles),
  and check a capture. A project lit for tone mapping then looks dark: keep it off and raise the
  exposure in the Shading menu, one value per project for all its clips (Dracula: environment 0.4,
  light 10, in `dracula.py`; boringhead: environment 0.1, in `boringhead.py`; woman, elephant
  and viking need nothing). Only a clip whose subject needs it keeps it, then with SSR, SSGI, SSAO, DOF,
  Dithering and chromatic aberration off: frames don't wait for the accumulation, so these would
  be grainy.
- Move the pointer along paths (`drag` with `hover`), never jump: the brush ring stays where the
  pointer last left the viewport, as on desktop. A jump onto a button leaves it in an odd place. An
  open menu covers it. Symmetry draws its mirrored ring even while the pointer is over the UI.
- The viewer must see what gets clicked. `record` draws a touch marker at the pointer (the OS cursor
  isn't in the frames), with a ring on each press. Glide to a button at a hand's pace (longer moves
  take longer), rest on it ~20 frames, hold the press ~8 frames, then wait ~20 frames for the result
  to show. Don't `click` by id while recording: the pointer would jump to the widget's center.
  `Clip.click()` does all of this.
- Avoid robotic moves, without adding jitter. Pointer moves bow slightly (a wrist moves in arcs),
  start quickly and land slowly, and vary a little in duration (fixed seed: a retake is identical).
  The camera makes one continuous move (`camera` with a per-frame `path`) where orbit, a few degrees
  of tilt, a slight zoom and a drift overlap, rather than separate out-and-back orbits that stop
  dead. `pan` keeps the model centered while it swings (+x moves it left, +y down): check a contact
  sheet of the move that the model stays whole in frame.
- Keep the viewport uncluttered: only what the clip is about, large enough on screen to read the
  change.
- Pitfalls found while recording:
  - Post Process checkboxes low in the panel sit under its quick-jump buttons or the bottom bar,
    so a `set` there clicks whatever covers them (DOF toggled X-Ray once). Scroll the panel so the
    checkbox is well inside it (e.g. `to: 400` for SSGI, SSAO, DOF) and check the result after
    setup.
  - Left toolbar shortcuts (Sub, Unmask...) treat a held press as hold-to-use: `click(p, hold=1)`.
  - Some state survives a project load: the Unmask toggle, panel scroll positions, the current
    tool (`tool_clay` on an active Clay toggles back to the previous tool). Reset what the clip
    relies on in setup.
  - A tool with an extra left slider column shifts the menus right by ~53 px.
  - Long presses run on wall-clock time, and recording slows the frames. Bottom bar buttons with
    options (Wireframe, Grid...) open their popup on the 8-frame press of `click()`: use `hold=2`.
    A stroke whose pointer stays within 7 px for 0.7 s (7 to 10 recorded frames: a turnaround, an
    eased end) snaps into a curve and opens the Stroke snap bar: lift between passes and keep some
    speed at both ends. A long stroke with an eased start stays still long enough to count as a
    long press (Smooth switched to Select for the whole stroke): start at speed (`glide` in
    tool_smooth.py). An unrecorded dry run shows none of these.
  - A stroke that starts just off the model orbits the camera: check start points against the
    silhouette.
  - A top bar button stays lit a moment after its menu closes: end setup with a `wait` of ~90
    frames, or frame 0 (the poster) shows it. Dialog ids change between sessions (built when first
    opened): click their buttons by text.
  - The sub mode (Sub, Fill, Invert...) is kept per tool and survives a new scene: turn it off in
    setup for every tool the clip shows. Files > New and adding a primitive turn `Sym` back on.
  - The toolbox ends at Polish at this window height: scroll it in setup for a lower tool. Its
    scroll shifts while an unvalidated primitive is selected (shorter list); the left toolbar's
    shortcuts don't move.
  - A mouse press moves the orbit pivot: re-send the camera (same view) before a `camera` path, or
    the orbit swings around the last picked point. A new scene's camera is at z 3.359 (tool_drag
    and tool_layer hardcode an older 1.758: fix them at their next retake).
  - Clay on the default 98k sphere leaves saw teeth on diagonal strokes: subdivide once in setup.
  - Pinch barely shows at slider intensity: radius about twice the feature's width, intensity typed
    above 100%, on a raised ridge rather than a rounded rim.
  - Transform with fingers starts once a finger has travelled 16 to 20 px: the object lags by that
    much, and a pinch scales only by the motion after it.
  - Escape doesn't close a top bar menu: click its button again.
  - A paint color without the picker: Paint menu, color row, the `#hex` option, `type` with no id.
  - A painted scene makes ~3 MB frames. Several sessions started together can show a red toast
    (settings write) on launch: check the first frames.
  - The Intensity slider `set` takes a fraction (1 = 100%). Move and Drag strokes follow the
    pointer by the intensity: 100% to keep the surface under it (Move defaults to 50%).
  - The DynTopo shortcut under `Sym` keeps its own on/off state, apart from the menu's `Enabled`,
    and survives Files > New: check it in setup.
  - Lock + radius / Lock + intensity: a drag that eases to a stop snaps like a Dot stroke (keep
    speed to the end). Lock + intensity is 100 px of drag per 100%, uncapped; heights under about
    3x apart look the same at page size, and a height only reads in profile: place the stamps
    where one camera move brings them onto the silhouette. Clay stamps barely show in the Lock
    modes: Brush with the soft `square` alpha, or Paint with its `Falloff` off for patterns.
  - Stroke type radios and dialogs get new ids each session: address them by label, scoped to
    their panel. A bare `click` on the text `Ok` with no dialog open matches `stroke_dot.png`.
    Each Stroke menu tab is its own panel with its own pin.
  - The real mouse moving over the Nomad window moves the brush ring: send a hover on the spot
    just before `record`, and check the first and last frames for a stray ring.
  - A `set` on a disabled top bar button is an error that aborts setup: Topology, Material, Stroke,
    Paint, Symmetry, Layers... are disabled while a camera or a group is selected, or with the
    Gizmo or View tool. Select a mesh and Clay first. Don't chain setup and record in one command:
    a failed setup still gets recorded over.
  - Files > New keeps the previous scene's camera, projection and field of view: set Perspective
    and the FOV in setup. Pinned panels survive scene loads: unpin in setup and afterwards. A
    slider drag that starts left of a pinned panel orbits the camera.
  - The pimples of tips.md only show on a glossy material (roughness 25 %, metalness 100 %, smooth
    shading) with Smooth typed far above its slider range.
  - A reference image: the PNG must be in the sandbox backgrounds folder when Nomad starts (see
    audit.md); choosing it through `Import...` can't be recorded.
  - Several Nomads recording at once slow the capture (load average 20 to 45 with four), and the
    wall-clock traps then fire on takes that used to pass: a 4-frame press on a toolbox button
    borrows the tool (use 2), an eased stroke end snaps into a curve.
  - Preset and texture popups: their `All` tab has two states (grouped by folder on a fresh Nomad,
    or one grid; clicking `All` again toggles, and the state is shared by both popups), so item
    positions depend on it. A drag inside a popup's list moves the popup for the session. A
    preset tapped without a hover move afterwards leaves the model previewed in that material.
    User textures are listed when Nomad starts (`dots.png` in the sandbox `textures/` first).
  - A Scene list row picks itself up on a held press and drops into the row above as its child:
    `hold=2`. A hidden object that is still selected is drawn as a dither over what is in front.
    A new scene's sphere has radius 0.4198, a Quad Sphere from Scene > Add 0.5. The light settings
    popup opens from the `...` of the light row in Shading (ids change per load).
  - Wireframe roughly doubles the file size: a 6k sphere or a 32-division box is about the
    density that still reads at page size.
  - macOS doesn't clamp the `[1200, 900]` window the same way all day (885, 895, 900 and 917 were
    seen), which shifts the bottom bar, popups and viewport-centred points by a few pixels, enough
    to miss a gizmo arrow. Check the `capture` size after setup; `[1200, 885]` gives the 2400×1770
    frames of the first clips. Clips are 1440×1062 or 1440×1080 depending on the day's clamp.
  - A slider's value box opens centred the first time in a session, then next to its slider: open
    and cancel it once in setup. A layer factor slider covers 100 % over its own width: keep the
    drag inside the panel. A large tool ring parks where the pointer left the viewport: leave over
    the background.
- A menu can stay open while you sculpt (the pin in its panel header). When a clip goes back and
  forth between a menu and the viewport, pinning it is an option instead of closing and reopening
  it each time; choose whichever reads more clearly.

## Encoding

```sh
ffmpeg -framerate 60 -i frames/<name>/%05d.png -vf scale=1440:-2:flags=lanczos \
  -c:v libx264 -preset slow -crf 24 -pix_fmt yuv420p -movflags +faststart -an docs/videos/<name>.mp4
```

Poster: the first frame scaled to 720 px wide, through `.agents/webp.py`. Replace both in place
under the same names: no page edit needed.

Frames are ~1.5 MB each (a 25 s clip is ~2 GB): check a contact sheet, encode, then delete the take's
frame folder and any failed takes. Several agents can record at once, each with its own
`AI_SESSION=<name>` on every `ai.py` call.

## Status

Redone (2026-11-19, retaken 2026-11-20 with the cursor, slower clicks, hand-like moves):
multiresolution (test of the workflow).

Audited 2026-11-20 (contact sheets against the current UI) and re-recorded the same day, one script
each in `.agents/videos/` (`.agents/scenes/stone_tiles.py` builds the depth-filter plane). Some
scripts rely on UI state an earlier setup left (stroke types shown as a list, Connected topology),
or query the running Nomad (trim, split, project, gizmo: set `AI_SESSION`): check a retake's first
frames. Redone, outdated UI:
- tools: tool_move, tool_drag, tool_flatten, tool_stamp, tool_layer, tool_delete_layer, tool_mask1,
  tool_mask2, tool_selector_mask, tool_paint, tool_smudge, tool_trim, tool_split, tool_project,
  tool_tube, tool_lathe, tool_gizmo
- topology, scene, material, tips: decimate, dynamic, hole_filling, unwrap, voxel_remesher,
  merge_separate, triplanar, refraction, tip_pimples_reproject
- layers, painting, stroke: layer, layer_happysad, layer_shell, layers_details, paint_color_texture,
  connected_topology, filter_keep_sharp_edges, stroke_depth_bump, stroke_depth_cavity,
  stroke_randomize
- gettingstarted_01 to 11, redone as one set with finger input (`touch`), all from
  `.agents/videos/gettingstarted.py`: setup replays the earlier clips, so any clip retakes alone.
  Touch pitfalls: a pinch needs its midpoint to drift a little or it doesn't zoom; two fingers held
  still 500 ms start the history scrub (start moving at once); a two-finger tap must last under
  230 ms (2 frames); toasts fade on wall-clock time (wait unrecorded before `record`).

- the remaining tool clips, redone later the same day (user request: all the tool clips match):
  tool_clay, tool_brush, tool_smooth, tool_crease, tool_pinch, tool_inflate, tool_nudge,
  tool_planar on a fresh-scene sphere; tool_insert and tool_transform on the terrain built by
  `.agents/videos/terrain.py` (both have a `dry` mode: the same steps unrecorded, with captures).
  tool_transform uses finger input; `touch` presses both fingers together, so the page's "hold one
  finger, add a second" gestures aren't shown.

- the last old clips, same day (they still showed the old menus): stroke_dot, stroke_roll,
  stroke_lock_radius, stroke_lock_intensity, alpha_tiling (helpers in `stroke_modes.py`, with a
  `restore` of the shared stroke settings); stroke_drag, stroke_grab, stroke_lockradius_drag,
  stroke_lazy_rope, stroke_silhouette (`stroke_common.py`, same); layer_leftright, symmetry_demo,
  tip_pimples_before, tip_pimples_stable_smooth, reference_camera.

- post process off, same day: the 21 clips recorded on a manual project were retaken with it off
  (see Recording), layer_leftright with them. tip_pimples_reproject was rebuilt on the metal
  sphere of `tip_pimples.py`, like the two clips before it on the page.

Every Nomad clip is now scripted. Not Nomad, kept: blender_pbr. Deleted 2026-11-20, used by no page: merge_add, merge_inter, merge_sub,
stroke_tile, stroke_type, symmetry.
