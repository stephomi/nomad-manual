#!/usr/bin/env python3
"""docs/videos/unwrap.mp4: the colored woman's head gets Topology > UV Unwrap > UVAtlas Unwrap; with
`Show UV after unwrap` on, the UV inspector shows a checker on the model and the islands behind it.
Then BFF Unwrap for comparison: fewer, bigger islands. Post process off (the main checkbox of its
menu), as a new user sees the app. See .agents/videos.md.

    unwrap.py setup | python3 ../nomad/.agents/ai.py send -
    unwrap.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import sys

from clip import Clip

PROJECT = "/Users/steph/Downloads/data_nomad/cache/projects/manual/woman color.nom"
SCENE, TOPO, POST, POST_PANEL = 3326, 6399, 13905, 13892
CLAY, SYM, RADIUS, LIGHTS, CAMERAS = 67742, 56799, 56725, 4059, 4060
UV_TAB, UV_PANEL, SHOW_UV = 67827, 5458, 5479
RENDER_RES, POST_ON = 13908, 13907           # POST_ON: the checkbox of the "Post Process" title
WINDOW = [1200, 900]
TOPO_AT = [175, 25]
ATLAS_AT = [156, 380]
BFF_AT = [156, 632]
START = [1010, 640]


def post_setup(steps):
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})  # the whole post process off
    steps.append({"do": "set", "id": POST, "value": False})


c = Clip(START, seed=13)
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
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "click", "id": UV_TAB})
    steps.append({"do": "scroll", "id": UV_PANEL, "to": 110})
    steps.append({"do": "set", "id": SHOW_UV, "value": True})  # open the UV inspector after unwrapping
    steps.append({"do": "scroll", "id": UV_PANEL, "to": 0})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(30)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "unwrap"})
    c.wait(40)
    c.click(TOPO_AT); c.wait(20)                    # Topology > UV Unwrap
    # the inspector (checker on the model, islands behind it) shows while the menu is open: keep it open
    c.click(ATLAS_AT); c.wait(50)                   # UVAtlas: many islands, little stretch
    c.go(START); c.wait(10)
    c.camera(150, yaw=[(0.5, 26), (1, 20)], pitch=[(0.5, 4), (1, 3)])
    c.wait(30)
    c.click(BFF_AT); c.wait(50)                     # BFF: fewer cuts, more stretch
    c.go(START); c.wait(10)
    c.camera(150, yaw=[(0.5, -30), (1, -24)], pitch=[(0.5, -3), (1, -2)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
