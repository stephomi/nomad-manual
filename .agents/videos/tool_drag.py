#!/usr/bin/env python3
"""docs/videos/tool_drag.mp4: DynTopo turned on in the Topology menu, Drag picked in the toolbox, then
long winding strokes pull snake-like limbs out of a sphere; a look around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_drag.py setup | python3 ../nomad/.agents/ai.py send -
    tool_drag.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import math
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX = 58936
CLAY, DRAG = 67742, 67745
SYM, RADIUS = 56799, 56725
TOPO, TOPO_AT = 6399, [175, 25]
DYN_ENABLED_AT = [370, 333]           # DynTopo tab, `Enabled` checkbox
DRAG_AT = [1170, 286]
WINDOW = [1200, 900]
START = [1010, 640]
REST = [1085, 760]                    # parked for the look around, away from the model
HOME_Z = 1.758320689201355            # camera distance of a new scene (pivot at the origin)

c = Clip(START)
steps = c.steps


def post_process():
    """A new scene has the post process off: only the render resolution to set."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})


def pick(p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
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


def snake(way, n):
    """One winding drag through the waypoints, eased at both ends."""
    c.go(way[0]); c.wait(12)
    pts = [[round(v, 1) for v in catmull(way, min_jerk(i / n))] for i in range(n + 1)]
    steps.append({"do": "drag", "points": pts})
    c.pos = list(way[-1])
    c.wait(20)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    post_process()
    # DynTopo would warn that the multires levels get lost: drop them now, leave the menu on DynTopo
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "text": "Multires", "type": "radio_option"})
    steps.append({"do": "click", "text": "Delete lower"})
    steps.append({"do": "click", "text": "DynTopo", "type": "radio_option"})
    steps.append({"do": "set", "id": TOPO, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": DRAG, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 70})
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Drag itself
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_drag"})
    c.wait(25)
    c.click(TOPO_AT); c.wait(10)       # Topology, on its DynTopo tab
    c.click(DYN_ENABLED_AT); c.wait(15)
    c.click(TOPO_AT)                   # close
    pick(DRAG_AT)
    snake([[790, 400], [880, 360], [930, 430], [1010, 400], [1050, 300], [1010, 230]], 130)
    snake([[420, 520], [330, 560], [270, 490], [190, 520], [150, 620], [200, 700]], 130)
    snake([[640, 230], [660, 150], [740, 120], [800, 160]], 90)
    snake([[560, 660], [540, 740], [600, 790], [700, 780]], 90)
    c.go(REST); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": [0, 0, 0], "translation": [0, 0, HOME_Z]})
    c.camera(220, yaw=[(0.5, -45), (0.85, -15), (1, -18)], pitch=[(0.45, 15), (1, 6)],
             dolly=[(0.5, 1.05), (1, 1.05)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
