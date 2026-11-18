#!/usr/bin/env python3
"""docs/videos/stroke_lockradius_drag.mp4: the `Lock + radius` stroke type of Move. On a sphere: Stroke
menu > `Lock + radius`, then three pulls of growing length. The radius follows the distance dragged: a
short pull raises a small spike, a longer one a cone, a long one stretches the whole top into a teardrop;
a look around. See .agents/videos.md.

    stroke_lockradius_drag.py setup | python3 ../../.agents/ai.py send -
    stroke_lockradius_drag.py record [name] | python3 ../../.agents/ai.py send - 900
    stroke_lockradius_drag.py dry | ...          the same steps unrecorded, with a capture
Setup leaves Move on `Grab`, its default type."""
import sys

import stroke_common as sc
from clip import Clip

VIEW = sc.SPHERE_VIEW                 # sphere center 580,500, radius 212 px
# far enough apart: the long pull's radius (its length) would carry closer bumps along
SHORT = [[730, 560], [778, 582]]      # 53 px
MEDIUM = [[430, 560], [330, 605]]     # 110 px
LONG = [[580, 330], [588, 125]]       # 205 px

c = Clip(sc.START, seed=13)
steps = c.steps
mode = sys.argv[1]

if mode == "setup":
    sc.new_scene(c)
    sc.tool(c, sc.MOVE, 100, 1, sc.MODE_GRAB)  # 100%: the surface stays under the pointer (default 50%: a third)
    sc.view(c, VIEW)
    sc.park(c)
else:
    sc.begin(c, mode, sys.argv[2] if len(sys.argv) > 2 else "stroke_lockradius_drag")
    c.wait(24)
    c.click(sc.STROKE_AT); c.wait(5)
    c.click(sc.LOCK_AT); c.wait(12)           # Stroke type: Lock + radius
    c.click(sc.STROKE_AT)
    sc.pull(c, SHORT, 40, rest=30)            # the further the drag, the larger the radius
    sc.pull(c, MEDIUM, 60, rest=30)
    sc.pull(c, LONG, 90, rest=30)
    c.go(sc.REST); c.wait(10)
    sc.view(c, VIEW)                          # strokes moved the orbit pivot: same view, pivot at the center
    c.camera(132, yaw=[(0.5, -32), (1, -22)], pitch=[(0.45, 10), (1, 6)], dolly=[(0.5, 1.04), (1, 1.03)])
    c.wait(24)
    sc.end(c, mode)
print(c.json())
