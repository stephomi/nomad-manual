#!/usr/bin/env python3
"""docs/videos/reference_camera.mp4: the dragon in its left view, lined up with a reference image of the
same pose next to it. Camera > Add View saves the view (its row shows the image's thumbnail);
Background > Reference image unticked, the image is gone; the camera orbits away; a tap on the view in
the Camera menu brings back both the viewpoint and the reference image. See .agents/videos.md.

    reference_camera.py setup | python3 ../nomad/.agents/ai.py send -
    reference_camera.py record [name] | python3 ../nomad/.agents/ai.py send - 900
`record dry` runs the same steps unrecorded.

Choosing the image isn't in the clip: `Import...` opens the system file dialog, which the AI API can't
drive. The user's `dragon_reference.nom` (manual folder) holds the reference settings and the image's
name; the image itself (.agents/scenes/IMG_3307.webp, as a PNG) must sit in the sandbox user folder
before Nomad starts: ~/Downloads/data_nomad/cache/tmp_session/argB/backgrounds/IMG_3307.png (see
.agents/audit.md). After the load the `Reference image` title looks dimmed but its checkbox works.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip

PROJECTS = "/Users/steph/Downloads/data_nomad/cache/projects/manual/"
# top bar buttons: menus stay open across a project load. The second list is disabled unless a mesh is
# selected with a sculpting tool (a take ends with the saved view selected, the user's scene opens with
# the Gizmo), and a `set` on a disabled widget is an error
MENUS = [108, 3326, 9959, 13905, 18138, 17912, 40184, 35769]
MESH_MENUS = [6399, 11516, 33760, 33331, 32972, 23086, 19331, 27845]
SCENE, POST, POST_PANEL, RENDER_RES, POST_ON = 3326, 13905, 13892, 13908, 13907
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, SUB, CLAY, VIEW_TOOL, TOOLBOX = 56799, 57353, 67742, 67777, 58936
BACKGROUND, REFERENCE = 18138, 19173  # top bar button, the `Reference image` checkbox
# reference image sliders: overlay, opacity, position x and y, scale, rotation
PLACEMENT = {19176: 0, 19196: 100, 19232: 0.49, 19252: 0, 19292: 0.5, 19272: 0}
WINDOW = [1200, 900]
# left view: the model's pose in the reference image, at the image's size, just left of it
VIEW = {"pivot": [-0.54194, 0.50378, 0.11329], "rotation": [0.0034278, -0.699427, 0.0033546, -0.714688],
        "translation": [2.0, -0.34, 8.476]}
ON_MODEL = [400, 560]                 # a tap there selects a mesh of the dragon (the tail: the selected
#                                       groups show their icon in the middle of the model, and it takes taps)
START = [640, 790]
CAMERA_AT, BACKGROUND_AT = [425, 25], [375, 25]
ADD_VIEW_AT = [270, 182]              # Add View, while the list of views is empty
VIEW_ROW_AT = [200, 172]              # the name of the first view
REFERENCE_AT = [370, 665]             # the checkbox of Reference image, Background panel not scrolled

c = Clip(START, seed=41)
steps = c.steps

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    steps.append({"do": "import", "path": PROJECTS + "dragon_reference.nom", "replace": True})
    steps.append({"do": "import", "path": PROJECTS + "dragon.nom", "replace": False})
    c.wait(30)
    steps.append({"do": "set", "id": POST, "value": True})
    c.wait(5)
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})  # off, as a new user sees it
    steps.append({"do": "set", "id": POST, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": SCENE, "value": True})
    c.wait(5)
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": BACKGROUND, "value": True})
    c.wait(10)
    steps.append({"do": "set", "id": REFERENCE, "value": True})
    c.wait(5)
    for i, value in PLACEMENT.items():
        steps.append({"do": "set", "id": i, "value": value})
    steps.append({"do": "set", "id": BACKGROUND, "value": False})
    c.wait(20)
    # the import leaves the lights and groups selected, with their icons: select a mesh instead
    # (with the View tool: the Gizmo's handles, in the middle of the model, would take the tap)
    steps.append({"do": "set", "id": VIEW_TOOL, "value": True})
    c.wait(5)
    steps.append(dict({"do": "camera"}, **VIEW))
    c.tap(ON_MODEL)
    c.wait(10)
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})  # the user's scene leaves the Gizmo tool on; not
    c.wait(5)                                               # `tool_clay`, which toggles when Clay is active
    for i in MESH_MENUS:                                    # enabled now: a mesh and a sculpting tool
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 40})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append(dict({"do": "camera"}, **VIEW))            # the tap moved the orbit pivot
    steps.append({"do": "drag", "points": [[560, 700], START], "hover": True})
    c.wait(90)
    steps.append({"do": "stats"})
else:
    name = sys.argv[2] if len(sys.argv) > 2 else "reference_camera"
    if name != "dry":
        steps.append({"do": "record", "to": name})
    c.wait(50)                             # the model, lined up with its reference image
    c.click(CAMERA_AT); c.wait(10)
    c.click(ADD_VIEW_AT); c.wait(40)       # Add View: the row shows the reference image's thumbnail
    c.click(CAMERA_AT)
    c.click(BACKGROUND_AT); c.wait(10)
    c.click(REFERENCE_AT); c.wait(30)      # Reference image off
    c.click(BACKGROUND_AT)
    c.go(START); c.wait(10)
    c.camera(170, yaw=[(0.6, -80), (1, -68)], pitch=[(0.5, 14), (1, 10)], dolly=[(0.6, 0.9), (1, 0.92)])
    c.wait(35)                             # another viewpoint
    c.click(CAMERA_AT); c.wait(10)
    c.click(VIEW_ROW_AT); c.wait(60)       # the saved view: its viewpoint and its reference image
    c.click(CAMERA_AT)
    c.go(START); c.wait(55)
    if name != "dry":
        steps.append({"do": "record"})
print(c.json())
