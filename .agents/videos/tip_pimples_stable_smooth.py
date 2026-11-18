#!/usr/bin/env python3
"""docs/videos/tip_pimples_stable_smooth.mp4: the sphere of tip_pimples_before.mp4 right after its voxel
remesh (setup), Smooth active. The tool's settings: `Stable smoothing` ticked; the same two scrubbing
passes melt the swirl and leave clean reflections. See tip_pimples.py and .agents/videos.md.

    tip_pimples_stable_smooth.py setup | python3 ../../.agents/ai.py send -
    tip_pimples_stable_smooth.py record [name] | python3 ../../.agents/ai.py send - 900
    tip_pimples_stable_smooth.py restore | python3 ../../.agents/ai.py send -
`restore` unticks Stable smoothing again (a setting the sessions share). `record dry` runs the same
steps unrecorded."""
import sys

from clip import Clip
import tip_pimples as tp

STABLE_AT = [1066, 452]                       # the checkbox of Stable smoothing, in Settings - Smooth

c = Clip(tp.START, seed=29)
steps = c.steps

if sys.argv[1] == "setup":
    tp.swirl_sphere(c)
    tp.remesh(c)
    tp.smooth_tool(c, False)                  # the clip ticks it
    steps.append(dict({"do": "camera"}, **tp.HOME))
    steps.append({"do": "drag", "points": [[900, 700], tp.START], "hover": True})
    c.wait(90)
    steps.append({"do": "stats"})
elif sys.argv[1] == "restore":
    tp.smooth_tool(c, False)
else:
    name = sys.argv[2] if len(sys.argv) > 2 else "tip_pimples_stable_smooth"
    if name != "dry":
        steps.append({"do": "record", "to": name})
    c.wait(40)                                 # the remeshed swirl
    c.click(tp.TOOL_MENU_AT); c.wait(10)       # Settings - Smooth
    c.click(STABLE_AT); c.wait(25)             # Stable smoothing
    c.click(tp.TOOL_MENU_AT)
    tp.smooth_hard(c)                          # the swirl melts, no pimples
    tp.look_around(c)
    c.wait(50)
    if name != "dry":
        steps.append({"do": "record"})
print(c.json())
