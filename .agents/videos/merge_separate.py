#!/usr/bin/env python3
"""docs/videos/merge_separate.mp4: a sphere and a torus, apart. Both are checked in the Scene list and
joined (Join): the gizmo lifts them together, one object. Split… > Split by Parts makes them two again:
the torus alone is selected and pulled down with the gizmo. See .agents/videos.md.

    merge_separate.py setup | python3 ../../.agents/ai.py send -
    merge_separate.py record [name] | python3 ../../.agents/ai.py send - 900
The Dracula project only lends its background and lights: its meshes are deleted. dracula.load() turns
its post process off (as a new user sees the viewport) and sets the exposure shared by the clips on
that project. The gizmo drags and camera steps of the setup are a chain (each depends on the view the
previous one left): keep them together. Widget ids are the 2026-11-19 build's (check them with `find`
after a rebuild)."""
import sys

from clip import Clip
import dracula

SCENE = 3326
LIGHTS, CAMERAS, ADD, DELETE, QUAD_SPHERE, CLAY = 4059, 4060, 3911, 3912, 3447, 67742
ROW = lambda i: [209, 312 + 80 * i]          # Scene list rows: Lights group, Light, sphere, torus
CHECK = lambda i: [310, 352 + 80 * i]        # their selection checkboxes
WINDOW = [1200, 900]
SCENE_AT = [125, 25]
JOIN_AT, SPLIT_AT = [305, 122], [375, 122]
BY_PARTS_AT = [301, 234]
JOINED_UP = [700, 290]                       # gizmo Y arrow of the joined object
TORUS_UP = [853, 212]                        # gizmo Y arrow of the torus, once split and lifted
START = [1010, 640]


def line(a, b, n=30):
    return [[round(a[0] + (b[0] - a[0]) * i / n, 1), round(a[1] + (b[1] - a[1]) * i / n, 1)] for i in range(n + 1)]


c = Clip(START, seed=31)
steps = c.steps

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    dracula.load(steps)
    steps.append({"do": "click", "id": SCENE})
    for _ in range(5):                               # delete Dracula's meshes, keep its lights
        c.tap(ROW(0))
        steps.append({"do": "click", "id": DELETE})
    steps.append({"do": "set", "id": LIGHTS, "value": False})
    steps.append({"do": "set", "id": CAMERAS, "value": False})
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "id": QUAD_SPHERE})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "click", "text": "Validate"})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "text": "Torus", "type": "button"})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "click", "text": "Validate"})
    # the torus moves out to the right with the gizmo (X arrow), in two drags
    steps.append({"do": "set", "id": CLAY, "value": True})  # tool_gizmo toggles back when Gizmo is active
    steps.append({"do": "action", "name": "tool_gizmo"})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(30)
    # (y 450: the viewport center of a 1200x900 window. On the arrow head, not its tip: a press that
    # misses it grabs the screen ring and scales the torus)
    steps.append({"do": "drag", "points": line([750, 450], [1170, 450])})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(30)
    steps.append({"do": "camera", "orbit": [0, 22]})
    steps.append({"do": "drag", "points": line([893, 450], [1033, 450])})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(30)
    steps.append({"do": "camera", "orbit": [0, 22], "pan": [-0.18, 0], "dolly": 1.05})
    steps.append({"do": "camera", "dolly": 1.25, "pan": [0.05, 0]})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(100)                                      # let the "Reset view" toast fade
    steps.append({"do": "stats"})                    # Torus box ~ 0.83,-0.1,-0.6 2.03,0.1,0.6
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "merge_separate"})
    c.wait(30)                                       # two objects, the torus selected
    c.click(SCENE_AT); c.wait(10)
    c.click(CHECK(2)); c.wait(20)                    # check the sphere too: both highlighted
    c.click(JOIN_AT); c.wait(30)                     # Join: one object
    c.click(SCENE_AT)
    c.go(JOINED_UP); c.wait(12)                      # the gizmo lifts both together
    c.stroke(JOINED_UP, [JOINED_UP[0], JOINED_UP[1] - 90], 45, bow=0); c.wait(30)
    c.click(SCENE_AT); c.wait(10)
    c.click(SPLIT_AT); c.wait(10)
    c.click(BY_PARTS_AT); c.wait(30)                 # Split by Parts: two objects again
    c.click(ROW(3)); c.wait(20)                      # select the torus alone
    c.click(SCENE_AT)
    c.go(TORUS_UP); c.wait(12)                       # and pull it down, away from the sphere
    c.stroke(TORUS_UP, [TORUS_UP[0], TORUS_UP[1] + 190], 55, bow=0); c.wait(40)
    c.go(START); c.wait(30)
    steps.append({"do": "record"})
print(c.json())
