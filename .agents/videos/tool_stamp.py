#!/usr/bin/env python3
"""docs/videos/tool_stamp.mp4: Stamp picked in the toolbox, a cross alpha (screw-head like) stamped on a
box with `Lock + radius` (each drag sets size and rotation), then `Lock + intensity` picked in the Stroke
menu (the drag sets height and rotation, the size stays); a look around. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_stamp.py setup | python3 ../../.agents/ai.py send -
    tool_stamp.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild. The alpha library popup
opens next to the thumbnail tap (it was once seen elsewhere, at 507,36, on its first opening): after
setup, check in the Stroke menu's Alpha tab that the cross is the Stamp alpha before recording."""
import sys

from clip import Clip

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX, TOOLBOX_SCROLL = 58936, 600
CLAY, STAMP, STAMP_AT = 67742, 67762, [1170, 772]
SYM, RADIUS = 56799, 56725
STROKE, STROKE_AT = 19331, [825, 25]
ALPHA_THUMB_AT = [887, 310]
ALPHA_LIBRARY, CROSS_SCROLL, CROSS_AT = 20025, 1180, [1110, 692]  # last cell of Kenney/Base
ALPHA_SCALING = 21325
LOCK_INTENSITY_AT = [1042, 540]
X_DIV, VALIDATE = 62297, 63231
HOME = {"pivot": [0, 0, 0], "translation": [0, 0, 1.758320689201355]}
VIEW = dict(HOME, rotation=[0.18514118, -0.23747711, -0.04616088, 0.95246869])
WINDOW = [1200, 900]
START = [1010, 700]

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


def stamp(p, d, n=30):
    """Press at p and drag by d: the stamp grows (or rises) and turns with the drag."""
    c.go(p); c.wait(10)
    c.tap(p, 3)  # press, held a moment before the drag starts
    steps[-1]["points"] += c.path(p, [p[0] + d[0], p[1] + d[1]], n, 0.0, lambda t: t * t * (3 - 2 * t))[1:]
    c.pos = [p[0] + d[0], p[1] + d[1]]
    c.wait(16)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    steps.append({"do": "action", "name": "delete"})  # the new scene's sphere: a box suits stamps
    steps.append({"do": "action", "name": "add_box"})
    c.wait(5)
    steps.append({"do": "set", "id": X_DIV, "value": 300})  # stamps need dense faces
    c.wait(5)
    steps.append({"do": "click", "id": VALIDATE})
    c.wait(5)
    steps.append(dict({"do": "camera"}, **VIEW))
    post_process()
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": STAMP, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 120})
    # the cross alpha, picked in the Stroke menu's Alpha tab; leave the menu on its Stroke tab
    steps.append({"do": "set", "id": STROKE, "value": True})
    c.wait(5)
    steps.append({"do": "click", "text": "Alpha", "type": "radio_option"})
    c.wait(5)
    steps.append({"do": "set", "id": ALPHA_SCALING, "value": 1})  # the arms' tips round off in the brush
    c.tap(ALPHA_THUMB_AT, 1)                                    # the thumbnail opens the library
    c.wait(10)
    steps.append({"do": "scroll", "id": ALPHA_LIBRARY, "to": CROSS_SCROLL})
    c.wait(20)
    c.tap(CROSS_AT, 1)
    c.wait(10)
    steps.append({"do": "set", "id": STROKE, "value": False})
    c.wait(5)
    steps.append({"do": "set", "id": STROKE, "value": True})
    c.wait(5)
    steps.append({"do": "click", "text": "Stroke", "type": "radio_option"})
    c.wait(5)
    steps.append({"do": "click", "text": "Lock + radius"})
    steps.append({"do": "set", "id": STROKE, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Stamp itself
    steps.append({"do": "scroll", "id": TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_stamp"})
    c.wait(25)
    pick(STAMP_AT)
    stamp([400, 370], [55, -30])                  # Lock + radius: the drag sets size and turn
    stamp([610, 420], [35, 40])
    stamp([420, 620], [80, 15])
    c.click(STROKE_AT)                            # Stroke menu
    c.click(LOCK_INTENSITY_AT)
    c.click(STROKE_AT)
    stamp([620, 650], [10, -55])                  # Lock + intensity: same size, the drag sets height
    stamp([520, 500], [-25, -30])
    c.go(START); c.wait(10)
    steps.append(dict({"do": "camera"}, **VIEW))  # strokes moved the orbit pivot: back on the box center
    c.camera(170, yaw=[(0.55, 24), (1, 18)], pitch=[(0.5, -8), (1, -5)])
    c.wait(25)
    steps.append({"do": "record"})
print(c.json())
