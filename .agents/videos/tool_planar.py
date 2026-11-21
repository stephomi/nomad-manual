#!/usr/bin/env python3
"""docs/videos/tool_planar.mp4: Planar picked in the toolbox; two sweeps cut into a sphere, then a stroke
that starts on the cut and works outwards cleans it into one flat, hard-edged face. The `Fill` sub mode
does the opposite next to it: a flat plateau pulled up. A look around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_planar.py setup | python3 ../nomad/.agents/ai.py send -
    tool_planar.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import math
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
WIREFRAME = 46039
TOOLBOX, TOOLBOX_SCROLL = 58936, 600
CLAY, PLANAR, PLANAR_AT = 67742, 67752, [1170, 132]
SYM, RADIUS, INTENSITY, SUB, SUB_AT = 56799, 56725, 56745, 57353, [25, 477]
# a new scene's view (pivot at the origin, 25° FoV), turned a little so the faces catch the light
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 3.35921049118042]}
VIEW = [-25, 12]
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
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it.
    The same goes for the sub mode button of the left toolbar."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def sweep(a, b, n, bow=0.03):
    c.go(a); c.wait(10)
    c.stroke(a, b, n, bow)
    c.wait(12)


def spiral(center, radius, turns, n):
    """One stroke from the center outwards: starting on the plane and working out keeps that plane."""
    pts = []
    for i in range(n + 1):
        u = min_jerk(i / n)
        a = u * turns * 2 * math.pi
        pts.append([round(center[0] + radius * u * math.cos(a), 1),
                    round(center[1] + radius * u * math.sin(a) * 0.8, 1)])
    c.go(pts[0]); c.wait(10)
    steps.append({"do": "drag", "points": pts})
    c.pos = pts[-1]
    c.wait(18)


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
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": PLANAR, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 110})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Planar itself
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "orbit": VIEW})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_planar"})
    c.wait(25)
    pick(PLANAR_AT)
    sweep([440, 330], [600, 300], 40)            # two quick sweeps cut into the sphere
    sweep([590, 330], [450, 370], 40, -0.03)
    spiral([520, 345], 80, 2, 110)               # from the cut outwards: one clean plane
    pick(SUB_AT)                                 # Fill: a plateau pulled up to the highest point
    sweep([680, 470], [760, 560], 40)
    spiral([720, 520], 62, 2.25, 100)
    c.go(REST); c.wait(10)                       # (Fill stays on: setup turns it off)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": HOME["pivot"], "translation": HOME["translation"]})
    c.camera(180, yaw=[(0.5, -38), (0.85, -8), (1, -11)], pitch=[(0.45, 12), (1, 4)],
             dolly=[(0.5, 0.96), (1, 0.98)])
    c.wait(25)
    steps.append({"do": "record"})
print(c.json())
