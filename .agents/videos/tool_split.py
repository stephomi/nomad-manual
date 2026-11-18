#!/usr/bin/env python3
"""docs/videos/tool_split.mp4: Split on a sphere (orthographic camera): a Lasso across its top cuts it
into two objects, the Gizmo picked in the toolbox pulls the lower one away, a look around shows both
cut faces filled (`Hole filling`: Boolean). See .agents/videos.md.

    AI_SESSION=<s> tool_split.py setup | AI_SESSION=<s> python3 ../../.agents/ai.py send -
    tool_split.py record [name] | python3 ../../.agents/ai.py send - 900
Setup asks the running Nomad (AI_SESSION, AI_PY: that session's ai.py) whether Split shows its shapes
as a list or as a popup (a saved per-tool setting) and switches to the popup the page describes.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import json
import math
import os
import subprocess
import sys

from clip import Clip, min_jerk

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../.agents/ai.py"))
FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOPO, MULTIRES_TAB, DELETE_LOWER = 6399, 67820, 6498
CAMERA_MENU, ORTHO = 17912, 18086
TOOLBOX, SPLIT = 58936, 67757
SYM, LAYOUT, SHAPES = 56799, 54629, 48750
TOOL_MENU, BOOLEAN = 28318, 31921
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0.04, 1.3]}
WINDOW = [1200, 900]
START = [1010, 700]
SHAPE_AT, LASSO_P = [25, 331], [173, 265]
TOOLBOX_SCROLL = 900                        # Split near the top of the toolbox
GIZMO_AT = [1170, 676]                      # after the toolbox is dragged up 250 (scroll ~1143)
ARROW = [600, 309]                          # the cone of the gizmo's green (Y) arrow (gizmo at the sphere center)

c = Clip(START, seed=8)
steps = c.steps


def glide(t):
    """A shape drag: eased, but still moving at release (a pause at the end is `Edit: Hold`)."""
    return 0.55 * t + 0.45 * min_jerk(t)


def drag(points):
    steps.append({"do": "drag", "points": [[round(x, 1), round(y, 1)] for x, y in points]})
    c.pos = list(points[-1])


def lasso(center, rx, ry, start_deg, n):
    pts = []
    for i in range(n + 1):
        a = math.radians(start_deg) + 2 * math.pi * glide(i / n) * 0.97
        r = 1 + 0.05 * math.sin(3 * a + 0.7)
        pts.append([center[0] + rx * r * math.cos(a), center[1] + ry * r * math.sin(a)])
    c.go(pts[0]); c.wait(10)
    drag(pts)


def scroll_toolbox(a, dy, n=40):
    """A finger push on the toolbox, slowed to a stop before release so it doesn't coast. It must move
    from its first frame: a press that stays still is a long press, which drags the tool to another
    place in the toolbox (and the new order is saved in the user folder's settings)."""
    c.go(a); c.wait(10)
    drag([[a[0], a[1] - dy * (1 - (1 - i / n) ** 2.5)] for i in range(n + 1)] + [[a[0], a[1] - dy]] * 6)
    c.wait(15)


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def popup_layout():
    """Steps that switch the tool's shapes to the popup layout, if Nomad shows them as a list."""
    q = [{"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL}, {"do": "set", "id": SPLIT, "value": True},
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
    steps.append({"do": "set", "id": TOPO, "value": True})     # no multires: Split would warn it gets lost
    steps.append({"do": "click", "id": MULTIRES_TAB})
    steps.append({"do": "click", "id": DELETE_LOWER})
    steps.append({"do": "set", "id": TOPO, "value": False})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": True})
    steps.append({"do": "click", "id": ORTHO})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "dolly": 0.72})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": SPLIT, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "set", "id": TOOL_MENU, "value": True})
    steps.append({"do": "click", "id": BOOLEAN})
    steps.append({"do": "set", "id": TOOL_MENU, "value": False})
    c.tap(SHAPE_AT); c.wait(10); c.tap(LASSO_P); c.wait(10)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_split"})
    c.wait(30)
    lasso([600, 290], 300, 115, 185, 60); c.wait(50)     # Lasso across the top: two objects
    scroll_toolbox([1170, 650], 250)
    pick(GIZMO_AT)                                       # Gizmo: pull the lower part away
    c.go(ARROW); c.wait(15)
    c.stroke(ARROW, [ARROW[0], ARROW[1] + 130], 45, bow=0.0); c.wait(30)
    c.go(START); c.wait(10)
    c.camera(240, yaw=[(0.5, -32), (1, -24)], pitch=[(0.5, 26), (1, 18)], dolly=[(0.5, 1.12), (1, 1.1)],
             pan_y=[(0.5, 0.08), (1, 0.06)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
