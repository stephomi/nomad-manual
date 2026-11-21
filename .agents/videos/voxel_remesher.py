#!/usr/bin/env python3
"""docs/videos/voxel_remesher.mp4: the elephant's head (voxel remeshed low in setup, wireframe on) gets
an ear pulled far out with Move, which stretches its faces; Topology > Voxel > Remesh evens them out.
Then the trunk is pulled and remeshed again: hit Remesh once in a while. Post process off (the main
checkbox of its menu), as a new user sees the app. See .agents/videos.md.

    voxel_remesher.py setup | python3 ../nomad/.agents/ai.py send -
    voxel_remesher.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import sys

from clip import Clip

PROJECT = "/Users/steph/Downloads/data_nomad/cache/projects/manual/elephant.nom"
SCENE, TOPO, POST, POST_PANEL = 3326, 6399, 13905, 13892
MOVE, SYM, RADIUS, WIREFRAME, LIGHTS = 67744, 56799, 56725, 46039, 4059
VOXEL_TAB, VOXEL_RES, VOXEL_REMESH = 67821, 6814, 6954
RENDER_RES, POST_ON = 13908, 13907           # POST_ON: the checkbox of the "Post Process" title
ROW = lambda i: [209, 312 + 80 * i]          # Scene list rows
EYE = lambda i: [349, 352 + 80 * i]          # their eye buttons
WINDOW = [1200, 900]
TOPO_AT = [175, 25]
VOXEL_AT = [165, 122]
REMESH_AT = [235, 394]
START = [1000, 640]


def post_setup(steps):
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})  # the whole post process off
    steps.append({"do": "set", "id": POST, "value": False})


c = Clip(START, seed=3)
steps = c.steps

EAR, EAR_TO = [740, 330], [1030, 300]       # the side of the head, pulled into a big lump
TRUNK, TRUNK_TO = [442, 722], [650, 800]

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    post_setup(steps)
    steps.append({"do": "click", "id": SCENE})
    c.tap(ROW(0))                                   # the head
    c.tap(EYE(3))                                   # hide the body
    steps.append({"do": "set", "id": LIGHTS, "value": False})  # no light gizmos in the viewport
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "click", "id": VOXEL_TAB})
    steps.append({"do": "set", "id": VOXEL_RES, "value": 90})  # a light block-out mesh: its wireframe reads
    steps.append({"do": "click", "id": VOXEL_REMESH})
    steps.append({"do": "click", "text": "Ok"})      # the head had multires levels
    c.wait(5)
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "set", "id": WIREFRAME, "value": True})
    steps.append({"do": "set", "id": MOVE, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "set", "id": RADIUS, "value": 95})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(30)
    steps.append({"do": "action", "name": "view_focus"})
    c.wait(30)
    steps.append({"do": "camera", "orbit": [-25, 10], "dolly": 0.85, "pan": [0.02, -0.09]})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(60)                                      # let the toasts fade
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "voxel_remesher"})
    c.wait(40)
    c.go(EAR); c.wait(15)                           # pull a lump far out: its faces stretch
    c.stroke(EAR, EAR_TO, 80, bow=-0.08); c.wait(15)
    c.go([1060, 470]); c.wait(50)                   # rest below it: the stretched faces read
    c.click(TOPO_AT); c.wait(10)                    # Topology > Voxel
    c.click(REMESH_AT); c.wait(60)                  # even faces again
    c.click(TOPO_AT)
    c.go(TRUNK); c.wait(15)                         # stretch the trunk, remesh again
    c.stroke(TRUNK, TRUNK_TO, 70, bow=0.08); c.wait(40)
    c.click(TOPO_AT); c.wait(5)
    c.click(REMESH_AT); c.wait(50)
    c.click(TOPO_AT)
    c.go(START); c.wait(10)
    c.camera(180, yaw=[(0.5, 22), (1, 14)], pitch=[(0.5, -6), (1, -3)], dolly=[(0.5, 0.92), (1, 0.94)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
