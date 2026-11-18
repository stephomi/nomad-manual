#!/usr/bin/env python3
"""docs/videos/stroke_randomize.mp4: close-up on the boring head's temple with Crease. A plain stroke
draws a clean line; Stroke menu > Randomize on (Offset, Intensity, Rotation, Scale), and strokes over
the same skin scatter into pores and small creases. Post process off and the scene brightened:
boringhead.py. See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    stroke_randomize.py setup | python3 ../../.agents/ai.py send -
    stroke_randomize.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import math
import sys

from boringhead import PROJECT, look
from clip import Clip

MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]
SCENE = 3326
ICONS = [4059, 4060, 4058]
SYM, RADIUS = 56799, 56725
LAYERS, BASE_ROW = 33760, 33814
TOOLBOX, CREASE = 58936, 67754
STROKE_MENU, STROKE_PANEL = 19331, 19318
SPACING, RANDOMIZE, RND_OFFSET = 19368, 19612, 19653
WINDOW = [1200, 885]                  # what macOS clamped [1200, 900] to when the clip was written

STROKE_MENU_AT = [825, 25]
RANDOMIZE_AT = [1100, 585]            # Randomize's checkbox, the Stroke tab scrolled down
START = [1000, 160]                   # resting pointer, background right of the head
LINE = ([300, 330], [650, 300])

c = Clip(START, seed=29)
steps = c.steps


def prepare():
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    steps.extend(look())
    steps.append({"do": "click", "id": SCENE})
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": SYM, "value": False})


def scribble(x0, x1, y, amp, n):
    """A zigzag across the skin, like hatching skin texture in."""
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append([round(x0 + (x1 - x0) * t, 1), round(y + amp * math.sin(t * math.pi * 7), 1)])
    c.go(pts[0]); c.wait(8)
    steps.append({"do": "drag", "points": pts})
    c.pos = pts[-1]
    c.wait(15)


if sys.argv[1] == "setup":
    prepare()
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "click", "id": BASE_ROW})        # sculpt the base, not the smile layer
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 300})
    steps.append({"do": "set", "id": CREASE, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 35})
    steps.append({"do": "click", "id": STROKE_MENU})
    steps.append({"do": "click", "text": "Stroke", "type": "radio_option", "in": STROKE_PANEL})
    steps.append({"do": "scroll", "id": STROKE_PANEL, "to": 600})
    steps.append({"do": "set", "id": RANDOMIZE, "value": True})   # its rows show once it's on
    steps.append({"do": "set", "id": SPACING, "value": 25})       # distinct dabs, each one randomized
    steps.append({"do": "set", "id": RND_OFFSET, "value": 50})
    steps.append({"do": "set", "id": RANDOMIZE, "value": False})
    steps.append({"do": "scroll", "id": STROKE_PANEL, "to": 600})
    steps.append({"do": "click", "id": STROKE_MENU})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(20)
    steps.append({"do": "camera", "orbit": [-35, 20], "frames": 1})  # the temple, above the ear
    steps.append({"do": "camera", "dolly": 0.45, "frames": 1})
    steps.append({"do": "camera", "pan": [0.05, 0.2], "frames": 1})
    steps.append({"do": "drag", "points": [[1300, 880], [1300, 160], START], "hover": True})
    c.wait(200)  # the "Reset view" toast fades on wall-clock time
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "stroke_randomize"})
    c.wait(30)
    a, b = LINE
    c.go(a); c.wait(10)
    c.stroke(a, b, 60, bow=0.04); c.wait(30)     # a plain crease line
    c.click(STROKE_MENU_AT)
    c.click(RANDOMIZE_AT); c.wait(60)            # Randomize: Offset, Intensity, Rotation, Scale
    c.click(STROKE_MENU_AT)
    scribble(260, 640, 420, 28, 110)             # scattered dabs: pores and small creases
    scribble(640, 280, 500, 28, 110)
    scribble(300, 600, 580, 26, 100)
    c.go(START); c.wait(10)
    c.camera(180, yaw=[(0.5, 10), (1, 7)], pitch=[(0.5, -5), (1, -3)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
