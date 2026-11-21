#!/usr/bin/env python3
"""docs/videos/stroke_roll.mp4: Brush on a sphere, with an alpha of diagonal stripes. A wavy stroke in
`Dot` smears the alpha into a plain ridge; Stroke menu > `Roll`, and the same stroke below unrolls the
stripes along its path, turning with it like a row of stitches. A short look around. See stroke_modes.py
and .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    stroke_roll.py setup | python3 ../nomad/.agents/ai.py send -
    stroke_roll.py record [name] | python3 ../nomad/.agents/ai.py send - 900"""
import sys

from clip import Clip
import stroke_modes as sm

X0, X1, AMPLITUDE = 375, 825, 56
Y_DOT, Y_ROLL = 345, 555

c = Clip(sm.START, seed=37)
if sys.argv[1] == "setup":
    sm.new_scene(c)
    sm.tool(c, sm.BRUSH, 44, 0.5, sm.DOT, sm.STRIPES)  # strong enough for the Dot ridge to read
    sm.view(c)
    sm.park(c)
else:
    sm.begin(c, sys.argv, "stroke_roll")
    c.wait(30)
    sm.draw(c, sm.wave(X0, X1, Y_DOT, AMPLITUDE, 105))    # Dot: the stripes blur into a ridge
    c.click(sm.STROKE_AT)
    c.click(sm.ROLL_AT); c.wait(15)
    c.click(sm.STROKE_AT)
    sm.draw(c, sm.wave(X0, X1, Y_ROLL, AMPLITUDE, 120))   # Roll: the stripes follow the stroke
    sm.look(c)
    c.wait(30)
    sm.end(c)
print(c.json())
