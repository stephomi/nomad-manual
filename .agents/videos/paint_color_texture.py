#!/usr/bin/env python3
"""docs/videos/paint_color_texture.mp4: a polka-dot texture in the Paint menu's color slot, painted on
the elephant's belly. The Dot stroke smears it into streaks; with the Lock + radius stroke type each
drag stamps a clean patch of dots. Post process off (the main checkbox of its menu), as a new user sees
the app. See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    AI_SESSION=<s> paint_color_texture.py setup | AI_SESSION=<s> python3 ../../.agents/ai.py send -
    paint_color_texture.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild.

The texture: the slot's popup lists the textures of the Nomad user folder; the AI session runs on the
sandbox one, so setup writes dots.png into its textures/ folder (ImageMagick) rather than going through
the slot's Import (a native file dialog)."""
import json
import os
import subprocess
import sys

from clip import Clip

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../.agents/ai.py"))
PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/elephant.nom")
# The sandbox user folder. Nomad lists its textures when it starts: if the slot's popup shows no dots
# (the folder gets emptied now and then), run setup once to write the file, restart Nomad, run it again.
TEXTURES = os.path.expanduser("~/Downloads/data_nomad/cache/tmp_session/argB/textures/")
MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]                       # top bar buttons: menus stay open across a project load
SCENE, POST, POST_PANEL, RENDER_RES = 3326, 13905, 13892, 13908
POST_ON = 13907                       # the checkbox of the "Post Process" title
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
PAINT_MENU, PAINT_TOOL, TOOLBOX = 23086, 67749, 58936
DOT, ROLL, LAYOUT = 56388, 56433, 54629           # Dot in the left bar's stroke list; the list/compact toggle
WINDOW = [1200, 900]

PAINT_AT = [875, 25]
SLOT_AT = [1015, 496]                 # the color texture slot
# Its popup (x 666 to 1016, from y 404) since the 2026-11-20 04:32 build. A just started Nomad groups
# the textures by folder (Nomad's own, then the user folder) in a list too short to show both groups;
# flat_textures() makes it one grid: no texture, Nomad's two, dots.png.
DOTS_AT = [953, 499]                  # dots.png, fourth of the grid
SLOT_CLOSE = [997, 420]
SLOT_FOLDERS, SLOT_ALL, SLOT_LIST = 24857, 24856, 24665  # the header's list button: it opens the folder
SLOT_NOMAD = [736, 521]               # list (All, Nomad's, the user's), where the previews are smaller
EMPTY_AT = [828, 510]                 # with the folder list open on All, the first item: no texture
# the presets popup opens over the right of the Paint menu (x 840 to 1190, y 260 to 890) since the
# 2026-11-20 04:32 build; before, it opened on the left of the preview (white at [569, 312]). It is one
# grid too once flat_textures() has run (the grid or groups choice is shared by these popups): white
# is the first of the second row. Grouped (metal, plastic, skin), it is at [902, 484].
PRESET_AT, WHITE_AT, PRESETS_CLOSE = [887, 375], [902, 429], [1171, 275]
LOCK_RADIUS_AT = [25, 310]            # in the left bar's stroke list
START = [1050, 330]                   # resting pointer, background right of the elephant
BODY = [625, 560]                     # on the elephant's body, in the view the project opens with

c = Clip(START, seed=11)
steps = c.steps


def texture():
    os.makedirs(TEXTURES, exist_ok=True)
    tile = ["-size", "128x128", "xc:#f1e4c6", "-fill", "#c8372d", "-draw", "circle 32,32 32,8",
            "-fill", "#2b63b0", "-draw", "circle 96,96 96,72", "-fill", "#e2a92e", "-draw", "circle 96,32 96,12",
            "-fill", "#2f8f55", "-draw", "circle 32,96 32,76"]
    subprocess.run(["magick", *tile, "-write", "mpr:t", "+delete", "-size", "256x256", "tile:mpr:t",
                    "-resize", "512x512", TEXTURES + "dots.png"], check=True)


def prepare():
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    c.tap(BODY); c.wait(90)  # select the body (the project opens with nothing selected), let the flash fade
    for i in MENUS:  # after the selection: with none, some menu buttons are disabled
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": POST})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})  # x1.25 renders banded shadows in a 1200 window
    steps.append({"do": "set", "id": POST_ON, "value": False})  # the whole post process off
    steps.append({"do": "click", "id": POST})
    steps.append({"do": "click", "id": SCENE})
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})


