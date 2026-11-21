#!/usr/bin/env python3
"""docs/videos/tip_pimples_before.mp4: a polished metal sphere with a crease swirl. Topology > Voxel:
`Build multiresolution` dragged to 3, Remesh. Smooth, picked in the toolbox, scrubbed hard over the
swirl: it melts, and the reflections stay dented where the remeshed topology is uneven (the pimples).
See tip_pimples.py and .agents/videos.md.

    tip_pimples_before.py setup | python3 ../nomad/.agents/ai.py send -
    tip_pimples_before.py record [name] | python3 ../nomad/.agents/ai.py send - 900
`record dry` runs the same steps unrecorded."""
import sys

from clip import Clip, min_jerk
import tip_pimples as tp

MULTIRES_Y, MULTIRES_X = 469, (88, 300)       # Build multiresolution: a relative slider, ~70 px per level
REMESH_AT = [235, 353]
OK_AT = [311, 449]                            # Ok of "UV will be lost!" (the default sphere has UVs)

c = Clip(tp.START, seed=23)
steps = c.steps

if sys.argv[1] == "setup":
    tp.swirl_sphere(c)
    tp.smooth_tool(c, False)
    steps.append({"do": "set", "id": tp.CLAY, "value": True})   # the clip picks Smooth itself
    steps.append({"do": "drag", "points": [[900, 700], tp.START], "hover": True})
    c.wait(90)
    steps.append({"do": "stats"})
else:
    name = sys.argv[2] if len(sys.argv) > 2 else "tip_pimples_before"
    if name != "dry":
        steps.append({"do": "record", "to": name})
    c.wait(40)                                 # the swirl
    c.click(tp.TOPO_AT); c.wait(10)            # Topology, on its Voxel tab
    a, b = MULTIRES_X                          # Build multiresolution: 0 -> 3
    c.go([a, MULTIRES_Y]); c.wait(14)
    n = 60
    steps.append({"do": "drag", "points": [[round(a + (b - a) * min_jerk(i / n), 1), MULTIRES_Y]
                                           for i in range(n + 1)]})
    c.pos = [b, MULTIRES_Y]
    c.wait(25)
    c.click(REMESH_AT); c.wait(10)             # Remesh: "UV will be lost!"
    c.click(OK_AT); c.wait(40)                 # remeshed
    c.click(tp.TOPO_AT)
    tp.pick(c, tp.SMOOTH_AT)
    tp.smooth_hard(c)                          # the swirl melts, the pimples stay
    tp.look_around(c)
    c.wait(50)
    if name != "dry":
        steps.append({"do": "record"})
print(c.json())
