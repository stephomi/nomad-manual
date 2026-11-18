#!/usr/bin/env python3
"""docs/videos/stroke_depth_cavity.mp4: dark blue strokes across a plane of stone tiles cover tops and
grooves alike; undo, Filter > Depth filter (Height offset 0%, Depth falloff with Top area 10%): the same
strokes only paint the grooves. See stroke_depth.py and .agents/videos.md.

The page suggests a -100% offset: the plane then sits a whole brush radius under the surface and the
falloff fades the grooves out too. With a wide Area sampling (100%), the plane is the tiles' average
height: 0% and a thin Top area keep the tops out and the grooves in.

Prints the JSON steps for `ai.py send -`:
    stroke_depth_cavity.py setup | python3 ../../.agents/ai.py send -
    stroke_depth_cavity.py record [name] | python3 ../../.agents/ai.py send - 900"""
import sys

from clip import Clip
import stroke_depth as sd

COLOR_AT = [646, 312]                 # plastic blue preset

c = Clip(sd.START, seed=23)
if sys.argv[1] == "setup":
    sd.setup(c, COLOR_AT, offset=0, top=10, bottom=100, falloff=True, area=100)
else:
    sd.record(c, sys.argv[2] if len(sys.argv) > 2 else "stroke_depth_cavity", sd.STROKES)
print(c.json())
