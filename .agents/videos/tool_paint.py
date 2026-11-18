#!/usr/bin/env python3
"""docs/videos/tool_paint.mp4: Paint on the boring head, symmetry on. Paint is picked in the toolbox; in
the Paint menu the color row opens the picker: blue; stripes on one cheek come out on both. Back in the
menu, red: the lips. `Erase` (the sub mode) rubs out the end of a stripe, mirrored too. Post process off
and the scene brightened: boringhead.py. See .agents/videos.md.

    AI_SESSION=<s> tool_paint.py setup | AI_SESSION=<s> python3 ../../.agents/ai.py send -
    tool_paint.py record [name] | python3 ../../.agents/ai.py send - 900
Setup asks the running Nomad (AI_SESSION, AI_PY: that session's ai.py) whether Paint shows its stroke
types as a list or as one button (a saved per-tool setting) and switches to the list the clip was laid
out with: its slider column shifts the menus right.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import json
import os
import subprocess
import sys

from boringhead import PROJECT, look
from clip import Clip, min_jerk

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../.agents/ai.py"))

TOOLBOX, CLAY, PAINT = 58936, 67742, 67749
SYM, SUB, PAINT_MENU, LAYOUT, STROKES = 56799, 57353, 23086, 54629, 48750
WINDOW = [1200, 885]                         # what macOS clamped [1200, 900] to when the clip was written
START = [1010, 700]
PAINT_AT = [1170, 540]                       # toolbox, scrolled to the top
MENU_AT = [875, 25]                          # top bar: Paint menu
COLOR_ROW = [900, 498]                       # Paint menu: the color row opens the picker
HUE_X, SQUARE_CORNER, PICKER_CLOSE = 1038, [1004, 602], [1058, 502]
BLUE_Y, RED_Y = 680, 596                     # on the hue bar
ERASE_AT = [25, 477.5]                       # the Sub button's exact center: Erase

c = Clip(START, seed=51)
steps = c.steps


def list_layout():
    """Steps that switch Paint's stroke types to the list layout, if Nomad shows them as one button."""
    q = [{"do": "scroll", "id": TOOLBOX, "to": 0}, {"do": "set", "id": PAINT, "value": True},
         {"do": "find", "in": STROKES, "type": "button"}]
    out = subprocess.run([sys.executable, AI_PY, "send", json.dumps(q)], capture_output=True, text=True).stdout
    return [] if out.count('icon="shape_') > 1 else [{"do": "click", "id": LAYOUT}]


def press(p, widget, value):
    """A sticky button (a tool, a left toolbar shortcut) turned on or off for sure: a held press only
    borrows it until release, and a recorded press lasts longer in wall-clock time when the frames are
    slow (a painted scene, other sessions recording). Glide onto the button's center, then `set` it
    there: the click by id lands where the pointer already is."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    steps.append({"do": "set", "id": widget, "value": value})
    c.wait(22)


def glide(t):
    """A paint stroke: barely eased. Within 7 px of its start for 0.5 s it is a long press (Paint picks the
    color under the pointer), within 7 px of its end for 0.7 s it snaps into a curve, and a painted frame
    takes up to 0.1 s to record."""
    return 0.8 * t + 0.2 * min_jerk(t)


def stroke(a, b, n=30, bow=0.08, rest=15):
    c.go(a); c.wait(8)
    steps.append({"do": "drag", "points": c.path(a, b, n, bow, glide)})
    c.pos = list(b)
    c.wait(rest)


def color(hue_y):
    """Paint menu > color row > picker: the hue, then the saturated corner of the square; close it all."""
    qclick(MENU_AT)
    qclick(COLOR_ROW)
    a = [HUE_X, 620]
    c.go(a); c.wait(10)
    steps.append({"do": "drag", "points": [a, a] + [[HUE_X, round(a[1] + (hue_y - a[1]) * min_jerk(i / 20), 1)]
                                                    for i in range(1, 21)] + [[HUE_X, hue_y]] * 3})
    c.pos = [HUE_X, hue_y]; c.wait(8)
    qclick(SQUARE_CORNER)
    qclick(MENU_AT)                                   # closes the picker with the menu


def qclick(p):
    """A click in a run of clicks inside a menu: shorter rests than Clip.click(), the hand already there."""
    c.go(p); c.wait(c.rng.randint(11, 14))
    c.tap(p, 2)
    c.wait(14)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(20)
    steps.extend(look())
    steps.append({"do": "camera", "pivot": [0, -0.05, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 2.7]})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": PAINT, "value": True})
    # the stroke types as a list (the two-squares toggle): its sliders have no label and other ids than
    # the compact layout's, their icon names find them in both
    steps.extend(list_layout())
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 22})
    steps.append({"do": "set", "text": "intensity.png", "type": "slider", "value": 1})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": SYM, "value": True})
    steps.append({"do": "set", "id": CLAY, "value": True})   # the clip picks Paint itself
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 80})  # Clay's ring at rest
    steps.append({"do": "drag", "points": [[1100, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_paint"})
    c.wait(30)
    press(PAINT_AT, PAINT, True)
    color(BLUE_Y)                                         # blue
    stroke([455, 232], [578, 266], 34)                    # stripes on the forehead, mirrored
    stroke([447, 292], [574, 318], 34)
    stroke([445, 540], [472, 598], 26, bow=-0.1)          # and under the eye
    color(RED_Y)                                          # red
    stroke([495, 628], [598, 640], 30, bow=-0.05, rest=25)   # the lips
    press(ERASE_AT, SUB, True)                            # Erase: cut the stripes' ends
    stroke([478, 205], [482, 335], 34, bow=0.03, rest=25)
    press(ERASE_AT, SUB, False)
    c.go(START); c.wait(10)
    c.camera(200, yaw=[(0.5, 30), (1, 18)], pitch=[(0.5, 6), (1, 3)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