def compact():
    """Whether the Paint tool's stroke types show as one button (compact) rather than as a list: asks the
    running Nomad (AI_SESSION, AI_PY: that session's ai.py). With the project loaded and its body selected,
    as the setup steps will find it: without a selection there is no toolbox."""
    q = [{"do": "window", "size": WINDOW}, {"do": "import", "path": PROJECT, "replace": True},
         {"do": "wait", "frames": 10}, {"do": "drag", "points": [BODY, BODY]}, {"do": "wait", "frames": 10},
         {"do": "scroll", "id": TOOLBOX, "to": 0}, {"do": "set", "id": PAINT_TOOL, "value": True},
         {"do": "find", "text": "Lock + radius"}]
    return "Lock + radius" not in ask(q)


def ask(q):
    return subprocess.run([sys.executable, AI_PY, "send", json.dumps(q)], capture_output=True, text=True).stdout


def flat_textures():
    """Done on the running Nomad, as it takes an answer: the slot emptied and its popup left on All as
    one grid. `All` in the folder list switches between the grid and the groups when it is already
    picked, and comes back to the last of the two from a folder: go through a folder, then look for the
    group titles (buttons that read "/")."""
    press = lambda p: {"do": "drag", "points": [p, p]}
    wait = {"do": "wait", "frames": 8}
    out = ask([{"do": "set", "id": PAINT_MENU, "value": False}, {"do": "set", "id": PAINT_MENU, "value": True}, wait,
               press(SLOT_AT), wait, {"do": "set", "id": SLOT_FOLDERS, "value": True}, wait, press(SLOT_NOMAD), wait,
               {"do": "click", "id": SLOT_ALL}, wait, {"do": "find", "in": SLOT_LIST, "type": "button"}])
    grouped = "button '/'" in out
    ask(([{"do": "click", "id": SLOT_ALL}, wait] if grouped else []) + [
        press(EMPTY_AT), wait, {"do": "set", "id": SLOT_FOLDERS, "value": False}, wait, press(SLOT_CLOSE), wait,
        {"do": "set", "id": PAINT_MENU, "value": False}])


def quick(p):
    """A short press: under recording 8 held frames can count as a long press."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 2)
    c.wait(25)


if sys.argv[1] == "setup":
    texture()
    stroke_compact = compact()  # both on the running Nomad, before the steps below are sent
    flat_textures()
    prepare()
    steps.append({"do": "action", "name": "mask_clear"})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": PAINT_TOOL, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    # the stroke types as a list in the left bar (the two-squares toggle above them; the layout is shared
    # state, so compact() asks Nomad): the radius set from the compact layout, then the list, with Dot
    if not stroke_compact:
        steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "set", "id": RADIUS, "value": 60})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "click", "id": ROLL})  # tapping the active stroke again would open its options
    steps.append({"do": "click", "id": DOT})
    steps.append({"do": "click", "id": PAINT_MENU})    # white plastic: the texture keeps its colors
    c.tap(PRESET_AT); c.wait(10); c.tap(WHITE_AT); c.wait(5); c.tap(PRESETS_CLOSE)
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})
    c.wait(30)
    steps.append({"do": "action", "name": "view_reset"})  # the project's saved view isn't restored on every load
    c.wait(20)
    steps.append({"do": "camera", "orbit": [-15, 20], "frames": 1})  # from above: the belly faces the camera
    steps.append({"do": "camera", "dolly": 0.55, "frames": 1})
    steps.append({"do": "camera", "pan": [0.02, -0.3], "frames": 1})
    c.wait(200)  # the "Reset view" toast fades on wall-clock time
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "paint_color_texture"})
    c.wait(30)
    c.click(PAINT_AT)
    quick(SLOT_AT); c.wait(10)                        # the color texture slot
    quick(DOTS_AT); c.wait(15)
    c.click(SLOT_CLOSE)
    c.click(PAINT_AT)
    a, b = [410, 445], [735, 460]
    c.go(a); c.wait(10)
    c.stroke(a, b, 70, bow=0.05); c.wait(50)          # Dot: the texture smears into streaks
    c.click(LOCK_RADIUS_AT); c.wait(10)               # Lock + radius
    for p, q in (([475, 565], [570, 590]), ([665, 560], [750, 540])):
        c.go(p); c.wait(12)
        c.stroke(p, q, 45, bow=0.0)                   # the drag sets the stamp's size and angle
        c.wait(35)
    c.go(START); c.wait(50)
    steps.append({"do": "record"})
print(c.json())
