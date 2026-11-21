#!/usr/bin/env python3
"""docs/videos/stroke_grab.mp4: the `Grab` stroke type. Same low sphere, view and pointer paths as
stroke_drag.mp4, with the Move tool: Stroke menu > `Grab`, then the two winding pulls. What was under the
brush at the start stays selected and follows the pointer, so each pull ends as one straight horn (the
wireframe shows the same quads, stretched) instead of a snake; a look around. See .agents/videos.md.

    stroke_grab.py setup | python3 ../nomad/.agents/ai.py send -
    stroke_grab.py record [name] | python3 ../nomad/.agents/ai.py send - 900
    stroke_grab.py dry | ...          the same steps unrecorded, with a capture
Setup leaves Move on `Drag`, as the previous clip of the page ends, so the click on `Grab` shows a change
(Grab is Move's default type)."""
import sys

import stroke_common as sc
from clip import Clip

VIEW, RIGHT, LEFT = sc.SPHERE_VIEW, sc.PULL_RIGHT, sc.PULL_LEFT

c = Clip(sc.START, seed=12)
steps = c.steps
mode = sys.argv[1]

if mode == "setup":
    sc.new_scene(c)
    sc.low_sphere(c)
    steps.append({"do": "set", "id": sc.WIREFRAME, "value": True})
    sc.tool(c, sc.MOVE, 100, 1, sc.MODE_DRAG)  # 100%: the tip stays under the pointer (Move's default 50%: halfway)
    sc.view(c, VIEW)
    sc.park(c)
else:
    sc.begin(c, mode, sys.argv[2] if len(sys.argv) > 2 else "stroke_grab")
    c.wait(24)
    c.click(sc.STROKE_AT); c.wait(5)
    c.click(sc.GRAB_AT); c.wait(12)           # Stroke type: Grab
    c.click(sc.STROKE_AT)
    sc.pull(c, RIGHT, 138, rest=20)           # the same paths as stroke_drag: the horn follows the pointer
    sc.pull(c, LEFT, 138, rest=20)
    c.go(sc.REST); c.wait(10)
    sc.view(c, VIEW)                          # strokes moved the orbit pivot: same view, pivot at the center
    c.camera(132, yaw=[(0.5, -32), (1, -22)], pitch=[(0.45, 10), (1, 6)], dolly=[(0.5, 1.04), (1, 1.03)])
    c.wait(24)
    sc.end(c, mode)
print(c.json())
