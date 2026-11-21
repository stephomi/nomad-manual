#!/usr/bin/env python3
"""docs/videos/stroke_silhouette.mp4: the `Silhouette` option. A box in wireframe, seen from the front and
a little above, with Move: a pull on its top front edge only raises a bump near that edge. Stroke menu >
`Silhouette` on (its projection choices show, `Closest` by default), and the same pull next to it raises
a ridge that runs through the whole depth of the box; the camera swings up to compare the two from above.
See .agents/videos.md.

    stroke_silhouette.py setup | python3 ../nomad/.agents/ai.py send -
    stroke_silhouette.py record [name] | python3 ../nomad/.agents/ai.py send - 900
    stroke_silhouette.py dry | ...          the same steps unrecorded, with a capture"""
import sys

import stroke_common as sc
from clip import Clip

ROTATION = [0.1851411759853363, -0.2374771237373352, -0.04616088047623634, 0.9524686932563782]  # yaw -28, pitch 22
VIEW = [0, 0, 4.199]
PLAIN = [[380, 277], [384, 157]]      # from just under the top front edge, straight up
THROUGH = [[600, 314], [604, 194]]

c = Clip(sc.START, seed=15)
steps = c.steps
mode = sys.argv[1]

if mode == "setup":
    sc.new_scene(c)
    steps.append({"do": "action", "name": "delete"})   # the new scene's sphere: flat faces show the depth
    steps.append({"do": "action", "name": "add_box"})  # 32 divisions: a wireframe that reads at the page's size
    c.wait(5)
    steps.append({"do": "click", "text": "Validate", "type": "button"})
    c.wait(5)
    steps.append({"do": "set", "id": sc.SYM, "value": False})  # a new primitive turns symmetry back on
    steps.append({"do": "scroll", "id": sc.TOOLBOX, "to": 0})  # its scroll shifts while a primitive is edited
    steps.append({"do": "set", "id": sc.WIREFRAME, "value": True})
    sc.tool(c, sc.MOVE, 110, 0.75, sc.MODE_GRAB)  # 75%: a tall, still rounded bump (Move's default is 50%)
    sc.view(c, VIEW, ROTATION)
    sc.park(c)
else:
    sc.begin(c, mode, sys.argv[2] if len(sys.argv) > 2 else "stroke_silhouette")
    c.wait(24)
    sc.pull(c, PLAIN, 55, rest=35)            # a regular stroke: only the surface within the radius moves
    c.click(sc.STROKE_AT); c.wait(5)
    c.click(sc.SILHOUETTE_AT); c.wait(40)     # Silhouette: X, Y, Z, View, If snapped, Closest
    c.click(sc.STROKE_AT)
    sc.pull(c, THROUGH, 55, rest=35)          # the same pull goes through the whole box
    c.go(sc.REST); c.wait(10)
    sc.view(c, VIEW, ROTATION)                # strokes moved the orbit pivot: same view, pivot at the center
    c.camera(170, yaw=[(0.6, -24), (1, -18)], pitch=[(0.55, 26), (1, 22)], dolly=[(0.5, 1.06), (1, 1.05)])
    c.wait(30)
    sc.end(c, mode)
print(c.json())
