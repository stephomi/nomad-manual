#!/usr/bin/env python3
"""docs/videos/tool_mask2.mp4: a band of mask painted around the woman's neck, the Mask settings opened
from the Tool menu (Extract / Split / Carve tabs, Height, Smoothness, Sides) with the shell previewed,
`Extract` makes it a new object: a choker; a look around it. Post process off (the main checkbox of its
menu), as a new user sees the app. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_mask2.py setup | python3 ../../.agents/ai.py send -
    tool_mask2.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import os
import sys

from clip import Clip, min_jerk

PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/woman.nom")
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
POST_ON = 13907                       # the checkbox of the "Post Process" title
SHADING, SHADING_PANEL, LIGHT_ICONS = 9959, 9946, 11359
TOOLBOX = 58936
CLAY, MASK, MASK_AT = 67742, 67748, [1170, 476]
SYM, RADIUS, SUB = 56799, 56725, 57353
TOOL_MENU, TOOL_AT, TOOL_PANEL = 28318, [775, 25], 28305
EXTRACT_TAB, EXTRACT_AT, HEIGHT = 29843, [930, 339], 28670
VIEW = {"pivot": [-1.5825, -0.0396, -0.5274], "rotation": [0.0054591, 0.0914579, 0.0005014, 0.9957939],
        "translation": [1.65, -0.3, 8.4]}
WINDOW = [1200, 900]
START = [1010, 700]

c = Clip(START)
steps = c.steps


def post_process():
    """Render resolution x1 and the whole post process off: what a new user sees."""
    steps.append({"do": "set", "id": POST, "value": True})
    c.wait(5)
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})
    steps.append({"do": "set", "id": POST, "value": False})


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it
    (2 frames: with the machine loaded, 4 recorded frames already lasted long enough to borrow)."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 2)
    c.wait(20)


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def pace(t):
    """Eased, but with speed left at both ends: a press that stays within 7 px for 0.7 s (wall-clock, and
    recording slows the frames) snaps the stroke into a curve ("Enter curve edit mode?")."""
    return 0.5 * t + 0.5 * min_jerk(t)


def scribble(way, n, rest=20):
    c.go(way[0]); c.wait(8)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(way, pace(i / n))] for i in range(n + 1)]})
    c.pos = list(way[-1])
    c.wait(rest)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(20)
    post_process()
    steps.append({"do": "set", "id": SHADING, "value": True})
    c.wait(5)
    steps.append({"do": "scroll", "id": SHADING_PANEL, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": LIGHT_ICONS, "value": False})
    steps.append({"do": "set", "id": SHADING, "value": False})
    steps.append(dict({"do": "camera"}, **VIEW))
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": MASK, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 24})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": TOOL_MENU, "value": True})  # the Mask settings open on Extract
    c.wait(5)
    steps.append({"do": "scroll", "id": TOOL_PANEL, "to": 0})
    steps.append({"do": "click", "id": EXTRACT_TAB})
    steps.append({"do": "set", "id": HEIGHT, "value": 0.2})  # a thicker choker than the default 0.1
    steps.append({"do": "set", "id": TOOL_MENU, "value": False})
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Mask itself
    steps.append({"do": "set", "id": RADIUS, "value": 70})  # Clay's own radius: the ring of the first frames
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_mask2"})
    c.wait(25)
    pick(MASK_AT)
    # a band around the neck, each stroke starting at its middle: the neck's edges are close to the
    # background, where a drag would turn the camera
    scribble([[575, 450], [535, 442], [500, 436], [540, 440], [580, 446], [620, 440], [655, 434]], 80)
    scribble([[575, 480], [535, 474], [502, 468], [540, 472], [580, 478], [620, 472], [652, 466]], 80)
    c.click(TOOL_AT); c.wait(70)                 # Mask settings: the shell is previewed
    c.click(EXTRACT_AT); c.wait(30)              # Extract: a new object, the menu closes
    c.go(START); c.wait(15)
    c.camera(220, yaw=[(0.5, 38), (0.85, 12), (1, 14)], pitch=[(0.45, 14), (1, 6)], dolly=[(0.5, 0.9), (1, 0.92)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
