#!/usr/bin/env python3
"""docs/videos/stroke_drag.mp4: the `Drag` stroke type. On a low sphere in wireframe, with the Drag tool:
Stroke menu > `Drag`, DynTopo turned on with its left toolbar shortcut, then two slow winding strokes pull
snake-like antennae out of the sphere (the stroke keeps picking up what is under the brush, DynTopo adds
the triangles); a look around. See .agents/videos.md.

    stroke_drag.py setup | python3 ../../.agents/ai.py send -
    stroke_drag.py record [name] | python3 ../../.agents/ai.py send - 900
    stroke_drag.py dry | ...          the same steps unrecorded, with a capture
Setup leaves the Drag tool on `Grab`, so the click on `Drag` shows a change (Drag is its default type).
The Drag tool rather than Move: in Drag mode the pull is scaled by the intensity, and Move's default 50%
loses the material after a short distance."""
import sys

import stroke_common as sc
from clip import Clip

VIEW, RIGHT, LEFT = sc.SPHERE_VIEW, sc.PULL_RIGHT, sc.PULL_LEFT  # shared with stroke_grab

c = Clip(sc.START, seed=11)
steps = c.steps
mode = sys.argv[1]

if mode == "setup":
    sc.new_scene(c)
    sc.low_sphere(c)
    steps.append({"do": "set", "id": sc.WIREFRAME, "value": True})
    sc.tool(c, sc.DRAG, 100, 1, sc.MODE_GRAB)
    # DynTopo: `Enabled` shows its shortcut under Sym; the shortcut off, the clip turns it on
    steps.append({"do": "set", "id": sc.TOPO, "value": True})
    steps.append({"do": "click", "id": sc.DYN_TAB})
    c.wait(3)
    steps.append({"do": "set", "text": "Enabled", "value": True})
    c.wait(5)
    steps.append({"do": "set", "id": sc.DYN_SHORTCUT, "value": False})
    steps.append({"do": "set", "id": sc.TOPO, "value": False})
    sc.view(c, VIEW)
    sc.park(c)
else:
    sc.begin(c, mode, sys.argv[2] if len(sys.argv) > 2 else "stroke_drag")
    c.wait(24)
    c.click(sc.STROKE_AT); c.wait(5)
    c.click(sc.DRAG_AT); c.wait(12)           # Stroke type: Drag
    c.click(sc.STROKE_AT)
    c.click(sc.DYN_SHORTCUT_AT, hold=1); c.wait(8)  # DynTopo on: the stretched surface gets new triangles
    sc.pull(c, RIGHT, 138, rest=16)           # slow strokes: the brush holds onto the material
    sc.pull(c, LEFT, 138, rest=16)
    c.go(sc.REST); c.wait(10)
    sc.view(c, VIEW)                          # strokes moved the orbit pivot: same view, pivot at the center
    c.camera(132, yaw=[(0.5, -32), (1, -22)], pitch=[(0.45, 10), (1, 6)], dolly=[(0.5, 1.04), (1, 1.03)])
    c.wait(24)
    sc.end(c, mode)
print(c.json())
