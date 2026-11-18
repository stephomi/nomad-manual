#!/usr/bin/env python3
"""docs/videos/tool_pinch.mp4: a sphere with a soft, rounded ridge across it. Pinch picked in the toolbox,
then strokes back and forth along the right half of the ridge only: its crest tightens into a sharp edge
while the left half stays round. A look around shows sharp next to soft, in profile. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_pinch.py setup | python3 ../../.agents/ai.py send - 300
    tool_pinch.py record [name] | python3 ../../.agents/ai.py send - 900
Pinch moves the vertices towards the center of the brush with a steep falloff, so it only reads with a
radius about twice the width of the ridge and an intensity typed above the slider range (3, i.e. 300%).
The cylinder rim of the old clip barely changes, whatever the settings: a rounded convex edge has nothing
to pull together. Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
WIREFRAME = 46039
TOOLBOX, TOOLBOX_SCROLL = 58936, 600
CLAY, BRUSH, PINCH, PINCH_AT = 67742, 67743, 67755, [1170, 324]
SYM, RADIUS, INTENSITY, SUB = 56799, 56725, 56745, 57353
# a new scene's view (pivot at the origin, 25° FoV), seen a little from above
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 3.35921049118042]}
VIEW = [-15, 18]
WINDOW = [1200, 900]
START = [1010, 640]

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


def ridge(x0, x1, n, pause=14):
    """One stroke along the ridge (a shallow arc on screen in VIEW) from x0 to x1. The pen lands and lifts
    while moving: a pointer that stays within 7 px for 0.7 s during a stroke triggers `Stroke snap` (the
    stroke becomes an editable curve), and recorded frames are slow, so the last frames of a long min_jerk
    stroke, or a turnaround inside one drag, are enough."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * (0.5 * min_jerk(u) + 0.5 * u)
        k = (x - 600) / 250.0
        pts.append([round(x, 1), round(400 + 45 * (1 - k * k), 1)])
    c.go(pts[0]); c.wait(8)
    steps.append({"do": "drag", "points": pts})
    c.pos = pts[-1]
    c.wait(pause)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    post_process()
    steps.append({"do": "set", "id": WIREFRAME, "value": False})  # the sandbox settings are shared
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "action", "name": "subdivide"})     # 393k: the pinched flanks stay smooth
    c.wait(5)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "orbit": VIEW})
    # the soft ridge: Brush, there and back
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": BRUSH, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 60})
    steps.append({"do": "set", "id": INTENSITY, "value": 0.6})
    steps.append({"do": "set", "id": SUB, "value": False})
    ridge(380, 820, 120, 5)
    ridge(820, 380, 120, 5)
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": PINCH, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 110})
    steps.append({"do": "set", "id": INTENSITY, "value": 3})
    steps.append({"do": "set", "id": SUB, "value": False})  # Invert
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Pinch itself
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "drag", "points": [[900, 560], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_pinch"})
    c.wait(30)
    pick(PINCH_AT)
    ridge(575, 835, 66)                # the right half of the ridge, back and forth
    ridge(835, 575, 66)
    ridge(575, 835, 66)
    ridge(835, 575, 66, 22)
    c.go(START); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": HOME["pivot"], "translation": HOME["translation"]})
    c.camera(200, yaw=[(0.5, 40), (0.85, 27), (1, 29)], pitch=[(0.45, 11), (1, 7)],
             dolly=[(0.5, 0.96), (1, 0.97)])
    c.wait(35)
    steps.append({"do": "record"})
print(c.json())
