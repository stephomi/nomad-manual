#!/usr/bin/env python3
"""docs/videos/triplanar.mp4: a Triplanar primitive (Scene > Add, done in setup) shaped with the Mask
tool on its back plane: the camera focuses the plane from the toolbar, a mask stroke adds horns
(symmetry mirrors it), Unmask carves eye holes; a look around, then Validate. See .agents/videos.md.

    triplanar.py setup | python3 ../../.agents/ai.py send -
    triplanar.py record [name] | python3 ../../.agents/ai.py send - 900
The viking project only lends its background: its objects are hidden, and its post process is turned
off (as a new user sees the viewport).
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import os
import sys

from clip import Clip

PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/viking.nom")
SCENE, POST, POST_PANEL = 3326, 13905, 13892
LIGHTS, CAMERAS, ADD, TRIPLANAR, RADIUS, UNMASK = 4059, 4060, 3911, 3457, 56725, 57353
POST_ON = 13907                              # the `Post Process` checkbox, above the effects
RENDER_RES = 13908
EYE = lambda i: [349, 352 + 80 * i]          # eye buttons of the Scene list rows
WINDOW = [1200, 900]
BACK_AT, VALIDATE_AT = [692, 122], [385, 122]   # primitive toolbar: focus the back plane, Validate
UNMASK_AT = [25, 477]                        # left toolbar toggle
START = [1010, 640]


def post_setup(steps):
    """Post process off (the project is saved with it on), render resolution x1."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "wait", "frames": 5})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "wait", "frames": 20})  # a top bar button reads as on a moment after its menu closes


c = Clip(START, seed=23)
steps = c.steps


def toggle(p):
    """Clip.click() holds the press 8 frames: on a left toolbar shortcut that is a hold (active only
    while pressed). A quick tap toggles it."""
    c.go(p)
    c.wait(c.rng.randint(17, 23))
    c.tap(p, 2)
    c.wait(20)

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    post_setup(steps)
    steps.append({"do": "click", "id": SCENE})
    for i in range(3):
        c.tap(EYE(i))                               # hide the viking
    steps.append({"do": "set", "id": LIGHTS, "value": False})
    steps.append({"do": "set", "id": CAMERAS, "value": False})
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "id": TRIPLANAR})  # selects the Mask tool, symmetry on
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": RADIUS, "value": 45})
    steps.append({"do": "set", "id": UNMASK, "value": False})  # the toggle outlives a project load
    steps.append({"do": "action", "name": "view_focus"})
    c.wait(30)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(30)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "triplanar"})
    c.wait(40)
    c.click(BACK_AT); c.wait(30)                    # face the back plane
    a = [780, 300]; c.go(a); c.wait(10)             # mask: horns (mirrored)
    c.stroke(a, [885, 180], 45, bow=0.1); c.wait(25)
    toggle(UNMASK_AT)                               # unmask: eye holes
    a = [505, 395]; c.go(a); c.wait(10)
    c.stroke(a, [525, 405], 20, bow=0.2); c.wait(25)
    toggle(UNMASK_AT)
    c.go(START); c.wait(10)
    c.camera(160, yaw=[(1, -38)], pitch=[(1, 24)], dolly=[(1, 1.25)])  # around: the shape in 3d
    c.wait(30)
    c.click(VALIDATE_AT); c.wait(40)                # a mesh to sculpt
    c.go(START); c.wait(10)
    c.camera(140, yaw=[(0.6, 30), (1, 24)], pitch=[(0.6, -6), (1, -4)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
