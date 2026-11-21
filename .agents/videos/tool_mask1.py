#!/usr/bin/env python3
"""docs/videos/tool_mask1.mp4: Mask picked in the toolbox paints a few mask blobs on a sphere; Paint
strokes across it leave the masked spots untouched. Back on Mask, `Unmask` erases one blob, and paint
now covers that spot too. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_mask1.py setup | python3 ../nomad/.agents/ai.py send -
    tool_mask1.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX = 58936
CLAY, MASK, MASK_AT, PAINT, PAINT_AT = 67742, 67748, [1170, 476], 67749, [1170, 540]
SYM, RADIUS, SUB, UNMASK_AT = 56799, 56725, 57353, [25, 477]
# Files > New keeps the camera of the previous scene: set it. The sphere is then centered at 600,450, radius
# ~215: every stroke starts inside it (off the mesh, a drag turns the camera)
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0.04, 1.3]}
WINDOW = [1200, 900]
START = [1010, 700]

c = Clip(START)
steps = c.steps


def post_process():
    """A new scene has the post process off: only the render resolution to set."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
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


def scribble(way, n, rest=18):
    """One stroke through the waypoints, eased at both ends."""
    c.go(way[0]); c.wait(8)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(way, min_jerk(i / n))] for i in range(n + 1)]})
    c.pos = list(way[-1])
    c.wait(rest)


def blob(p, r, n=40):
    """A small filled loop around p."""
    way = [[p[0] + dx * r, p[1] + dy * r] for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1), (-0.8, 0.1), (0.2, -0.3))]
    scribble(way, n)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    post_process()
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    for tool, r in ((MASK, 34), (PAINT, 75), (CLAY, 70)):  # the clip starts on Clay
        steps.append({"do": "set", "id": tool, "value": True})
        steps.append({"do": "set", "id": RADIUS, "value": r})
        steps.append({"do": "set", "id": SUB, "value": False})  # Unmask / Erase off, whatever a take left
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_mask1"})
    c.wait(25)
    pick(MASK_AT)
    blob([500, 360], 30)                                      # mask blobs
    blob([690, 330], 26)
    blob([600, 540], 32)
    scribble([[430, 470], [480, 450], [530, 470]], 30)        # and a little smile of mask
    pick(PAINT_AT)
    scribble([[470, 330], [730, 330], [440, 420], [760, 430], [450, 520], [740, 530], [520, 600], [680, 610]], 170, 30)
    pick(MASK_AT)
    pick(UNMASK_AT)                                           # Unmask: rub one blob away
    scribble([[655, 295], [730, 290], [655, 325], [735, 325], [660, 360], [725, 360], [690, 315]], 60, 25)
    pick(UNMASK_AT)
    pick(PAINT_AT)
    scribble([[640, 300], [740, 330], [650, 360], [730, 360]], 45, 30)
    c.go(START); c.wait(40)
    steps.append({"do": "record"})
print(c.json())
