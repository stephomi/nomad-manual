#!/usr/bin/env python3
"""docs/videos/tool_lathe.mp4: Lathe in an empty scene. Lathe is picked in the toolbox, a Curve stroke
right of the fixed center line draws a vase profile; a curve point is pulled out to round the belly;
the top toolbar's `Hole` gives the vase a wall and an opening; a look from above into it, then
`Validate`. See .agents/videos.md.

    tool_lathe.py setup | python3 ../../.agents/ai.py send -
    tool_lathe.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. Tools are picked by
label: their ids follow the toolbox order."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
SCENE, DELETE = 3326, 3912
CAMERA_MENU, PERSPECTIVE = 17912, 18085
TOOLBOX = 58936
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 2.2]}
WINDOW = [1200, 900]
START = [1010, 700]
LATHE_AT = [1170, 156]                     # second in the toolbox of an empty scene
# the profile, bottom (next to the center line at x 600) to lip
PROFILE = [[612, 700], [700, 690], [770, 600], [760, 480], [690, 380], [675, 310], [730, 245]]
POINT, POINT_TO = [803, 496], [872, 515]   # the belly's curve point, pulled out
HOLE_AT, VALIDATE_AT = [630, 123], [202, 123]   # lathe toolbar

c = Clip(START, seed=31)
steps = c.steps


def glide(t):
    """Eased, but still moving at release: a pause at the end of a stroke is `Edit: Hold`."""
    return 0.55 * t + 0.45 * min_jerk(t)


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def handle(a, b, n):
    """Grab a curve point (rest on it first so it highlights) and pull it."""
    c.go(a); c.wait(12)
    steps.append({"do": "drag", "points": [a, a] + [[round(a[0] + (b[0] - a[0]) * min_jerk(i / n), 1),
                                                    round(a[1] + (b[1] - a[1]) * min_jerk(i / n), 1)]
                                                   for i in range(1, n + 1)] + [b] * 4})
    c.pos = list(b)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": True})    # an empty scene: only the vase
    steps.append({"do": "click", "id": DELETE})
    steps.append({"do": "set", "id": SCENE, "value": False})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": True})
    steps.append({"do": "click", "id": PERSPECTIVE})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "text": "View", "in": TOOLBOX, "value": True})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(10)
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_lathe"})
    c.wait(30)
    pick(LATHE_AT)                                       # the center line shows
    n = 70
    c.go(PROFILE[0]); c.wait(10)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(PROFILE, glide(i / n))] for i in range(n + 1)]})
    c.pos = list(PROFILE[-1]); c.wait(45)
    handle(POINT, POINT_TO, 30); c.wait(30)              # a rounder belly
    c.click(HOLE_AT, hold=2); c.wait(30)                 # Hole: a wall and an opening
    c.go(START); c.wait(10)
    # up to look into it, a quarter turn around, back down
    c.camera(260, yaw=[(1, -40)], pitch=[(0.5, 38), (1, 12)], dolly=[(0.5, 1.05), (1, 1.0)], pan_y=[(0.5, 0.05), (1, 0)])
    c.wait(20)
    c.click(VALIDATE_AT, hold=2); c.wait(50)             # Validate: a mesh to sculpt
    c.go(START); c.wait(20)
    steps.append({"do": "record"})
print(c.json())
