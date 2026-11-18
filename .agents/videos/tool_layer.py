#!/usr/bin/env python3
"""docs/videos/tool_layer.mp4: Layer picked in the toolbox; a scribble on a sphere stays at one height,
but a second stroke across it builds on top. A layer added in the Layers menu (the Tool menu then shows
`Use layer data` on): scribble and crossing stroke now share one height. `Sub` digs a groove; a look
around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_layer.py setup | python3 ../../.agents/ai.py send -
    tool_layer.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX, TOOLBOX_SCROLL = 58936, 600
CLAY, LAYER, LAYER_AT = 67742, 67759, [1170, 580]
SYM, RADIUS, INTENSITY, SUB_AT = 56799, 56725, 56745, [25, 477]
LAYERS_AT, ADD_LAYER_AT = [1025, 25], [918, 182]
TOOL_MENU_AT = [775, 25]
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 1.758320689201355]}
WINDOW = [1200, 900]
START = [1010, 640]
REST = [1085, 760]

c = Clip(START)
steps = c.steps


def post_process():
    """A new scene has the post process off: only the render resolution to set."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})


def pick(p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def scribble(way, n):
    """One stroke through the waypoints, eased at both ends."""
    c.go(way[0]); c.wait(10)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(way, min_jerk(i / n))] for i in range(n + 1)]})
    c.pos = list(way[-1])
    c.wait(22)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    post_process()
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": LAYER, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 40})
    steps.append({"do": "set", "id": INTENSITY, "value": 0.3})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Layer itself
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_layer"})
    c.wait(25)
    pick(LAYER_AT)
    # no layer: one stroke caps its height, a new stroke builds on top of it
    # (all strokes start well inside the sphere: off it, a drag turns the camera)
    scribble([[420, 335], [510, 315], [430, 372], [525, 352], [440, 410], [535, 390]], 95)
    scribble([[450, 300], [480, 380], [510, 460]], 50)
    c.click(LAYERS_AT)                       # Layers menu: Add layer
    c.click(ADD_LAYER_AT)
    c.click(LAYERS_AT)
    c.click(TOOL_MENU_AT); c.wait(15)      # Tool menu: Use layer data is on
    c.click(TOOL_MENU_AT)
    # with the layer: everything stays at the layer's height
    scribble([[670, 335], [760, 315], [680, 372], [775, 352], [690, 410], [785, 390]], 95)
    scribble([[700, 300], [730, 380], [760, 460]], 50)
    pick(SUB_AT)                             # Sub (sticky like the toolbox: a short press): a groove
    scribble([[475, 565], [600, 615], [725, 565]], 65)
    pick(SUB_AT)
    c.go(REST); c.wait(10)
    steps.append(dict({"do": "camera"}, **HOME))  # strokes moved the orbit pivot: back to the center
    c.camera(170, yaw=[(0.5, -35), (0.85, -10), (1, -12)], pitch=[(0.45, 18), (1, 8)])
    c.wait(25)
    steps.append({"do": "record"})
print(c.json())
