#!/usr/bin/env python3
"""docs/videos/tool_crease.mp4: Crease picked in the toolbox, two winding strokes cut sharp creases into a
sphere, `Invert` on the left toolbar (the sub mode) draws a third one as a raised ridge; a short look
around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_crease.py setup | python3 ../nomad/.agents/ai.py send -
    tool_crease.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
CAMERA, FOV = 17912, 17914
TOPO, MULTIRES, SUBDIVIDE = 6399, 67820, 6482
TOOLBOX, TOOLBOX_SCROLL = 58936, 200  # Crease is below the fold of a 885 px high window
CLAY, CREASE, CREASE_AT = 67742, 67754, [1170, 658]
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
SUB, SUB_AT = 57353, [25, 477]        # the same button, labelled `Invert` for Crease
WINDOW = [1200, 900]
START = [1010, 640]
REST = [1050, 770]                    # parked for the look around, away from the model
HOME_Z = 2.956                        # a new scene is at 3.359: a little closer, the sphere fills the view

c = Clip(START)
steps = c.steps


def new_scene():
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    # a new scene has the post process off: only the render resolution to set
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": CAMERA, "value": True})  # HOME_Z frames the sphere for this field of view
    steps.append({"do": "set", "id": FOV, "value": 25})
    steps.append({"do": "set", "id": CAMERA, "value": False})
    steps.append({"do": "camera", "pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, HOME_Z]})
    # one more level (393k): a crease needs polygons to stay sharp
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": MULTIRES})
    steps.append({"do": "click", "id": SUBDIVIDE})
    steps.append({"do": "set", "id": TOPO, "value": False})


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


def wave(way, n):
    """One winding drag through the waypoints, eased at both ends."""
    c.go(way[0]); c.wait(12)
    pts = [[round(v, 1) for v in catmull(way, min_jerk(i / n))] for i in range(n + 1)]
    steps.append({"do": "drag", "points": pts})
    c.pos = list(way[-1])
    c.wait(18)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    new_scene()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Crease itself
    steps.append({"do": "set", "id": SUB, "value": False})  # each tool keeps its own, a new scene too
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": CREASE, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 50})
    steps.append({"do": "set", "id": INTENSITY, "value": 0.8})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_crease"})
    c.wait(25)
    pick(CREASE_AT)
    wave([[420, 290], [470, 370], [400, 450], [470, 530], [430, 610]], 85)              # two creases
    wave([[620, 680], [590, 600], [650, 500], [570, 400], [650, 300], [600, 200]], 100)
    c.click(SUB_AT, hold=1)                      # Invert: a raised crease
    wave([[780, 290], [730, 370], [800, 450], [730, 530], [770, 610]], 85)
    c.go(REST); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": [0, 0, 0], "translation": [0, 0, HOME_Z]})
    c.camera(170, yaw=[(0.5, 30), (1, 18)], pitch=[(0.5, 12), (1, 7)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
