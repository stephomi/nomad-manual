#!/usr/bin/env python3
"""docs/videos/tool_project.mp4: Project on a sphere (orthographic camera). The shape popup shows the
Project-only `Curve` and `Path`; a wavy Curve drawn across the sphere pushes everything above it onto
the curve; Wireframe then shows the same quads, stretched: no geometry was added or removed. See
.agents/videos.md.

    AI_SESSION=<s> tool_project.py setup | AI_SESSION=<s> python3 ../../.agents/ai.py send -
    tool_project.py record [name] | python3 ../../.agents/ai.py send - 900
Setup asks the running Nomad (AI_SESSION, AI_PY: that session's ai.py) whether Project shows its shapes
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
TOPO, MULTIRES_TAB, DELETE_HIGHER = 6399, 67820, 6499
LEVEL0_AT = [172, 341]                      # left end of the Multires level slider
CAMERA_MENU, ORTHO = 17912, 18086
TOOLBOX, PROJECT = 58936, 67758
SYM, LAYOUT, SHAPES, WIREFRAME = 56799, 54629, 48750, 46039
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0.04, 1.3]}
WINDOW = [1200, 900]
START = [1010, 700]
SHAPE_AT, CURVE_P = [25, 301], [173, 233]   # shape button (no hole filling row above it for Project)
WIREFRAME_AT = [375, 860]

c = Clip(START, seed=12)
steps = c.steps


def glide(t):
    """A shape drag: eased, but still moving at release (a pause at the end is `Edit: Hold`)."""
    return 0.55 * t + 0.45 * min_jerk(t)


def popup_layout():
    """Steps that switch the tool's shapes to the popup layout, if Nomad shows them as a list."""
    q = [{"do": "scroll", "id": TOOLBOX, "to": 600}, {"do": "set", "id": PROJECT, "value": True},
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
    steps.append({"do": "set", "id": TOPO, "value": True})     # level 0 only (6k quads): a readable wireframe
    steps.append({"do": "click", "id": MULTIRES_TAB})
    c.tap(LEVEL0_AT); c.wait(5)
    steps.append({"do": "click", "id": DELETE_HIGHER})
    steps.append({"do": "set", "id": TOPO, "value": False})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": True})
    steps.append({"do": "click", "id": ORTHO})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "dolly": 0.72})
    steps.append({"do": "set", "id": WIREFRAME, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 600})
    c.wait(5)
    steps.append({"do": "set", "id": PROJECT, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    c.tap(SHAPE_AT); c.wait(10); c.tap(CURVE_P); c.wait(10)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_project"})
    c.wait(30)
    c.click(SHAPE_AT); c.wait(25)                # the popup: Curve and Path are Project's own
    c.click(CURVE_P)
    # a wave across the sphere, left to right: what is above it is pushed onto it
    a, b, n = [345, 400], [855, 400], 70
    wave = lambda t: [a[0] + (b[0] - a[0]) * t, a[1] + 38 * math.sin(2 * math.pi * 1.5 * t)]
    c.go(wave(0)); c.wait(10)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in wave(glide(i / n))] for i in range(n + 1)]})
    c.pos = wave(1); c.wait(50)
    c.click(WIREFRAME_AT, hold=2); c.wait(30)    # the same quads, moved (a long press opens its options)
    c.go(START); c.wait(10)
    c.camera(220, yaw=[(0.5, -34), (1, -26)], pitch=[(0.5, 30), (1, 24)], dolly=[(0.5, 1.06), (1, 1.04)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
