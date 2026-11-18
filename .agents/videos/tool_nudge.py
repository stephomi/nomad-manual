#!/usr/bin/env python3
"""docs/videos/tool_nudge.mp4: Nudge picked in the toolbox; a first curved stroke smears the surface of a
sphere along its path. `Wireframe` turned on in the bottom bar: two more strokes show the topology sliding
with the brush. A short look around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_nudge.py setup | python3 ../../.agents/ai.py send -
    tool_nudge.py record [name] | python3 ../../.agents/ai.py send - 900
The record steps end by turning the wireframe back off (the sandbox settings are shared).
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
WIREFRAME, WIREFRAME_AT = 46039, [375, 858]
TOOLBOX, TOOLBOX_SCROLL = 58936, 600
CLAY, NUDGE, NUDGE_AT = 67742, 67761, [1170, 708]
SYM, RADIUS, INTENSITY, SUB = 56799, 56725, 56745, 57353
# a new scene's view (pivot at the origin, 25° FoV), turned a little
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 3.35921049118042]}
VIEW = [-25, 12]
WINDOW = [1200, 900]
START = [1010, 640]
REST = [1085, 760]

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
    c.tap(p, 3)
    c.wait(20)


def catmull(pts, u):
    """Point at u (0..1) on a Catmull-Rom curve through pts."""
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def smear(way, n):
    """One stroke through the waypoints, eased at both ends."""
    c.go(way[0]); c.wait(10)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(way, min_jerk(i / n))] for i in range(n + 1)]})
    c.pos = list(way[-1])
    c.wait(22)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    post_process()
    steps.append({"do": "set", "id": WIREFRAME, "value": False})  # the clip turns it on itself
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": NUDGE, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 90})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "set", "id": SUB, "value": False})  # Fold
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Nudge itself
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "orbit": VIEW})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_nudge"})
    c.wait(25)
    pick(NUDGE_AT)
    smear([[470, 330], [560, 300], [650, 340], [700, 430]], 85)     # the surface follows the stroke
    # Wireframe: the topology slides. A short press, as a held one opens the button's options popup
    # (recording slows the frames down: the 8 frames of Clip.click() are a long press)
    pick(WIREFRAME_AT)
    smear([[720, 560], [620, 600], [520, 560], [470, 470]], 85)
    smear([[600, 430], [600, 550], [610, 670]], 65)
    c.go(REST); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": HOME["pivot"], "translation": HOME["translation"]})
    c.camera(170, yaw=[(0.5, 32), (0.85, 12), (1, 14)], pitch=[(0.45, -10), (1, -5)],
             dolly=[(0.5, 0.95), (1, 0.97)])
    c.wait(25)
    steps.append({"do": "record"})
    steps.append({"do": "set", "id": WIREFRAME, "value": False})
print(c.json())
