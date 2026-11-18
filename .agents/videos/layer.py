#!/usr/bin/env python3
"""docs/videos/layer.mp4: paint layers on the woman bust. A yellow stroke on a new layer, a second
layer with a blue stroke across it (on top), then the yellow layer is dragged above the blue one and
its strength slider lowered: layers combine like in a 2d paint app. Post process off (the main checkbox
of its menu), as a new user sees the app. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    layer.py setup | python3 ../../.agents/ai.py send -
    layer.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. Layer rows get new ids
when they are created, so the clip works by position."""
import os
import sys

from clip import Clip

PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/woman.nom")
MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]                       # top bar buttons: menus stay open across a project load
SCENE, POST, POST_PANEL, RENDER_RES = 3326, 13905, 13892, 13908
POST_ON = 13907                       # the checkbox of the "Post Process" title
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
LAYERS, LAYERS_PIN = 33760, 33753
PAINT_TOOL, TOOLBOX = 67749, 58936
WINDOW = [1200, 900]

LAYERS_AT = [1025, 25]
PAINT_AT = [875, 25]                  # Paint menu (material)
ADD_AT = [918, 182]                   # Add layer
PRESET_AT = [887, 375]                # the material preview: opens the presets
# the presets popup opens over the right of the Paint menu (x 840 to 1190, y 260 to 890) since the
# 2026-11-20 04:32 build; before, it opened on the left of the preview (blue at [646, 312]). Positions
# for the presets in groups (metal, plastic, skin), as a just started Nomad shows them: the popup's `All`
# can also show one grid, a choice shared with the texture popup (paint_color_texture.py sets the grid)
BLUE_AT = [977, 484]                  # plastic blue preset
YELLOW_AT = [1127, 559]               # plastic yellow preset
PAINT_MENU = 23086
PRESETS_CLOSE = [1171, 275]
TOP_NAME = [1025, 252]                # with two layers, the compact (inactive) row on top...
LOW_NAME = [1025, 372]                # ...or below the active one
TOP_SLIDER = [930, 252]               # the compact row's strength (relative: drag left to lower)
START = [700, 790]                    # resting pointer, background below the right shoulder

YELLOW = [([330, 600], [620, 640])]   # a stroke across the chest
BLUE = [([470, 520], [445, 770])]     # crossing it

c = Clip(START, seed=5)
steps = c.steps


def prepare():
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    steps.append({"do": "click", "id": POST})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})  # x1.25 renders banded shadows in a 1200 window
    steps.append({"do": "set", "id": POST_ON, "value": False})  # the whole post process off
    steps.append({"do": "click", "id": POST})
    steps.append({"do": "click", "id": SCENE})
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": SYM, "value": False})


def paint(strokes):
    for a, b in strokes:
        c.go(a); c.wait(8)
        c.stroke(a, b, 70, bow=0.08)
    c.wait(20)


def quick(p):
    """A short press: recording slows the frames down, and 8 frames held on the material preview or a
    preset count as a long press (wall-clock), which doesn't open or pick it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 2)
    c.wait(25)


def reorder(a, b):
    """Press and hold a layer's name, then drag it to b."""
    c.go(a); c.wait(15)
    hold = [list(a)] * 40  # the hold picks the row up: one press for the hold, the move and the drop
    move = c.path(a, b, 40, 0.0, lambda t: t * t * (3 - 2 * t))
    steps.append({"do": "drag", "points": hold + move + [list(b)] * 8})
    c.pos = list(b)
    c.wait(30)


if sys.argv[1] == "setup":
    prepare()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": PAINT_TOOL, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 30})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "set", "id": LAYERS_PIN, "value": False})
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "click", "id": PAINT_MENU})  # the tool material is global: start from yellow
    c.tap(PRESET_AT); c.wait(10); c.tap(YELLOW_AT); c.wait(5); c.tap(PRESETS_CLOSE)
    steps.append({"do": "click", "id": PAINT_MENU})
    steps.append({"do": "camera", "pivot": [0.2574, -0.381, -0.5194], "translation": [0.9029, 0.258, 12.8988],
                  "rotation": [-0.02603, -0.10449, 0.00274, 0.99418]})  # the bust on the left of the menus
    c.wait(20)
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "layer"})
    c.wait(40)
    c.click(LAYERS_AT); c.click(ADD_AT)            # Layer: the first one
    c.click(LAYERS_AT)
    paint(YELLOW)
    c.click(LAYERS_AT); c.click(ADD_AT); c.wait(10)  # Layer 1, on top
    c.click(PAINT_AT); quick(PRESET_AT); quick(BLUE_AT); c.click(PRESETS_CLOSE)
    c.click(PAINT_AT)
    paint(BLUE)                                    # blue goes over yellow
    c.click(LAYERS_AT)
    reorder(LOW_NAME, TOP_NAME)                    # yellow layer on top: it covers the blue
    c.go(TOP_SLIDER); c.wait(15)
    c.stroke(TOP_SLIDER, [TOP_SLIDER[0] - 60, TOP_SLIDER[1]], 50, bow=0.0)  # lower it: the blue shows through
    c.wait(60)
    c.click(LAYERS_AT)
    c.go(START); c.wait(30)
    steps.append({"do": "record"})
print(c.json())
