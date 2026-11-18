#!/usr/bin/env python3
"""docs/videos/stroke_lock_radius.mp4: Brush on a sphere, with the square alpha. Stroke menu > `Lock +
radius`, then three stamps: each press plants the square, the drag away from it sets its size and turns
it (a short drag, a longer one, a long one), all at the same height. A short look around. See
stroke_modes.py and .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    stroke_lock_radius.py setup | python3 ../../.agents/ai.py send -
    stroke_lock_radius.py record [name] | python3 ../../.agents/ai.py send - 900"""
import sys

from clip import Clip
import stroke_modes as sm

c = Clip(sm.START, seed=41)
if sys.argv[1] == "setup":
    sm.new_scene(c)
    sm.tool(c, sm.BRUSH, 60, 0.9, sm.DOT, sm.SQUARE)  # the clip picks Lock + radius itself
    sm.view(c)
    sm.park(c)
else:
    sm.begin(c, sys.argv, "stroke_lock_radius")
    c.wait(30)
    c.click(sm.STROKE_AT)
    c.click(sm.LOCK_RADIUS_AT); c.wait(15)
    c.click(sm.STROKE_AT)
    sm.stamp(c, [440, 330], [50, -29])          # small
    sm.stamp(c, [745, 345], [58, 69])           # medium, turned the other way
    sm.stamp(c, [575, 585], [-138, 24])         # large
    sm.look(c)
    c.wait(30)
    sm.end(c)
print(c.json())
