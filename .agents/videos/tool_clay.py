#!/usr/bin/env python3
"""docs/videos/tool_clay.mp4: Clay picked in the toolbox, three wide overlapping strokes build a mass up on a
sphere, `Sub` on the left toolbar digs a hollow with two more; a short look around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_clay.py setup | python3 ../nomad/.agents/ai.py send -
    tool_clay.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
CAMERA, FOV = 17912, 17914
TOPO, MULTIRES, SUBDIVIDE = 6399, 67820, 6482
TOOLBOX = 58936
CLAY, BRUSH, CLAY_AT = 67742, 67743, [1170, 90]
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
SUB, SUB_AT = 57353, [25, 477]
WINDOW = [1200, 900]
START = [1010, 640]
REST = [1010, 715]                    # parked for the look around: the wide ring clear of the model and the UI
HOME_Z = 2.956                        # a new scene is at 3.359: a little closer, the sphere fills the view

c = Clip(START)
steps = c.steps


def new_scene():
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    # a new scene has the post process off: only the render resolution to set
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": CAMERA, "value": True})  # HOME_Z frames the sphere for this field of view
    steps.append({"do": "set", "id": FOV, "value": 25})
    steps.append({"do": "set", "id": CAMERA, "value": False})
    steps.append({"do": "camera", "pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, HOME_Z]})
    # 98k quads leave saw teeth on the sharp edge of a diagonal clay stroke: one more level, 393k
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": MULTIRES})
    steps.append({"do": "click", "id": SUBDIVIDE})
    steps.append({"do": "set", "id": TOPO, "value": False})


def pick(p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def sweep(a, b, n, bow=0.05):
    c.go(a); c.wait(10)
    c.stroke(a, b, n, bow)
    c.wait(15)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    new_scene()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 100})
    steps.append({"do": "set", "id": INTENSITY, "value": 2})  # 200 %: a few strokes must build a mass
    steps.append({"do": "set", "id": SUB, "value": False})  # each tool keeps its own, a new scene too
    steps.append({"do": "set", "id": BRUSH, "value": True})  # the clip picks Clay itself
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_clay"})
    c.wait(25)
    pick(CLAY_AT)
    sweep([390, 380], [630, 220], 40)            # wide strokes side by side, then on top: the clay piles up
    sweep([700, 300], [450, 470], 40, -0.05)
    sweep([420, 430], [660, 250], 40)
    c.click(SUB_AT, hold=1)                      # Sub: the same tool digs
    sweep([560, 640], [790, 520], 40)
    sweep([800, 560], [580, 650], 40, -0.05)
    c.go(REST); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": [0, 0, 0], "translation": [0, 0, HOME_Z]})
    c.camera(140, yaw=[(0.55, 28), (1, 20)], pitch=[(0.5, 12), (1, 7)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
