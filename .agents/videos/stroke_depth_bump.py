#!/usr/bin/env python3
"""docs/videos/stroke_depth_bump.mp4: red strokes across a plane of stone tiles cover tops and grooves
alike; undo, Filter > Depth filter (Height offset +50%, no Depth falloff): the same strokes only paint
the tile tops. See stroke_depth.py and .agents/videos.md.

The page suggests +90%: on these tiles (grooves ~1/3 of the brush radius deep) it leaves the tops
barely touched, +50% keeps them fully painted and the grooves clean.

Prints the JSON steps for `ai.py send -`:
    stroke_depth_bump.py setup | python3 ../nomad/.agents/ai.py send -
    stroke_depth_bump.py record [name] | python3 ../nomad/.agents/ai.py send - 900"""
import sys

from clip import Clip
import stroke_depth as sd

RED_AT = [646, 390]                   # plastic red preset

c = Clip(sd.START, seed=19)
if sys.argv[1] == "setup":
    sd.setup(c, RED_AT, offset=50, top=100, bottom=100, falloff=False, area=100)  # a wide area: the plane doesn't drop into each groove
else:
    sd.record(c, sys.argv[2] if len(sys.argv) > 2 else "stroke_depth_bump", sd.STROKES)
print(c.json())
