#!/usr/bin/env python3
"""docs/videos/connected_topology.mp4: a C-shaped tube whose two tips almost touch. Move on one tip
drags the other along; undo, Filter > Connected topology, the same move only takes the touched tip.
See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    connected_topology.py setup | python3 ../../.agents/ai.py send -
    connected_topology.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. The scene is built in
setup: a new scene, its sphere deleted, the C drawn with the Tube tool."""
import math
import sys

from clip import Clip

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
MENUS = [108, 3326, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331, 27845]
SYM, RADIUS = 56799, 56725
CONNECTED = 21816                     # Filter tab of the stroke menu
WINDOW = [1200, 900]

STROKE_MENU_AT = [825, 25]            # the top bar's stroke menu, opens on its Filter tab
CONNECTED_AT = [1100, 311]
UNDO_AT = [25, 858]
START = [1000, 700]                   # resting pointer, background right of the C
PAN = 0.25
TIP, PULL = [606, 428], [770, 410]    # the upper tip, pulled out to the right

c = Clip(START, seed=13)
steps = c.steps


def post_process():
    """A new scene has the post process off: only the render resolution to set."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})


def line(a, b, n=20):
    return [[round(a[0] + (b[0] - a[0]) * i / n, 1), round(a[1] + (b[1] - a[1]) * i / n, 1)] for i in range(n + 1)]


def tube():
    """The C: an arc drawn with the Tube tool, its end points pulled closer, validated."""
    steps.append({"do": "action", "name": "tool_tube"})
    c.wait(5)
    arc = []
    for i in range(121):
        a = math.radians(8 + 344 * i / 120)
        arc.append([round(580 + 230 * math.cos(a), 1), round(450 - 230 * math.sin(a), 1)])
    steps.append({"do": "drag", "points": arc})
    c.wait(10)
    steps.append({"do": "drag", "points": [[808, 415]] * 3 + line([808, 415], [812, 444])})
    c.wait(5)
    steps.append({"do": "drag", "points": [[800, 511]] * 3 + line([800, 511], [806, 486])})
    c.wait(5)
    steps.append({"do": "click", "text": "Validate", "type": "button"})
    c.wait(10)


def move(a, b):
    c.go(a); c.wait(15)
    c.stroke(a, b, 55, bow=0.05)
    c.wait(40)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    for i in MENUS:  # with the new sphere selected: with nothing, some menu buttons are disabled
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "id": SYM, "value": False})  # (its button needs a mesh)
    steps.append({"do": "action", "name": "delete"})  # the new scene's sphere: only the C is shown
    post_process()
    tube()
    steps.append({"do": "action", "name": "tool_move"})
    steps.append({"do": "set", "id": RADIUS, "value": 150})  # reaches the other tip
    steps.append({"do": "action", "name": "menu_filter"})
    c.wait(3)
    # on by default for Move. Not a `set`: it clicks the widget's center, where the help button sits.
    # The tap toggles, so the setup expects it on (a fresh session, or the end of the last take).
    c.tap(CONNECTED_AT); c.wait(3)
    steps.append({"do": "action", "name": "menu_filter"})
    steps.append({"do": "camera", "pan": [PAN, 0], "frames": 1})  # the C left of the menu
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(30)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "connected_topology"})
    c.wait(40)
    move(TIP, PULL)                   # both tips follow
    c.click(UNDO_AT); c.wait(15)
    c.click(STROKE_MENU_AT)
    c.click(CONNECTED_AT); c.wait(15) # Connected topology
    c.click(STROKE_MENU_AT)
    move(TIP, PULL)                   # only the touched tip
    c.go(START); c.wait(40)
    steps.append({"do": "record"})
print(c.json())
