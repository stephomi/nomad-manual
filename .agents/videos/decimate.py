#!/usr/bin/env python3
"""docs/videos/decimate.mp4: the woman's head in wireframe, Topology > Decimate pressed three times
(50% each): the triangles grow where the surface is flat and stay small on the eyes, nose and lips.
A closer look ends the clip. Post process off (the main checkbox of its menu), as a new user sees
the app. See .agents/videos.md.

    decimate.py setup | python3 ../nomad/.agents/ai.py send -
    decimate.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import sys

from clip import Clip

PROJECT = "/Users/steph/Downloads/data_nomad/cache/projects/manual/woman.nom"
SCENE, TOPO, POST, POST_PANEL = 3326, 6399, 13905, 13892
CLAY, SYM, RADIUS, WIREFRAME, LIGHTS, CAMERAS = 67742, 56799, 56725, 46039, 4059, 4060
DECIMATE_TAB = 67825
RENDER_RES, POST_ON = 13908, 13907           # POST_ON: the checkbox of the "Post Process" title
WINDOW = [1200, 900]
TOPO_AT = [175, 25]
DECIMATE_AT = [156, 380]
START = [1010, 640]


def post_setup(steps):
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})  # the whole post process off
    steps.append({"do": "set", "id": POST, "value": False})


c = Clip(START, seed=7)
steps = c.steps

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    post_setup(steps)
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": LIGHTS, "value": False})
    steps.append({"do": "set", "id": CAMERAS, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "set", "id": RADIUS, "value": 45})  # the resting brush ring: the radius is shared state
    steps.append({"do": "set", "id": WIREFRAME, "value": True})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "click", "id": DECIMATE_TAB})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(30)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "decimate"})
    c.wait(40)
    c.click(TOPO_AT); c.wait(15)                    # Topology > Decimate, Target triangles 50%
    for _ in range(3):
        c.click(DECIMATE_AT); c.wait(45)
    c.click(TOPO_AT)
    c.go(START); c.wait(10)
    # closer on the face: small triangles on the features, big ones on the cheeks and forehead
    c.camera(220, yaw=[(0.5, 24), (1, 18)], pitch=[(0.5, 4), (1, 2)], dolly=[(0.5, 0.6), (1, 0.58)],
             pan_x=[(0.5, -0.04), (1, -0.05)], pan_y=[(0.5, 0.05), (1, 0.06)])
    c.wait(60)
    steps.append({"do": "record"})
print(c.json())
