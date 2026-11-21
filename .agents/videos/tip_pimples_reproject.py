#!/usr/bin/env python3
"""docs/videos/tip_pimples_reproject.mp4: the polished metal sphere of tip_pimples_before.mp4, voxel
remeshed with Build multiresolution 3 and smoothed (setup): its reflections are dented by the pimples.
A clean Quad Sphere sits on it, hidden. The clip shows the clean sphere, selects it and hides the lumpy
one, then Topology > Bake > Reproject → Vertex brings the swirl onto the clean topology.
Same scene and look as the two clips before it in tips.md: a fresh scene, post process off (see
tip_pimples.py). See .agents/videos.md for the workflow.

    tip_pimples_reproject.py setup | python3 ../nomad/.agents/ai.py send -
    tip_pimples_reproject.py record [name] | python3 ../nomad/.agents/ai.py send - 900
`record dry` runs the same steps unrecorded. The hidden lumpy sphere is the only other mesh of the
scene, which Reproject then uses ("every other object hidden: the entire scene"). Widget ids are the
2026-11-20 build's (check them with `find` after a rebuild)."""
import sys

from clip import Clip
import tip_pimples as tp

SCENE, ADD, QUAD_SPHERE, BAKE_TAB = 3326, 3911, 3447, 67828
CAMERA, PERSPECTIVE = 17912, 18085
PRIM_MENU = 65074                            # the primitive menu panel ("..." of its toolbar)
ROW = lambda i: [209, 312 + 80 * i]          # Scene list rows: lumpy, clean
EYE = lambda i: [349, 352 + 80 * i]          # their eye buttons
PRIM_MORE = [692, 121]                       # "..." of the primitive toolbar
SCENE_AT = [125, 25]
REPROJECT_AT = [311, 688]                    # Reproject → Vertex: From high-res (1)
SPHERE_RADIUS = 0.4198                       # of a new scene's sphere: the clean one matches it
# the setup smooths less hard than the clip before (tp.INTENSITY, two passes: the swirl is gone): the
# swirl must survive, it is the detail to reproject
SMOOTH_INTENSITY, PASSES = 1, 1

c = Clip(tp.START, seed=17)
steps = c.steps


def clean_sphere():
    """A Quad Sphere on top of the lumpy one, as polished as it is. It stays selected."""
    steps.append({"do": "set", "id": SCENE, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": ADD})
    steps.append({"do": "click", "id": QUAD_SPHERE})
    steps.append({"do": "set", "id": SCENE, "value": False})
    c.wait(20)
    c.tap(PRIM_MORE)
    steps.append({"do": "set", "text": "Radius", "in": PRIM_MENU, "value": SPHERE_RADIUS})
    steps.append({"do": "set", "text": "Post subdivision", "value": 7})
    c.tap(PRIM_MORE)
    steps.append({"do": "click", "text": "Validate"})
    steps.append({"do": "set", "id": tp.SYM, "value": False})    # adding a primitive turns it back on
    steps.append({"do": "set", "id": tp.PAINT, "value": True})   # polished metal, as in tp.swirl_sphere
    steps.append({"do": "set", "id": tp.PAINT_MENU, "value": True})
    c.wait(5)
    steps.append({"do": "set", "id": tp.ROUGHNESS, "value": 25})
    steps.append({"do": "set", "id": tp.METALNESS, "value": 100})
    steps.append({"do": "click", "id": tp.ALL_ROUGHNESS})
    steps.append({"do": "click", "id": tp.ALL_METALNESS})
    steps.append({"do": "set", "id": tp.METALNESS, "value": 0})  # as found: other sessions paint too
    steps.append({"do": "set", "id": tp.ROUGHNESS, "value": 20})
    steps.append({"do": "set", "id": tp.PAINT_MENU, "value": False})
    steps.append({"do": "set", "id": tp.CLAY, "value": True})
    steps.append({"do": "set", "id": tp.SUB, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": tp.MATERIAL, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": tp.SMOOTH_SHADING})
    steps.append({"do": "set", "id": tp.MATERIAL, "value": False})
    c.wait(20)


def perspective():
    """Files > New resets the field of view (48.85) but keeps the projection: a session that loaded the
    viking project, or used a view shortcut, is orthographic, and tp.HOME then shows the sphere half
    as large as in the two clips before this one (685 px wide)."""
    steps.append({"do": "set", "id": CAMERA, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": PERSPECTIVE})
    steps.append({"do": "set", "id": CAMERA, "value": False})
    c.wait(20)


if sys.argv[1] == "setup":
    steps.append({"do": "scroll", "id": tp.TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": tp.CLAY, "value": True})  # after Gizmo some menus are disabled
    for i in tp.MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    perspective()
    tp.swirl_sphere(c)
    tp.remesh(c)
    tp.smooth_tool(c, False)
    tp.sliders(steps, tp.RADIUS, SMOOTH_INTENSITY)
    steps.append(dict({"do": "camera"}, **tp.HOME))
    for _ in range(PASSES):                      # the pimples show up
        tp.scrub(c, tp.zigzag(), tp.PASS)
    tp.sliders(steps, tp.RADIUS, tp.INTENSITY)   # as the other two clips leave it
    steps.append({"do": "set", "id": tp.CLAY, "value": True})  # Smooth's wider left toolbar shifts the menus
    clean_sphere()
    steps.append({"do": "set", "id": SCENE, "value": True})
    c.wait(5)                                    # let the list show the new row
    c.tap(EYE(1))                                # hidden for now
    c.tap(ROW(0))                                # a hidden object left selected shows through as a dither
    steps.append({"do": "set", "id": SCENE, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": tp.TOPO, "value": True})  # the menu opens on its Bake tab
    steps.append({"do": "click", "id": BAKE_TAB})
    steps.append({"do": "set", "id": tp.TOPO, "value": False})
    c.wait(20)
    steps.append(dict({"do": "camera"}, **tp.HOME))
    steps.append({"do": "drag", "points": [[900, 700], tp.START], "hover": True})
    c.wait(90)
    steps.append({"do": "stats"})
else:
    name = sys.argv[2] if len(sys.argv) > 2 else "tip_pimples_reproject"
    if name != "dry":
        steps.append({"do": "record", "to": name})
    c.wait(40)                                       # the lumpy voxel remesh
    c.click(SCENE_AT); c.wait(10)
    c.click(EYE(1)); c.wait(10)                      # show the clean sphere...
    # ...select it: Reproject works on the selection. A short press: held 8 frames while recording, the
    # row is picked up and dropped into the row above, as its child (hiding the parent then hides both)
    c.click(ROW(1), hold=2); c.wait(10)
    c.click(EYE(0)); c.wait(15)                      # ...and hide the lumpy one
    c.click(SCENE_AT)
    c.click(tp.TOPO_AT); c.wait(15)                  # Topology > Bake > Reproject → Vertex
    c.click(REPROJECT_AT); c.wait(60)                # the swirl, on clean topology
    c.click(tp.TOPO_AT)
    c.go(tp.START); c.wait(10)
    tp.look_around(c)                                # the reflections slide over a clean surface
    c.wait(40)
    if name != "dry":
        steps.append({"do": "record"})
print(c.json())
