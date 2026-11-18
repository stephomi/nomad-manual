#!/usr/bin/env python3
"""docs/videos/stroke_lazy_rope.mp4: `Lazy rope stabilizer`. Close on a sphere with Crease: a line drawn
with a shaky hand comes out wobbly; Stroke menu, the `Lazy rope stabilizer` slider dragged up, and the
same shaky path just below gives a smooth line, the stroke trailing the pointer at the end of its rope;
a short look around. See .agents/videos.md.

    stroke_lazy_rope.py setup | python3 ../../.agents/ai.py send -
    stroke_lazy_rope.py record [name] | python3 ../../.agents/ai.py send - 900
    stroke_lazy_rope.py dry | ...          the same steps unrecorded, with a capture and the slider's value"""
import math
import sys

import stroke_common as sc
from clip import Clip

VIEW = [0.081, 0, 2.75]               # closer: the sphere fills the view (center 540,450, radius 311 px)
TOPO_SUBDIVIDE = 6482
TOOLBOX_SCROLL = 200                  # shows Crease, below the fold of the window
SLIDER_AT, SLIDER_DRAG = [826, 686], 62  # press on the Lazy rope slider, drag right: about 1 per px
FIRST = ([300, 345], [745, 325])
SECOND = ([290, 565], [815, 545])     # longer: the stroke stops a rope's length before the pointer
AMP = 17                              # px of hand shake

c = Clip(sc.START, seed=14)
steps = c.steps
mode = sys.argv[1]


def shaky(a, b, n):
    """A line from a to b drawn by an unsteady hand: slow sideways waves of a few periods at once, a slight
    hesitation along the way. The same function of the distance for every line: both strokes get the same
    shake. Starts and stops at speed (a stroke that lingers snaps into a curve)."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    pts = []
    for i in range(n + 1):
        d = sc.glide(i / n, 0.04, 0.05) * length
        env = min(1.0, d / 40, (length - d) / 40)           # steady at both ends
        side = AMP * env * (math.sin(d / 9.5) + 0.6 * math.sin(d / 5.3 + 1.3) + 0.5 * math.sin(d / 17.0 + 0.4)) / 1.6
        along = d + 0.35 * AMP * env * math.sin(d / 7.1 + 2.0)
        pts.append([round(a[0] + ux * along - uy * side, 1), round(a[1] + uy * along + ux * side, 1)])
    return pts


def line(a, b, n):
    c.go(a); c.wait(12)
    steps.append({"do": "drag", "points": shaky(a, b, n)})
    c.pos = list(b)
    c.wait(30)


if mode == "setup":
    sc.new_scene(c)
    # one more level (393k): a crease needs polygons to stay sharp
    steps.append({"do": "set", "id": sc.TOPO, "value": True})
    steps.append({"do": "click", "id": sc.MULTIRES_TAB})
    steps.append({"do": "click", "id": TOPO_SUBDIVIDE})
    steps.append({"do": "set", "id": sc.TOPO, "value": False})
    steps.append({"do": "scroll", "id": sc.TOOLBOX, "to": TOOLBOX_SCROLL})
    c.wait(5)
    steps.append({"do": "set", "id": sc.CREASE, "value": True})
    c.wait(3)
    steps.append({"do": "set", "id": sc.RADIUS, "value": 45})
    steps.append({"do": "set", "id": sc.INTENSITY, "value": 1.5})  # a deep line: it has to read at 360 px
    steps.append({"do": "set", "id": sc.SUB, "value": False})      # `Invert`, kept per tool
    steps.append({"do": "set", "id": sc.STROKE, "value": True})
    c.wait(3)
    steps.append({"do": "click", "text": "Stroke", "type": "radio_option", "in": sc.STROKE_PANEL})
    steps.append({"do": "scroll", "id": sc.STROKE_PANEL, "to": 0})
    c.wait(3)
    steps.append({"do": "set", "id": sc.LAZY_ROPE, "value": 0})
    steps.append({"do": "set", "id": sc.STROKE, "value": False})
    sc.view(c, VIEW)
    sc.park(c)
else:
    sc.begin(c, mode, sys.argv[2] if len(sys.argv) > 2 else "stroke_lazy_rope")
    c.wait(24)
    line(*FIRST, 115)                         # no stabilizer: every shake of the hand shows
    c.click(sc.STROKE_AT); c.wait(5)
    c.go(SLIDER_AT); c.wait(20)               # Lazy rope stabilizer: drag the slider up
    end = [SLIDER_AT[0] + SLIDER_DRAG, SLIDER_AT[1] + 2]
    steps.append({"do": "drag", "points": [SLIDER_AT] * 5 + c.path(SLIDER_AT, end, 34, 0.0, sc.min_jerk) + [end] * 5})
    c.pos = end
    c.wait(30)
    if mode == "dry":
        steps.append({"do": "find", "text": "Lazy rope"})
    c.click(sc.STROKE_AT)
    line(*SECOND, 135)                        # the same shake, smoothed out
    c.go(sc.REST); c.wait(10)
    sc.view(c, VIEW)                          # strokes moved the orbit pivot: same view, pivot at the center
    c.camera(120, yaw=[(0.5, 20), (1, 13)], pitch=[(0.5, 9), (1, 6)])
    c.wait(24)
    sc.end(c, mode)
print(c.json())
