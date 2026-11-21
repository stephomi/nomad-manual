#!/usr/bin/env python3
"""docs/videos/layers_details.mp4: close-up on the boring head's forehead, whose wrinkles are on the
"detail" layer. Clay strokes on the Base fill the wrinkles in; undo, Layers > Advanced > Keep top layers
details, the same strokes: the forehead is built up and the wrinkles stay on top.
Post process off and the scene brightened: boringhead.py. See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    layers_details.py setup | python3 ../nomad/.agents/ai.py send -
    layers_details.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import sys

from boringhead import PROJECT, look
from clip import Clip

MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]                       # top bar buttons: menus stay open across a project load
SCENE = 3326
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
LAYERS, BASE_ROW, ADVANCED, KEEP = 33760, 33814, 35704, 35706
CLAY = 67742
WINDOW = [1200, 885]                  # what macOS clamped [1200, 900] to when the clip was written
LAYERS_AT = [1025, 25]
ADVANCED_AT = [965, 432]              # with Base active
KEEP_AT = [1075, 514]                 # Keep top layers details, in the Advanced popup
YES_AT = [1100, 456]                  # Yes of its confirmation (not a panel: `find` doesn't list it)
UNDO_AT = [25, 858]
START = [1100, 760]                   # resting pointer, background right of the head
# a wide Clay stroke across the forehead wrinkles, and back
PASSES = [([250, 350], [820, 345]), ([820, 345], [250, 355])]

c = Clip(START, seed=3)
steps = c.steps


def prepare():
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    steps.extend(look())
    steps.append({"do": "click", "id": SCENE})
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": SYM, "value": False})


def clay():
    for a, b in PASSES:
        if c.pos != a:
            c.go(a)
        c.wait(8)
        c.stroke(a, b, 70, bow=0.02)
    c.wait(10)
    c.go(START, 50)


if sys.argv[1] == "setup":
    prepare()
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 130})
    steps.append({"do": "set", "id": INTENSITY, "value": 0.5})
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "click", "id": BASE_ROW})             # sculpt the base, under the detail layer
    steps.append({"do": "click", "id": ADVANCED})
    steps.append({"do": "set", "id": KEEP, "value": False})
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "camera", "pivot": [-0.0002, -0.3276, -0.0222], "translation": [0.0025, 0.3474, 1.4855],
                  "rotation": [-0.05214, -0.08704, 0.00456, 0.99483]})  # close on the forehead
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "layers_details"})
    c.wait(50)                         # the wrinkles, on their own layer; Base is active
    clay(); c.wait(50)                 # the forehead built up: the wrinkles are filled in
    c.click(UNDO_AT); c.wait(30)
    c.click(LAYERS_AT)
    c.click(ADVANCED_AT)
    c.click(KEEP_AT); c.wait(25)       # Keep top layers details: "Lock the top layers?"
    c.click(YES_AT)
    c.click(LAYERS_AT)
    clay(); c.wait(60)                 # same strokes: the wrinkles stay on top
    c.camera(160, yaw=[(0.5, -12), (1, -8)], pitch=[(0.5, -4), (1, -3)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
