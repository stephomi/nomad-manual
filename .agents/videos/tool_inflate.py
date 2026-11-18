#!/usr/bin/env python3
"""docs/videos/tool_inflate.mp4: Inflate picked in the toolbox; a curved stroke puffs a ridge out of a
sphere, small circles in one place blow a balloon, then `Sub` deflates a groove. A look around shows the
balloon in profile. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_inflate.py setup | python3 ../../.agents/ai.py send -
    tool_inflate.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import math
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
WIREFRAME = 46039
TOOLBOX, TOOLBOX_SCROLL = 58936, 600
CLAY, INFLATE, INFLATE_AT = 67742, 67760, [1170, 644]
SYM, RADIUS, INTENSITY, SUB, SUB_AT = 56799, 56725, 56745, 57353, [25, 477]
# a new scene's view (pivot at the origin, 25° FoV), turned a little
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
    The same goes for the Sub button of the left toolbar."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def catmull(pts, u):
    """Point at u (0..1) on a Catmull-Rom curve through pts."""
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
    c.wait(20)


def circles(center, radius, turns, n):
    """Small circles around one spot: the stroke keeps inflating the same area."""
    pts = []
    for i in range(n + 1):
        u = i / n
        a = u * turns * 2 * math.pi
        r = radius * min(1, 4 * u, 4 * (1 - u))  # leaves from the center and comes back to it
        pts.append([round(center[0] + r * math.cos(a), 1), round(center[1] + r * math.sin(a), 1)])
    c.go(pts[0]); c.wait(10)
    steps.append({"do": "drag", "points": pts})
    c.pos = pts[-1]
    c.wait(20)


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
    steps.append({"do": "set", "id": INFLATE, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 75})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Inflate itself
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "orbit": VIEW})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_inflate"})
    c.wait(25)
    pick(INFLATE_AT)
    scribble([[430, 570], [400, 430], [465, 305], [585, 255]], 85)   # a puffed ridge
    circles([725, 430], 14, 4, 150)                                  # a balloon
    pick(SUB_AT)                                                     # Sub: deflates
    scribble([[490, 610], [615, 665], [745, 615]], 70)
    c.go(REST); c.wait(10)                                           # (Sub stays on: setup turns it off)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": HOME["pivot"], "translation": HOME["translation"]})
    c.camera(180, yaw=[(0.5, 50), (0.85, 22), (1, 25)], pitch=[(0.45, -8), (1, -3)],
             dolly=[(0.5, 1.04), (1, 1.02)])
    c.wait(25)
    steps.append({"do": "record"})
print(c.json())
