#!/usr/bin/env python3
"""docs/videos/layer_leftright.mp4: the boring head's smile is a layer (renamed "left" by setup), the
Layers menu is pinned open and DelLayer is the tool, symmetry off. The clip clones the layer (the smile
doubles), rubs the right half out of one copy, selects the other, renames it "right" and rubs its left
half out; then each layer's factor dragged to zero and back drops one side of the smile.
Post process off and the scene brightened: boringhead.py. The whole face sits left of the panel, and the
tool's ring is kept off it (see START). See .agents/videos.md for the workflow.

    layer_leftright.py setup | python3 ../nomad/.agents/ai.py send -
    layer_leftright.py record [name] | python3 ../nomad/.agents/ai.py send - 900
    layer_leftright.py restore | python3 ../nomad/.agents/ai.py send -
`restore` unpins and closes the Layers menu (the pin outlives the scene). `record dry` runs the same
steps unrecorded. Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. The
layer rows get new ids on each load, so the clip clicks them by position."""
import sys

from boringhead import PROJECT, look
from clip import Clip, min_jerk

# top bar buttons, Layers apart: menus stay open across a project load. The second list is disabled
# unless a mesh is selected with a sculpting tool, and a `set` on a disabled widget is an error
MENUS = [108, 3326, 9959, 13905, 18138, 17912, 40184, 35769]
MESH_MENUS = [6399, 11516, 33331, 32972, 23086, 19331, 27845]
SCENE = 3326
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, SUB = 56799, 57353
LAYERS, PIN = 33760, 33753            # top bar button, the pin of its panel header
CLAY, DEL_LAYER, TOOLBOX = 67742, 67764, 58936
WINDOW = [1200, 885]                  # the size of the other clips (what macOS clamped [1200, 900] to)
# front view, the whole face (ears included) between the left toolbar's sliders and the pinned Layers panel
VIEW = {"pivot": [-0.12619, -0.32877, 0.17157], "rotation": [0, 0, 0, 1],
        "translation": [0.346, 0.133, 2.41]}          # the translation is relative to the pivot
# The DelLayer ring (radius ~117) stays where the pointer last left the viewport: over the background
# right of the neck, under the panel, never on the face. The pointer rests at START and goes into the
# panel through GATE, across its bottom edge
START, GATE = [930, 730], [935, 690]
# Layers panel rows, 40 px each from y 232; the active layer takes three (name, factor slider, buttons)
PENCIL_TOP, CLONE_TOP = [915, 332], [1015, 332]   # buttons of the active layer when it is the top row
TOP_ROW, SECOND_ROW = [1025, 252], [1025, 372]    # names of the inactive rows around the active one
FACTOR_TOP, FACTOR_SECOND = 292, 332              # y of the active layer's factor slider
FACTOR_X = (1082, 792)                # the slider (x 802 to 1084) is relative, its width for 100 %: this
FACTOR_UP = (812, 1112)               # empties it without leaving the panel (x 790 to 1140); and back
OK_AT = [979, 450]                    # Ok of the "New name" dialog, which opens under the pencil
# DelLayer scrubs over each half of the smile: mouth corner, cheek and eye bag, around the mouth center
MOUTH = [432, 444]
SCALE = 1 / 1.2                       # the path and the radius were laid out on a view 1.2 times closer
HALF = [[110, -160], [265, -135], [100, -70], [280, -30], [90, 25], [265, 65], [100, 115], [225, 150]]
RIGHT = [[MOUTH[0] + x * SCALE, MOUTH[1] + y * SCALE] for x, y in HALF]
LEFT = [[MOUTH[0] - x * SCALE, MOUTH[1] + y * SCALE] for x, y in HALF]

c = Clip(START, seed=31)
steps = c.steps


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def glide(t, a=0.05, d=0.15):
    """Up to speed at once, steady, a soft landing: an eased start counts as a long press while recording."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def scrub(way, n=110):
    c.go(way[0]); c.wait(8)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(way, glide(i / n))]
                                           for i in range(n + 1)]})
    c.pos = list(way[-1])
    c.wait(20)


def enter():
    """From the viewport to the panel's bottom edge: see START."""
    c.go(GATE)


def slide(y, down=True, n=65):
    """Drag the active layer's factor to 0 % (or back to 100 %), slowly: half of the face moves with it."""
    x0, x1 = FACTOR_X if down else FACTOR_UP
    c.go([x0, y]); c.wait(14)
    steps.append({"do": "drag", "points": [[round(x0 + (x1 - x0) * min_jerk(i / n), 1), y] for i in range(n + 1)]})
    c.pos = [x1, y]


def unpin():
    steps.append({"do": "set", "id": LAYERS, "value": True})
    c.wait(10)
    steps.append({"do": "set", "id": PIN, "value": False})
    steps.append({"do": "set", "id": LAYERS, "value": False})
    c.wait(20)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})     # the project opens with its head selected
    c.wait(5)
    unpin()
    for i in MESH_MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    steps.extend(look())                                       # post process off, the scene brightened
    c.wait(20)
    steps.append({"do": "set", "id": SCENE, "value": True})
    c.wait(5)
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": False})
    c.wait(20)
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 900})   # DelLayer is far down the toolbox
    c.wait(5)
    steps.append({"do": "set", "id": DEL_LAYER, "value": True})
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": round(140 * SCALE)})
    steps.append({"do": "set", "text": "intensity.png", "type": "slider", "value": 1})
    steps.append({"do": "set", "id": SUB, "value": False})     # Invert off
    steps.append({"do": "set", "id": SYM, "value": False})     # one side at a time
    steps.append(dict({"do": "camera"}, **VIEW))
    steps.append({"do": "set", "id": LAYERS, "value": True})
    c.wait(10)
    steps.append({"do": "set", "id": PIN, "value": True})
    c.tap(PENCIL_TOP)                                         # the smile layer (active, top row): "left"
    c.wait(10)
    for ch in "left":
        steps.append({"do": "type", "input": ch})
    steps.append({"do": "click", "text": "Ok"})
    steps.append({"do": "drag", "points": [[930, 500], [930, 600], [930, 680], START], "hover": True})
    c.wait(90)
    steps.append({"do": "stats"})
elif sys.argv[1] == "restore":
    unpin()
else:
    name = sys.argv[2] if len(sys.argv) > 2 else "layer_leftright"
    if name != "dry":
        steps.append({"do": "record", "to": name})
    c.wait(40)                          # a symmetrical smile, on its own layer
    enter(); c.click(CLONE_TOP); c.wait(25)   # clone it: two layers, the smile doubles
    scrub(RIGHT)                        # DelLayer: this one keeps the left half only
    enter(); c.click(TOP_ROW)           # the copy
    c.click(PENCIL_TOP)                 # rename it
    for ch in "right":
        steps.append({"do": "type", "input": ch}); c.wait(c.rng.randint(8, 14))
    c.click(OK_AT)
    scrub(LEFT)                         # and it keeps the right half only
    enter()
    slide(FACTOR_TOP); c.wait(55)       # "right" to 0 %: that side of the smile drops
    slide(FACTOR_TOP, down=False); c.wait(25)
    c.click(SECOND_ROW)                 # "left"
    slide(FACTOR_SECOND); c.wait(55)    # the other side
    slide(FACTOR_SECOND, down=False); c.wait(20)
    slide(FACTOR_SECOND); c.wait(45)    # once more: the clip ends on half a smile
    c.go([930, 520]); c.go(START); c.wait(40)   # out through the panel's bottom edge
    if name != "dry":
        steps.append({"do": "record"})
print(c.json())
