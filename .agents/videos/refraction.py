#!/usr/bin/env python3
"""docs/videos/refraction.mp4: a sphere in front of the viking's beard; Material > Refraction (blurry:
the default roughness), Paint glossy (clear glass), Index of Refraction raised (stronger lens), then
the Interior roughness override for a frosted inside under a sharp surface. See .agents/videos.md.

    refraction.py setup | python3 ../nomad/.agents/ai.py send -
    refraction.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Post process is off (the project is saved with it on: setup unchecks `Post Process`), as a new user
sees the viewport: refraction doesn't need it.
Widget ids are the 2026-11-19 build's (check them with `find` after a rebuild)."""
import sys

from clip import Clip

PROJECT = "/Users/steph/Downloads/data_nomad/cache/projects/manual/viking.nom"
SCENE, POST, POST_PANEL = 3326, 13905, 13892
LIGHTS, CAMERAS, ADD, QUAD_SPHERE, CLAY, SYM, RADIUS = 4059, 4060, 3911, 3447, 67742, 56799, 56725
MATERIAL, MATERIAL_PANEL = 11516, 11503
PRIM_MENU = 65074                           # the primitive menu panel ("..." of its toolbar)
POST_ON = 13907                             # the `Post Process` checkbox, above the effects
RENDER_RES = 13908
WINDOW = [1200, 900]
PRIM_MORE = [692, 121]
MATERIAL_AT, REFRACTION_AT, GLOSSY_AT = [225, 25], [119, 322], [235, 584]
IOR_Y, INTERIOR_Y = 538, 650                # Interior: once the panel is scrolled by SCROLL
SCROLL = ([360, 600], [360, 380])            # a drag on the panel background
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


def line(a, b, n=30):
    return [[round(a[0] + (b[0] - a[0]) * i / n, 1), round(a[1] + (b[1] - a[1]) * i / n, 1)] for i in range(n + 1)]


c = Clip(START, seed=29)
steps = c.steps

if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(10)
    post_setup(steps)
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": LIGHTS, "value": False})
    steps.append({"do": "set", "id": CAMERAS, "value": False})
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "id": QUAD_SPHERE})  # at the origin, inside the head
    steps.append({"do": "click", "id": SCENE})
    c.tap(PRIM_MORE)
    steps.append({"do": "set", "text": "Radius", "in": PRIM_MENU, "value": 0.9})
    steps.append({"do": "set", "text": "Post subdivision", "value": 7})  # smooth normals: no grid in the glass
    c.tap(PRIM_MORE)
    steps.append({"do": "click", "text": "Validate"})
    # move it out in front of the beard with the gizmo, seen from the right: forward (Z), then down (Y)
    steps.append({"do": "set", "id": CLAY, "value": True})  # tool_gizmo toggles back when Gizmo is active
    steps.append({"do": "action", "name": "tool_gizmo"})
    steps.append({"do": "action", "name": "view_toggle_right"})
    c.wait(30)
    steps.append({"do": "drag", "points": line([478, 191], [98, 191])})
    steps.append({"do": "camera", "pan": [-0.1, 0.2]})
    steps.append({"do": "drag", "points": line([320, 130], [320, 306])})
    steps.append({"do": "action", "name": "view_toggle_front"})
    c.wait(30)
    steps.append({"do": "camera", "orbit": [14, 4], "dolly": 0.92, "pan": [-0.06, 0]})  # clear of the menu
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 45})  # the resting ring: other clips change it
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "click", "id": MATERIAL})  # panels keep their scroll: start at the top
    steps.append({"do": "scroll", "id": MATERIAL_PANEL, "to": 0})
    steps.append({"do": "click", "id": MATERIAL})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})                    # Quad Sphere box ~ -0.9,-2.2,1.9 0.9,-0.4,3.7
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "refraction"})
    c.wait(40)
    c.click(MATERIAL_AT); c.wait(15)
    c.click(REFRACTION_AT); c.wait(45)              # glass, blurry: the painted roughness
    c.click(GLOSSY_AT); c.wait(45)                  # roughness and metalness painted to 0: clear
    a = [150, IOR_Y]; c.go(a); c.wait(15)           # Index of Refraction up: a stronger lens
    c.stroke(a, [205, IOR_Y], 50, bow=0); c.wait(40)
    c.go(SCROLL[0]); c.wait(10)                     # down to the roughness overrides
    c.stroke(SCROLL[0], SCROLL[1], 30, bow=0); c.wait(25)
    a = [188, INTERIOR_Y]; c.go(a); c.wait(15)      # Interior rougher: frosted inside, sharp surface
    c.stroke(a, [228, INTERIOR_Y], 50, bow=0); c.wait(45)
    c.click(MATERIAL_AT)
    c.go(START); c.wait(10)
    c.camera(170, yaw=[(0.5, -24), (1, -18)], pitch=[(0.5, 5), (1, 3)])  # the lens shifts as it turns
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
