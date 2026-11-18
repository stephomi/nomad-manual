#!/usr/bin/env python3
"""docs/videos/tool_gizmo.mp4: a horn (a slim Cone primitive, validated) on a sphere, Gizmo tool. The
top toolbar's mode button goes to Rotate; turning the horn on its own center lifts it off the head; with
the left toolbar's `Pivot` on, a tap at the horn's base moves the pivot onto the surface; Pivot off,
the same turn now swings the horn from its base; the top toolbar's `Pivot` popup puts the pivot back
in the middle (Auto). See .agents/videos.md.

    tool_gizmo.py setup | python3 ../../.agents/ai.py send -
    tool_gizmo.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import json
import math
import os
import subprocess
import sys

from clip import Clip, min_jerk

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../.agents/ai.py"))
PIVOT, MODE = 56722, 68011                  # left toolbar Pivot toggle, top toolbar All/Move/Rotate/Scale
MODE_AT, PIVOT_MENU_AT, UNDO_AT, PIVOT_AT = [507, 123], [447, 123], [25, 858], [25, 480]
AUTO_AT, POPUP_CLOSE = [317, 215], [603, 128]     # in the Pivot popup
CENTER, BASE_CENTER, RING_R = [648, 408], [600, 480], 114   # gizmo on the horn's middle / on its base
BASE_AT = [600, 478]                        # the horn's base on the head

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
SCENE, ADD, CONE = 3326, 3911, 3452
CAMERA_MENU, PERSPECTIVE = 17912, 18085
TRANSFORM_MENU = 27845
TX, TY, TZ, RZ, SCALE = 27936, 27956, 27976, 28036, 28056   # Transform menu > Matrix sliders
TOOLBOX, GIZMO = 58936, 67769
HOME = {"pivot": [0.1, 0.2, 0], "rotation": [0, 0, 0, 1], "translation": [0.1, 0.25, 1.7]}
WINDOW = [1200, 900]
START = [1010, 700]
BASE_RADIUS = ([526, 442], [552, 457])     # base radius handle of the placed cone, and where it goes

c = Clip(START, seed=41)
steps = c.steps


def drag(points):
    steps.append({"do": "drag", "points": [[round(x, 1), round(y, 1)] for x, y in points]})
    c.pos = list(points[-1])


def ring(center, a0, a1, n=45):
    """Grab the view-facing rotation ring at angle a0 (degrees, screen) and turn it to a1 (the 45 degree
    rotation snap pulls it to a step)."""
    p = lambda a: [center[0] + RING_R * math.cos(math.radians(a)), center[1] + RING_R * math.sin(math.radians(a))]
    c.go(p(a0)); c.wait(15)
    drag([p(a0), p(a0)] + [p(a0 + (a1 - a0) * min_jerk(i / n)) for i in range(1, n + 1)] + [p(a1)] * 4)


def mode_taps():
    """Taps on the gizmo mode button (All -> Move -> Rotate -> Scale) that bring it to Move."""
    q = [{"do": "find", "id": MODE}]
    out = subprocess.run([sys.executable, AI_PY, "send", json.dumps(q)], capture_output=True, text=True).stdout
    order = ["All", "Move", "Rotate", "Scale"]
    line = next((l for l in out.splitlines() if l.strip().startswith(f"{MODE} button")), "")
    cur = next((m for m in order if f"'{m}'" in line), "Move")
    return (1 - order.index(cur)) % 4


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
    steps.append({"do": "set", "id": CAMERA_MENU, "value": True})
    steps.append({"do": "click", "id": PERSPECTIVE})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": True})
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "id": CONE})
    steps.append({"do": "set", "id": SCENE, "value": False})
    # the horn: tilted 30 degrees to the right, its base sunk a little in the sphere (radius 0.42)
    steps.append({"do": "set", "id": TRANSFORM_MENU, "value": True})
    steps.append({"do": "set", "id": SCALE, "value": 0.45})
    steps.append({"do": "set", "id": TX, "value": 0.3075})
    steps.append({"do": "set", "id": TY, "value": 0.533})
    steps.append({"do": "set", "id": TZ, "value": 0.0})
    steps.append({"do": "set", "id": RZ, "value": -30})
    steps.append({"do": "set", "id": TRANSFORM_MENU, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))
    c.wait(5)
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 5000})
    c.wait(5)
    steps.append({"do": "set", "id": GIZMO, "value": True})
    c.wait(5)
    # slimmer: the base radius handle a third of the way to the base center (shown with the primitive)
    # (a press then release on the handle opens its numeric input: drag straight from it)
    a, b = BASE_RADIUS
    steps.append({"do": "drag", "points": [[a[0] - 40, a[1] - 20], [a[0] - 10, a[1] - 5], a, a], "hover": True})
    drag([a, a] + [[a[0] + (b[0] - a[0]) * i / 12, a[1] + (b[1] - a[1]) * i / 12] for i in range(1, 13)] + [b])
    c.wait(5)
    steps.append({"do": "click", "text": "Validate"})
    c.wait(10)
    steps.append({"do": "set", "id": PIVOT, "value": False})   # the toggle outlives a new scene
    for _ in range(mode_taps()):
        c.tap(MODE_AT, 2); c.wait(5)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "find", "id": MODE})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_gizmo"})
    c.wait(30)
    c.click(MODE_AT, hold=2); c.wait(20)          # Move -> Rotate: only the rotation rings
    ring(CENTER, 150, 105); c.wait(45)            # turns on its middle: the base lifts off the head
    c.click(UNDO_AT, hold=2); c.wait(25)
    c.click(PIVOT_AT, hold=2); c.wait(15)         # Pivot on: the gizmo moves, not the horn
    c.click(BASE_AT, hold=2); c.wait(40)          # tap the base: the pivot jumps onto the surface
    c.click(PIVOT_AT, hold=2); c.wait(15)         # Pivot off
    ring(BASE_CENTER, 150, 105); c.wait(45)       # the same turn now swings it from its base
    c.click(PIVOT_MENU_AT, hold=2); c.wait(30)    # Pivot popup: Auto puts it back in the middle
    c.click(AUTO_AT, hold=2); c.wait(30)
    c.click(POPUP_CLOSE, hold=2); c.wait(20)
    c.go(START); c.wait(10)
    c.camera(200, yaw=[(0.5, 35), (1, 25)], pitch=[(0.5, 10), (1, 6)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
