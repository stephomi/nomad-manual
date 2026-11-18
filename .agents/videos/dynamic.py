#!/usr/bin/env python3
"""docs/videos/dynamic.mp4: a low quad sphere in wireframe; Topology > DynTopo > Enabled, then Clay
strokes add small triangles only where they pass. Zoomed in, a stroke makes even smaller ones (Screen
detail). Post process off (the main checkbox of its menu), as a new user sees the app. See
.agents/videos.md.

    dynamic.py setup | python3 ../../.agents/ai.py send -
    dynamic.py record [name] | python3 ../../.agents/ai.py send - 900
The woman project only lends its background: its objects are hidden, a Quad Sphere is added.
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import os
import sys

from clip import Clip

PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/woman.nom")
SCENE, TOPO, POST, POST_PANEL = 3326, 6399, 13905, 13892
CLAY, SYM, RADIUS, WIREFRAME, LIGHTS, CAMERAS = 67742, 56799, 56725, 46039, 4059, 4060
ADD, QUAD_SPHERE = 3911, 3447
MULTIRES_TAB, DYN_TAB, DYN_ENABLED = 67820, 67822, 6581
RENDER_RES, POST_ON = 13908, 13907           # POST_ON: the checkbox of the "Post Process" title
EYE = lambda i: [349, 352 + 80 * i]          # eye buttons of the Scene list rows
WINDOW = [1200, 900]
TOPO_AT = [175, 25]
ENABLED_AT = [371, 374]
DYN_SHORTCUT = [25, 150]
PRIM_MORE = [692, 121]                       # "..." of the primitive toolbar
START = [1010, 640]


def post_setup(steps):
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})  # the whole post process off
    steps.append({"do": "set", "id": POST, "value": False})


c = Clip(START, seed=5)
steps = c.steps

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    post_setup(steps)
    steps.append({"do": "click", "id": SCENE})
    for i in range(5):
        c.tap(EYE(i))                                # hide the bust
    steps.append({"do": "set", "id": LIGHTS, "value": False})
    steps.append({"do": "set", "id": CAMERAS, "value": False})
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "id": QUAD_SPHERE})
    steps.append({"do": "click", "id": SCENE})
    c.tap(PRIM_MORE)
    steps.append({"do": "set", "text": "Post subdivision", "value": 3})  # big quads: the new triangles stand out
    c.tap(PRIM_MORE)
    steps.append({"do": "click", "text": "Validate"})
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "set", "id": RADIUS, "value": 45})
    steps.append({"do": "set", "id": WIREFRAME, "value": True})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "click", "id": MULTIRES_TAB})
    steps.append({"do": "click", "text": "Delete lower"})  # one level: no multires popup, full wireframe
    steps.append({"do": "click", "id": DYN_TAB})
    # the left toolbar's DynTopo shortcut (only there while Enabled is on) keeps its own on/off state,
    # even across Files > New: off, the strokes would add no triangle
    steps.append({"do": "set", "id": DYN_ENABLED, "value": True})
    steps.append({"do": "set", "text": "DynTopo", "type": "button", "value": True})
    steps.append({"do": "set", "id": DYN_ENABLED, "value": False})
    steps.append({"do": "click", "id": TOPO})
    steps.append({"do": "action", "name": "view_focus"})
    c.wait(30)
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "dynamic"})
    c.wait(40)
    c.click(TOPO_AT); c.wait(15)                    # Topology > DynTopo
    c.click(ENABLED_AT); c.wait(25)
    c.click(TOPO_AT)
    c.go(DYN_SHORTCUT); c.wait(35)                  # the DynTopo toggle now under Sym, left
    a = [470, 330]; c.go(a); c.wait(10)            # Clay strokes: triangles appear only along them
    c.stroke(a, [720, 300], 55, bow=-0.12); c.wait(15)
    a = [450, 450]; c.go(a, 20); c.wait(8)
    c.stroke(a, [760, 470], 60, bow=0.1); c.wait(15)
    a = [500, 580]; c.go(a, 20); c.wait(8)
    c.stroke(a, [700, 560], 50, bow=0.15); c.wait(30)
    c.go(START); c.wait(10)
    c.camera(90, dolly=[(1, 0.55)], pan_x=[(1, 0.08)], pan_y=[(1, -0.06)]); c.wait(20)  # closer
    a = [430, 380]; c.go(a); c.wait(10)             # zoomed in, the same detail makes smaller triangles
    c.stroke(a, [760, 420], 60, bow=-0.1); c.wait(40)
    c.go(START); c.wait(10)
    c.camera(200, dolly=[(1, 1.6)], yaw=[(0.6, 30), (1, 24)], pitch=[(0.5, -12), (1, -8)],
             pan_x=[(1, -0.07)], pan_y=[(1, 0.05)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
