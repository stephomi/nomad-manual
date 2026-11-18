#!/usr/bin/env python3
"""docs/videos/tool_flatten.mp4: Flatten picked in the toolbox, then a few strokes cut flat planes into the
woman bust's shoulders and chest; a short look around shows them in the light. Post process off (the
main checkbox of its menu), as a new user sees the app. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_flatten.py setup | python3 ../../.agents/ai.py send -
    tool_flatten.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import os
import sys

from clip import Clip

PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/woman.nom")
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
POST_ON = 13907                       # the checkbox of the "Post Process" title
SHADING, LIGHT_ICONS = 9959, 11359
CAMERA, CAMERA_ICONS = 17912, 18069
LAYERS = 33760
TOOLBOX = 58936
CLAY, FLATTEN, FLATTEN_AT = 67742, 67751, [1170, 668]
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
WINDOW = [1200, 900]
START = [1010, 700]                   # resting pointer, background right of the head

c = Clip(START)
steps = c.steps


def post_process():
    """Render resolution x1 and the whole post process off: what a new user sees."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})
    steps.append({"do": "set", "id": POST, "value": False})


def no_icons():
    """Light and camera gizmos would clutter the viewport."""
    for menu, panel, icons in ((SHADING, 9946, LIGHT_ICONS),):  # no scene camera here: no camera icons
        steps.append({"do": "set", "id": menu, "value": True})
        c.wait(5)
        steps.append({"do": "scroll", "id": panel, "to": 0})
        c.wait(5)
        steps.append({"do": "set", "id": icons, "value": False})
        steps.append({"do": "set", "id": menu, "value": False})


def pick(p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def sweep(a, b, n, bow=0.03):
    c.go(a); c.wait(10)
    c.stroke(a, b, n, bow)
    c.wait(15)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(20)
    steps.append({"do": "set", "id": LAYERS, "value": False})
    post_process()
    no_icons()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": FLATTEN, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 80})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Flatten itself
    steps.append({"do": "set", "id": RADIUS, "value": 80})  # Clay's own radius: the ring of the first frames
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_flatten"})
    c.wait(25)
    pick(FLATTEN_AT)
    sweep([725, 570], [870, 590], 50)            # top of her left shoulder, back and forth
    sweep([860, 600], [730, 585], 45, -0.03)
    sweep([745, 640], [865, 670], 45)            # its front plane
    sweep([490, 610], [350, 650], 50, -0.03)     # the other shoulder
    sweep([360, 665], [480, 640], 45)
    sweep([520, 730], [690, 720], 55)            # upper chest
    c.go(START); c.wait(10)
    c.camera(160, yaw=[(0.55, -28), (1, -22)], pitch=[(0.5, 10), (1, 7)])
    c.wait(25)
    steps.append({"do": "record"})
print(c.json())
