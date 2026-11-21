#!/usr/bin/env python3
"""docs/videos/tool_tube.mp4: Tube in an empty scene. Tube is picked in the toolbox, a Curve stroke
draws an S tube; a curve point is dragged to reshape it; the top toolbar's `Radius` switches to a radius
at the start and end and the end's orange handle flares it; `Hole` makes it a pipe; a look into the
flared end, then `Validate`. See .agents/videos.md.

    tool_tube.py setup | python3 ../nomad/.agents/ai.py send -
    tool_tube.py record [name] | python3 ../nomad/.agents/ai.py send - 900
The left toolbar shows its stroke modes as the list the page's image shows (View, Curve, Path, Cross).
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. Tools are picked by
label: their ids follow the toolbox order."""
import math
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
TUBE_AT = [1170, 92]                       # first in the toolbox of an empty scene (only the tools that work there)
POINT, POINT_TO = [564, 528], [474, 497]   # a curve point of the drawn tube, and where it goes
RADIUS_AT, HOLE_AT, VALIDATE_AT = [783, 123], [600, 123], [110, 123]   # tube toolbar
END_HANDLE = [851, 296]                    # orange radius handle of the end, once Radius is start/end

c = Clip(START, seed=21)
steps = c.steps


def glide(t):
    """Eased, but still moving at release: a pause at the end of a stroke is `Edit: Hold`."""
    return 0.55 * t + 0.45 * min_jerk(t)


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def handle(a, b, n):
    """Grab a handle (rest on it first so it highlights) and pull it."""
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
    steps.append({"do": "set", "id": SCENE, "value": True})    # an empty scene: only the tube
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
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_tube"})
    c.wait(30)
    pick(TUBE_AT)
    # an S stroke from bottom left to top right: the tube appears on release, its curve points shown
    n = 60
    s = lambda t: [330 + 540 * t, 690 - 420 * t + 110 * math.sin(2 * math.pi * t)]
    c.go(s(0)); c.wait(10)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in s(glide(i / n))] for i in range(n + 1)]})
    c.pos = s(1); c.wait(45)
    handle(POINT, POINT_TO, 30); c.wait(30)              # edit a curve point
    c.click(RADIUS_AT, hold=2); c.wait(20)               # Radius: one at the start, one at the end
    # flare the end: the handle grows the radius when pulled away from its curve point (it sits below it)
    handle(END_HANDLE, [END_HANDLE[0] + 3, END_HANDLE[1] + 26], 30); c.wait(30)
    c.click(HOLE_AT, hold=2); c.wait(30)                 # Hole: a pipe
    c.go(START); c.wait(10)
    # around to the right, to look into the flared end, and back
    c.camera(260, yaw=[(0.5, -55), (1, -20)], pitch=[(0.5, 10), (1, 4)], dolly=[(0.5, 0.95), (1, 1.0)],
             pan_y=[(0.5, 0.12), (1, 0.03)])
    c.wait(20)
    c.click(VALIDATE_AT, hold=2); c.wait(50)             # Validate: a mesh to sculpt
    c.go(START); c.wait(20)
    steps.append({"do": "record"})
print(c.json())
