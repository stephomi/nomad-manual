#!/usr/bin/env python3
"""docs/videos/stroke_dot.mp4: Brush on a sphere. Stroke menu > `Dot` picked (the menu opens on `Lock +
radius`), then two dragged strokes, a wavy one and one that loops over itself: a regular paint stroke.
A short look around. See stroke_modes.py and .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    stroke_dot.py setup | python3 ../nomad/.agents/ai.py send -
    stroke_dot.py record [name] | python3 ../nomad/.agents/ai.py send - 900"""
import sys

from clip import Clip
import stroke_modes as sm

RIDGE = [[365, 405], [450, 300], [555, 335], [645, 265], [755, 300], [835, 390]]
LOOP = [[385, 520], [480, 480], [590, 530], [670, 620], [600, 665], [535, 600], [610, 520], [730, 500],
        [820, 555]]

c = Clip(sm.START, seed=31)
if sys.argv[1] == "setup":
    sm.new_scene(c)
    sm.tool(c, sm.BRUSH, 42, 0.5, sm.LOCK_RADIUS, sm.NONE)  # the clip picks Dot itself
    sm.view(c)
    sm.park(c)
else:
    sm.begin(c, sys.argv, "stroke_dot")
    c.wait(30)
    c.click(sm.STROKE_AT)
    c.click(sm.DOT_AT); c.wait(15)
    c.click(sm.STROKE_AT)
    sm.draw(c, sm.winding(RIDGE, 105))
    sm.draw(c, sm.winding(LOOP, 150))
    sm.look(c)
    c.wait(30)
    sm.end(c)
print(c.json())
