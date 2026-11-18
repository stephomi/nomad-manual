#!/usr/bin/env python3
"""docs/videos/hole_filling.mp4: the boring head with a round hole in its skull (cut in setup: Hide
lasso, then the hide_remove action); Topology > Misc > Holes > Close holes fills it with a smooth
patch. Post process off and the scene brightened: boringhead.py. See .agents/videos.md.

    hole_filling.py setup | python3 ../../.agents/ai.py send -
    hole_filling.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import json
import math
import sys

from boringhead import PROJECT, look
from clip import Clip

SCENE, TOPO = 3326, 6399
CLAY, SYM, LIGHTS, CAMERAS, MIRRORS = 67742, 56799, 4059, 4060, 4058
MISC_TAB = 67823
WINDOW = [1200, 885]                  # what macOS clamped [1200, 900] to when the clip was written
RADIUS = 56725
TOPO_AT = [175, 25]
CLOSE_HOLES_AT = [235, 380]
START = [1010, 640]


c = Clip(START, seed=11)
steps = c.steps

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    steps.extend(look())
    steps.append({"do": "click", "id": SCENE})
    for i in (LIGHTS, CAMERAS, MIRRORS):           # no gizmos in the viewport
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(30)
    steps.append({"do": "action", "name": "view_focus"})
    c.wait(30)
    steps.append({"do": "camera", "orbit": [-35, 25]})
    # the hole: a lasso with the Hide tool on the side of the skull, then remove the hidden faces
    steps.append({"do": "action", "name": "tool_hide"})
    c.wait(5)
    lasso = [[round(610 + 60 * math.cos(2 * math.pi * i / 40), 1), round(250 + 50 * math.sin(2 * math.pi * i / 40), 1)]
             for i in range(41)]
    steps.append({"do": "drag", "points": lasso})
    steps.append({"do": "action", "name": "hide_remove"})
    steps.append({"do": "camera", "dolly": 0.8, "pan": [0, 0.04]})  # closer, the hole well in view
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 45})  # the ring at rest: other takes leave Clay's radius
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "click", "id": MISC_TAB})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "hole_filling"})
    c.wait(30)
    c.camera(100, yaw=[(1, 12)], pitch=[(1, 6)])   # a look into the hole
    c.wait(10)
    c.click(TOPO_AT); c.wait(15)                    # Topology > Misc > Holes
    c.click(CLOSE_HOLES_AT); c.wait(50)
    c.click(TOPO_AT)
    c.go(START); c.wait(10)
    c.camera(130, yaw=[(0.6, -22), (1, -18)], pitch=[(0.6, -8), (1, -6)])
    c.wait(30)
    steps.append({"do": "record"})
print(json.dumps(steps))
