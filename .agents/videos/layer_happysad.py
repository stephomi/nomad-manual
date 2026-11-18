#!/usr/bin/env python3
"""docs/videos/layer_happysad.mp4: the boring head's smile is a layer. Layers > the smile layer's More
popup > Settings: dragging its Offset channel factor below zero turns the smile into a frown.
Post process off and the scene brightened: boringhead.py. See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    layer_happysad.py setup | python3 ../../.agents/ai.py send -
    layer_happysad.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. The layer rows get new
ids on each load, so the clip clicks them by position."""
import sys

from boringhead import PROJECT, look
from clip import Clip, min_jerk

SCENE = 3326
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, RADIUS = 56799, 56725
WINDOW = [1200, 885]                  # what macOS clamped [1200, 900] to when the clip was written
LAYERS_AT = [1025, 25]
MORE_AT = [1115, 332]                 # More button of the active (smile) layer
OFFSET_Y = 504                        # Offset row of the More popup, Settings tab
CLOSE_AT = [1096, 347]                # the popup's cross
VALUE_AT = [987, 504]                 # Offset's value: opens an input box
OK_AT = [1050, 622]                   # its Ok button
START = [1010, -30]                   # above the window: the pointer comes in over the top bar

c = Clip(START)
steps = c.steps


MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]                       # top bar buttons: menus stay open across a project load


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
    steps.append({"do": "set", "id": RADIUS, "value": 4})  # no sculpting here: the ring shows over the top bar


def slide(x0, x1, n):
    """Drag the Offset slider (a relative one: ~0.26% per point) from x0 to x1."""
    c.go([x0, OFFSET_Y]); c.wait(14)
    c.steps.append({"do": "drag", "points": [[round(x0 + (x1 - x0) * min_jerk(i / n), 1), OFFSET_Y]
                                             for i in range(n + 1)]})
    c.pos = [x1, OFFSET_Y]


def prime_input_box():
    """The input box opens in the middle of the window the first time in a session, next to its slider
    from then on (where OK_AT is): open it once and cancel."""
    steps.append({"do": "set", "id": MENUS[10], "value": True})  # Layers
    c.wait(10)
    for p in (MORE_AT, VALUE_AT):
        c.tap(p, 2); c.wait(15)
    steps.append({"do": "click", "text": "Cancel"})  # by text: the box gets its ids when first opened
    c.wait(10)
    c.tap(CLOSE_AT, 2); c.wait(10)
    steps.append({"do": "set", "id": MENUS[10], "value": False})


if sys.argv[1] == "setup":
    prepare()
    prime_input_box()
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(20)
    steps.append({"do": "camera", "orbit": [-8, -3], "frames": 1})
    steps.append({"do": "camera", "dolly": 0.6, "frames": 1})
    steps.append({"do": "camera", "pan": [0.075, 0.04], "frames": 1})
    steps.append({"do": "drag", "points": [[1300, 880], [1300, -30], START], "hover": True})  # outside: no ring
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "layer_happysad"})
    c.wait(40)                         # the smile
    c.click(LAYERS_AT); c.wait(10)     # Layers: smile is the active layer
    c.click(MORE_AT); c.wait(20)       # its More popup, Settings tab: the channel factors
    slide(950, 790, 70); c.wait(30)    # Offset down to ~40%: the smile flattens
    slide(950, 790, 70); c.wait(30)    # ~16%
    c.click(VALUE_AT)                  # the value: type a negative one
    for ch in "-100":
        steps.append({"do": "type", "input": ch}); c.wait(c.rng.randint(8, 14))
    c.click(OK_AT); c.wait(70)         # -100%: a frown
    c.click(CLOSE_AT)
    c.click(LAYERS_AT)
    c.go([LAYERS_AT[0] + 30, -40]); c.wait(10)
    c.camera(200, yaw=[(0.5, 16), (1, 10)], pitch=[(0.5, 4), (1, 2)], dolly=[(0.5, 0.95), (1, 0.97)],
             pan_x=[(0.5, -0.03), (1, -0.02)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
