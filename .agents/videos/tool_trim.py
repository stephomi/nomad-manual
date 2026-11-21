#!/usr/bin/env python3
"""docs/videos/tool_trim.mp4: Trim on a sphere seen through an orthographic camera. The Tool menu shows
the `Hole filling` settings (Boolean), then three shapes picked from the left toolbar's shape popup: a
Line slices the top off, a Rect punches a square tunnel, a Lasso bites the side; a look around shows
the flat filled cuts. See .agents/videos.md.

    AI_SESSION=<s> tool_trim.py setup | AI_SESSION=<s> python3 ../nomad/.agents/ai.py send -
    tool_trim.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Setup asks the running Nomad (AI_SESSION, AI_PY: that session's ai.py) whether Trim shows its shapes
as a list or as a popup (a saved per-tool setting) and switches to the popup the page describes.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import json
import math
import os
import subprocess
import sys

from clip import Clip, min_jerk

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../nomad/.agents/ai.py"))
LAYOUT, SHAPES = 54629, 48750

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOPO, MULTIRES_TAB, DELETE_LOWER = 6399, 67820, 6498
CAMERA_MENU, ORTHO = 17912, 18086
TOOLBOX, TRIM = 58936, 67756
SYM = 56799
TOOL_MENU, BOOLEAN = 28318, 31921
# Files > New keeps the camera of the previous scene: set it. The sphere is then centered at ~600,460,
# radius ~205
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0.04, 1.3]}
WINDOW = [1200, 900]
START = [1010, 700]
TOOL_AT = [775, 25]
SHAPE_AT = [25, 331]                       # the shape button of the left toolbar: opens the popup
LASSO_P, LINE_P, RECT_P = [173, 265], [173, 325], [98, 385]

c = Clip(START, seed=5)
steps = c.steps


def glide(t):
    """A shape drag: eased, but still moving at release (a pause at the end is `Edit: Hold`)."""
    return 0.55 * t + 0.45 * min_jerk(t)


def drag(points):
    steps.append({"do": "drag", "points": [[round(x, 1), round(y, 1)] for x, y in points]})
    c.pos = list(points[-1])


def line(a, b, n):
    drag([[a[0] + (b[0] - a[0]) * glide(i / n), a[1] + (b[1] - a[1]) * glide(i / n)] for i in range(n + 1)])


def lasso(center, rx, ry, start_deg, n):
    """A freehand loop, a little irregular, closing on itself."""
    pts = []
    for i in range(n + 1):
        a = math.radians(start_deg) + 2 * math.pi * glide(i / n) * 0.97
        r = 1 + 0.06 * math.sin(3 * a + 0.7)
        pts.append([center[0] + rx * r * math.cos(a), center[1] + ry * r * math.sin(a)])
    c.go(pts[0]); c.wait(10)
    drag(pts)


def shape(p):
    c.click(SHAPE_AT); c.wait(15)
    c.click(p)


def popup_layout():
    """Steps that switch the tool's shapes to the popup layout, if Nomad shows them as a list."""
    q = [{"do": "scroll", "id": TOOLBOX, "to": 600}, {"do": "set", "id": TRIM, "value": True},
         {"do": "find", "in": SHAPES, "type": "button"}]
    out = subprocess.run([sys.executable, AI_PY, "send", json.dumps(q)], capture_output=True, text=True).stdout
    return [{"do": "click", "id": LAYOUT}] if out.count('icon="shape_') > 1 else []


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.extend(popup_layout())
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    # the new sphere has multires levels: Trim would warn they get lost
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": MULTIRES_TAB})
    steps.append({"do": "click", "id": DELETE_LOWER})
    steps.append({"do": "set", "id": TOPO, "value": False})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": True})   # Trim cuts along the view: orthographic
    steps.append({"do": "click", "id": ORTHO})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "dolly": 0.72})               # orthographic zoom: radius ~200
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 600})     # Trim in view in the toolbox
    c.wait(5)
    steps.append({"do": "set", "id": TRIM, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "set", "id": TOOL_MENU, "value": True})
    steps.append({"do": "click", "id": BOOLEAN})
    steps.append({"do": "set", "id": TOOL_MENU, "value": False})
    c.tap(SHAPE_AT); c.wait(10); c.tap(LASSO_P); c.wait(10)    # start from the default shape
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_trim"})
    c.wait(30)
    c.click(TOOL_AT); c.wait(50)                 # Tool menu: Hole filling, Boolean
    c.click(TOOL_AT)
    shape(LINE_P)                                # Line: slice the top off
    a = [420, 268]; c.go(a); c.wait(10)
    line(a, [820, 420], 45); c.wait(45)
    shape(RECT_P)                                # Rect: a square tunnel
    a = [455, 480]; c.go(a); c.wait(10)
    line(a, [560, 585], 35); c.wait(45)
    shape(LASSO_P)                               # Lasso: a bite out of the side
    lasso([775, 545], 75, 95, 200, 60); c.wait(45)
    c.go(START); c.wait(10)
    # around: the flat top and the tunnel from the left, then the bite on the right
    c.camera(320, yaw=[(0.4, 38), (1, -34)], pitch=[(0.35, 26), (1, 20)], dolly=[(0.5, 1.08), (1, 1.05)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
