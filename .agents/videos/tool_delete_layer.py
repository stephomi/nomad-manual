#!/usr/bin/env python3
"""docs/videos/tool_delete_layer.mp4: on the boring head, a layer added in the Layers menu gets a Clay
stroke and a Paint stroke across the forehead; Delete Layer, picked further down the toolbox, then wipes
both away where it passes, the paint too. Post process off and the scene brightened: boringhead.py.
See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_delete_layer.py setup | python3 ../../.agents/ai.py send -
    tool_delete_layer.py record [name] | python3 ../../.agents/ai.py send - 900
Setup asks the running Nomad (AI_SESSION, AI_PY: that session's ai.py) whether Paint shows its stroke
types as a list or as one button (a saved per-tool setting: tool_paint.py switches to the list) and
switches back to the one button this clip was laid out with.
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import json
import os
import subprocess
import sys

from boringhead import PROJECT, look
from clip import Clip

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../.agents/ai.py"))
LAYOUT, STROKES = 54629, 48750        # the two-squares toggle of the left toolbar, and its panel
PAINT_MENU, COLOR_ROW, HEX, PICKER_CLOSE = 23086, 23178, 23366, 23166
PAINT_COLOR = "#e0a820"               # the paint color is shared by the sessions: other clips leave theirs
SHADING, SHADING_PANEL, LIGHT_ICONS = 9959, 9946, 11359
SCENE, SCENE_ICONS = 3326, [4058, 4060]  # mirror and camera gizmos in the viewport
LAYERS, LAYERS_AT, ADD_LAYER_AT = 33760, [1025, 25], [918, 182]
TOOLBOX = 58936
CLAY, PAINT, PAINT_AT = 67742, 67749, [1170, 540]
DEL_LAYER, DEL_LAYER_SCROLL, DEL_LAYER_AT = 67764, 800, [1170, 715]  # after the clip's two scroll drags
SYM = 56799
VIEW = {"pivot": [-0.151, -0.303, 0.202], "rotation": [-0.0721, 0.2876, 0.0519, 0.9536], "translation": [0.15, 0.12, 3.1]}
WINDOW = [1200, 885]                  # what macOS clamped [1200, 900] to when the clip was written
START = [1010, 700]

c = Clip(START)
steps = c.steps


def tool_radius(tool, r, intensity):
    """The sliders by their icon names: a tool whose stroke types show as a list has other, unlabeled ones."""
    steps.append({"do": "set", "id": tool, "value": True})
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": r})
    steps.append({"do": "set", "text": "intensity.png", "type": "slider", "value": intensity})


def compact_layout():
    """Steps that fold Paint's stroke types back into one button, if Nomad shows them as a list (its slider
    column would cover the left of the viewport). Paint ends up the active tool."""
    q = [{"do": "scroll", "id": TOOLBOX, "to": 0}, {"do": "set", "id": PAINT, "value": True},
         {"do": "find", "in": STROKES, "type": "button"}]
    out = subprocess.run([sys.executable, AI_PY, "send", json.dumps(q)], capture_output=True, text=True).stdout
    return [{"do": "click", "id": LAYOUT}] if out.count('icon="shape_') > 1 else []


def paint_color(hex_color):
    """Paint menu > color row > the picker's hex field."""
    steps.append({"do": "set", "id": PAINT_MENU, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": COLOR_ROW})
    c.wait(10)  # the picker's first opening of a session settles over a few frames
    steps.append({"do": "click", "id": HEX})
    c.wait(10)
    steps.append({"do": "type", "input": hex_color})  # no id: the field is already being edited
    steps.append({"do": "click", "text": "Ok"})       # by text: the dialog is built when it first opens
    steps.append({"do": "click", "id": PICKER_CLOSE})
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})


def pick(p, tool):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release, and a recorded press
    lasts longer in wall-clock time when several sessions record at once (Paint wasn't picked in one
    take). Glide onto the button's center, then `set` it there: the click by id lands where the pointer
    already is."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    steps.append({"do": "set", "id": tool, "value": True})
    c.wait(4)   # the frames the held press took
    c.wait(20)


def stroke(way, n, ease=0.15):
    """One stroke through the waypoints (straight segments, slowed by `ease` at each turn, never stopped:
    7 frames within 7 px, at a waypoint or at the end, snap the stroke into a curve when the frames are
    slow, which they are with a painted scene and other sessions recording)."""
    c.go(way[0]); c.wait(10)
    pts = []
    for a, b in zip(way, way[1:]):
        pts += c.path(a, b, n, 0.04, lambda t: (1 - ease) * t + ease * t * t * (3 - 2 * t))[1 if pts else 0:]
    steps.append({"do": "drag", "points": pts})
    c.pos = list(way[-1])
    c.wait(22)


def scroll_toolbox(y0, y1, n=30):
    """A finger drag on the toolbox: it scrolls without picking anything."""
    c.go([1170, y0]); c.wait(6)
    steps.append({"do": "drag", "points": c.path([1170, y0], [1170, y1], n, 0.0, lambda t: t * t * (3 - 2 * t)) + [[1170, y1]] * 4})
    c.pos = [1170, y1]
    c.wait(8)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(30)
    for menu in (LAYERS, 17912, SCENE, SHADING, 6399):  # no menu left open from an earlier take
        steps.append({"do": "set", "id": menu, "value": False})
    steps.extend(look())
    steps.append({"do": "set", "id": SHADING, "value": True})
    c.wait(5)
    steps.append({"do": "scroll", "id": SHADING_PANEL, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": LIGHT_ICONS, "value": False})
    steps.append({"do": "set", "id": SHADING, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": True})
    c.wait(5)
    for i in SCENE_ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": False})
    steps.append(dict({"do": "camera"}, **VIEW))
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "scroll", "id": TOOLBOX, "to": DEL_LAYER_SCROLL})
    c.wait(5)
    tool_radius(DEL_LAYER, 60, 1)
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": PAINT, "value": True})
    steps.extend(compact_layout())
    tool_radius(PAINT, 22, 1)
    paint_color(PAINT_COLOR)
    tool_radius(CLAY, 42, 1)                                 # the clip starts on Clay
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_delete_layer"})
    c.wait(25)
    c.click(LAYERS_AT)                                       # a new layer
    c.click(ADD_LAYER_AT); c.wait(10)
    c.click(LAYERS_AT)
    stroke([[500, 225], [600, 240], [700, 268]], 45)         # Clay on the layer, a broad band
    stroke([[700, 275], [600, 250], [505, 238]], 45)
    pick(PAINT_AT, PAINT)                                    # Paint on the layer
    stroke([[560, 175], [585, 245], [610, 320]], 40)
    stroke([[640, 185], [660, 255], [675, 330]], 40)
    scroll_toolbox(780, 390)                                 # down to Delete Layer
    scroll_toolbox(780, 370)
    pick(DEL_LAYER_AT, DEL_LAYER)
    stroke([[530, 190], [570, 325], [600, 160], [640, 330], [665, 170], [705, 280]], 32, ease=0.4)
    c.go(START); c.wait(50)
    steps.append({"do": "record"})
print(c.json())
