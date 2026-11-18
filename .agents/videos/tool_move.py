#!/usr/bin/env python3
"""docs/videos/tool_move.mp4: Move picked in the toolbox, two ears and a chin pulled out of a sphere,
then a pull that comes back to where it started leaves no trace; a look around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_move.py setup | python3 ../../.agents/ai.py send -
    tool_move.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX = 58936
MOVE, MOVE_AT = 67744, [1170, 222]
CLAY = 67742
SYM, RADIUS = 56799, 56725
WINDOW = [1200, 900]
START = [1010, 640]                   # resting pointer, background right of the sphere
REST = [1085, 760]                    # parked for the look around: Move's background ring stays off the sphere
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


def pull(a, b, n, bow=0.05, back=False):
    """Glide to a, rest, drag to b (and back to a with `back`)."""
    c.go(a); c.wait(12)
    if back:  # one press: out, held (the bump stays while the pointer is away), back to the start
        pts = c.path(a, b, n, bow, min_jerk) + [b] * 25 + c.path(b, a, n, bow, min_jerk)[1:]
        steps.append({"do": "drag", "points": pts})
    else:
        c.stroke(a, b, n, bow)
    c.wait(25)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    post_process()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": MOVE, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 110})
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Move itself
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_move"})
    c.wait(30)
    pick(MOVE_AT)
    pull([705, 285], [800, 150], 55)                 # right ear
    pull([495, 285], [400, 150], 55, bow=-0.05)      # left ear
    pull([600, 650], [600, 780], 50)                 # chin
    pull([770, 480], [930, 560], 45, back=True)      # out and back: nothing left
    c.go(REST); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": [0, 0, 0], "translation": [0, 0, HOME_Z]})
    c.camera(220, yaw=[(0.5, -40), (0.85, -8), (1, -10)], pitch=[(0.45, 12), (1, 4)],
             dolly=[(0.5, 0.92), (1, 0.95)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
