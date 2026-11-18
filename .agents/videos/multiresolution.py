#!/usr/bin/env python3
"""docs/videos/multiresolution.mp4: Dracula's head goes down to level 1, both ears are pulled with Move,
back up to level 4 the wrinkles follow the new shape. dracula.load() turns the project's post process
off (as a new user sees the viewport) and sets the exposure shared by the clips on that project.
See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    multiresolution.py setup | python3 ../../.agents/ai.py send -
    multiresolution.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's (stable across project loads): check them with `find` after a
rebuild. Pointer and camera moves come from clip.py."""
import sys

from clip import Clip
import dracula

SCENE, TOPO = 3326, 6399
MOVE, SYM = 67744, 56799
HEAD_ROW = [209, 471]                 # headhi in the Scene list
TOPO_AT = [175, 25]
TICK_Y = 382
TICKS = [80, 157, 235, 312, 390]      # multires slider levels 0..4 (a slider `set` doesn't change the level)
WINDOW = [1200, 900]                  # 4:3 like the manual's other clips
START = [1030, 620]                   # resting pointer, on the background right of the head
EAR_R, EAR_L = [840, 300], [374, 300]

c = Clip(START)
steps = c.steps


def topology():
    c.click(TOPO_AT)


def level(i):
    c.click([TICKS[i], TICK_Y])


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    dracula.load(steps)
    steps.append({"do": "click", "id": SCENE}); c.tap(HEAD_ROW); steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "click", "text": "Multires", "type": "radio_option"})
    for _ in range(4):  # the head is saved as one level: rebuild levels 0..3 below it
        steps.append({"do": "click", "text": "Reverse"})
    c.tap([TICKS[4], TICK_Y])
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "set", "id": MOVE, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(90)                        # the Topology button stays lit a moment: not in frame 0 (the poster)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "multiresolution"})
    c.wait(50)                        # the sculpt at its highest level
    topology(); c.wait(25)            # Topology > Multires: let the panel be read
    level(1); c.wait(60)              # down to level 1: the wrinkles are gone
    topology()                        # close the menu
    c.go(EAR_R); c.wait(15)           # right ear
    c.stroke(EAR_R, [EAR_R[0] + 120, 230], 60, bow=0.05); c.wait(20)
    c.go(EAR_L); c.wait(15)           # left ear
    c.stroke(EAR_L, [EAR_L[0] - 120, 230], 60, bow=-0.05); c.wait(25)
    topology(); c.wait(15)
    level(4); c.wait(80)              # back to the highest level: the details follow the new shape
    topology()
    c.go(START); c.wait(10)
    # one continuous look around: swing left while closing in a little, back past the front, settle
    # (pan +x moves the model left, +y down: they keep the head centered and its top in view)
    c.camera(260, yaw=[(0.45, -34), (0.82, 6), (1, 2)], pitch=[(0.4, 3), (0.85, -1), (1, 0)],
             dolly=[(0.5, 0.95), (1, 0.96)], pan_x=[(0.45, -0.12), (1, -0.01)], pan_y=[(0.5, 0.06), (1, 0)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
