#!/usr/bin/env python3
"""docs/videos/filter_keep_sharp_edges.mp4: a red stroke along an edge of a flat-faced icosahedron spills
onto the next face; undo, Filter > Falloff Normal Filter (Min 60, Max 80), the same stroke stays on the
face under the brush. See .agents/videos.md for the workflow.

The page shows this clip under Area Normal Filter, but for painting that filter changes nothing visible:
it only weights the points of the area plane (Picking.cpp). The Falloff Normal Filter is the one that
cuts the brush falloff at the edge (Falloff.hpp).

Prints the JSON steps for `ai.py send -`:
    filter_keep_sharp_edges.py setup | python3 ../nomad/.agents/ai.py send -
    filter_keep_sharp_edges.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. The setup expects the
left bar's stroke types shown as a list (as paint_color_texture.py leaves them)."""
import sys

from clip import Clip

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
MENUS = [108, 3326, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331, 27845]
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
PAINT_MENU, PAINT_TOOL, TOOLBOX = 23086, 67749, 58936
DOT, ROLL, LAYOUT = 56388, 56433, 54629
FILTER_PANEL, AREA_NORMAL = 21752, 22019
FALLOFF_NORMAL, FMIN, FMAX = 22075, 22091, 22111
WINDOW = [1200, 900]

PRESET_AT, RED_AT, PRESETS_CLOSE = [887, 375], [646, 390], [838, 100]
SLOT_AT, EMPTY_AT, SLOT_CLOSE = [1015, 496], [729, 459], [996, 354]
STROKE_MENU_AT = [825, 25]            # the top bar's stroke menu, opens on its Filter tab
FALLOFF_NORMAL_AT = [1100, 705]       # Falloff Normal Filter's checkbox, panel scrolled down
UNDO_AT = [25, 858]
START = [1000, 700]
EDGE = ([385, 393], [630, 410])       # on the light top face, just above its edge with the face below

c = Clip(START, seed=17)
steps = c.steps


def post_process():
    """A new scene has the post process off: only the render resolution to set."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})


def paint():
    a, b = EDGE
    c.go(a); c.wait(12)
    c.stroke(a, b, 70, bow=0.02)
    c.wait(50)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    for i in MENUS:  # with the new sphere selected: with nothing, some menu buttons are disabled
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "action", "name": "delete"})
    steps.append({"do": "action", "name": "add_icosahedron"})  # a subdivided one: flat faces, 2562 vertices
    c.wait(5)
    steps.append({"do": "click", "text": "Validate", "type": "button"})
    steps.append({"do": "set", "id": SYM, "value": False})  # a new primitive turns symmetry back on
    post_process()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": PAINT_TOOL, "value": True})
    steps.append({"do": "click", "id": ROLL})  # tapping the active stroke again would open its options
    steps.append({"do": "click", "id": DOT})
    steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "set", "id": RADIUS, "value": 55})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "click", "id": PAINT_MENU})  # red, no texture
    c.tap(PRESET_AT); c.wait(10); c.tap(RED_AT); c.wait(5); c.tap(PRESETS_CLOSE)
    c.tap(SLOT_AT); c.wait(10); c.tap(EMPTY_AT); c.wait(5); c.tap(SLOT_CLOSE)
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})
    steps.append({"do": "action", "name": "menu_filter"})
    steps.append({"do": "scroll", "id": FILTER_PANEL, "to": 300})
    steps.append({"do": "set", "id": AREA_NORMAL, "value": False})
    steps.append({"do": "set", "id": FALLOFF_NORMAL, "value": True})   # the angles show once it's on
    # the angles are a threshold on the normal's dot product, shown as asin: 60..80 fades out points
    # turned 10..30 degrees away from the area normal (an icosahedron's faces are 41.8 degrees apart)
    steps.append({"do": "set", "id": FMIN, "value": 60})
    steps.append({"do": "set", "id": FMAX, "value": 80})
    steps.append({"do": "set", "id": FALLOFF_NORMAL, "value": False})
    steps.append({"do": "scroll", "id": FILTER_PANEL, "to": 300})     # clamped: the normal filters in view
    steps.append({"do": "action", "name": "menu_filter"})
    steps.append({"do": "camera", "orbit": [5, -35], "frames": 1})  # neighbor faces shaded apart
    steps.append({"do": "camera", "dolly": 1.25, "frames": 1})
    steps.append({"do": "camera", "pan": [0.12, 0], "frames": 1})
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(30)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "filter_keep_sharp_edges"})
    c.wait(40)
    paint()                            # spills over the edge
    c.click(UNDO_AT); c.wait(15)
    c.click(STROKE_MENU_AT)
    c.click(FALLOFF_NORMAL_AT); c.wait(50)  # Falloff Normal Filter, with its Min/Max angles
    c.click(STROKE_MENU_AT)
    paint()                            # stays on the face
    c.go(START); c.wait(10)
    c.camera(180, yaw=[(0.5, -25), (1, -18)], pitch=[(0.5, 8), (1, 5)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
