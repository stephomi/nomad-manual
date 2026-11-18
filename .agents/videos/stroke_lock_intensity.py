#!/usr/bin/env python3
"""docs/videos/stroke_lock_intensity.mp4: Brush on a sphere, with the square alpha. Stroke menu > `Lock +
intensity`, then three stamps of the same size along the upper part of the sphere: the drag away from the
press sets how high the square rises and turns it. A short drag leaves a low slab, a longer one a block,
a drag across the sphere a tower. The camera then tilts until the three stand on the silhouette, in
profile. See stroke_modes.py and .agents/videos.md.

The intensity is the drag's length: 100 px for 100%, with no limit at 100% (the drags are 60, 180 and
400 px). Heights closer together (20% to 140% in earlier takes) look the same at the page's size.
The stamps sit on a great circle 33 degrees above the equator (38 degrees apart), so one tilt brings all
three to the silhouette together; a negative pitch looks from below.

Prints the JSON steps for `ai.py send -`:
    stroke_lock_intensity.py setup | python3 ../../.agents/ai.py send -
    stroke_lock_intensity.py record [name] | python3 ../../.agents/ai.py send - 900"""
import sys

from clip import Clip
import stroke_modes as sm

c = Clip(sm.START, seed=43)
if sys.argv[1] == "setup":
    sm.new_scene(c)
    sm.tool(c, sm.BRUSH, 84, 0.5, sm.DOT, sm.SQUARE)  # the clip picks Lock + intensity itself
    sm.view(c)
    sm.park(c)
else:
    sm.begin(c, sys.argv, "stroke_lock_intensity")
    c.wait(30)
    c.click(sm.STROKE_AT)
    c.click(sm.LOCK_INTENSITY_AT); c.wait(15)
    c.click(sm.STROKE_AT)
    sm.stamp(c, [400, 311], [48, -36])          # 60%: a low slab
    sm.stamp(c, [600, 268], [60, 170])          # 180%: a block, turned
    sm.stamp(c, [800, 311], [-330, 226])        # 400%: a tower
    c.go(sm.REST); c.wait(10)
    sm.view(c)  # the stamps moved the orbit pivot onto the surface: back to the center, same view
    c.camera(200, yaw=[(0.5, 6), (1, 4)], pitch=[(0.6, -34), (1, -28)], pan_y=[(1, 0.03)])
    c.wait(40)
    sm.end(c)
print(c.json())
