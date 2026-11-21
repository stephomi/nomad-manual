#!/usr/bin/env python3
"""docs/videos/alpha_tiling.mp4: the Alpha tab pinned open next to a sphere, Paint tool, a pentagon alpha
stamped in red (`Lock + radius`: one big stamp shows the whole alpha). Four stamps, each one undone before
the next: `Tiling` 1, one pentagon; the slider dragged to 3 (`Tiling - X` on `Repeat`, `Tiling - Y` on
`None`, the defaults), a row of three; `Tiling - Y` on `Repeat`, a grid; both on `Mirror`, every other
row upside down. See stroke_modes.py and .agents/videos.md.

Paint rather than a sculpting tool: flat color reads at the page's size, the relief of a tiled alpha
doesn't. The paint falloff is off (Paint menu), or the outer tiles fade.

Prints the JSON steps for `ai.py send -`:
    alpha_tiling.py setup | python3 ../nomad/.agents/ai.py send -
    alpha_tiling.py record [name] | python3 ../nomad/.agents/ai.py send - 900
The clip ends with the pointer in the bottom left corner: its brush ring stays clear of the sphere."""
import sys

from clip import Clip
import stroke_modes as sm

VIEW = [0.25, 0, 2.85]                # the sphere left of the pinned menu, as large as the room allows
CENTER, UP = [420, 450], [0, -215]    # a drag straight up: the alpha stays upright
TILING_FROM, TILING_TO = [812, 689], [860, 689]   # the Tiling slider, 1 to 3
Y_REPEAT_AT, X_MIRROR_AT, Y_MIRROR_AT = [1003, 770], [1081, 730], [1081, 770]
START = [690, 790]
CORNER = [64, 832]                    # viewport corner above the Undo button: the ring clears the sphere

c = Clip(START, seed=47)
steps = c.steps


def slide(a, b, n=40):
    """Drag a slider: no rest on the press (a held press could open its input), a steady move."""
    c.go(a); c.wait(18)
    c.tap(a, 2)
    steps[-1]["points"] += c.path(a, b, n, 0.0, sm.glide)[1:] + [b] * 5
    c.pos = list(b)
    c.wait(24)


def stamp():
    sm.stamp(c, CENTER, UP, n=46, rest=34)


def undo():
    c.click(sm.UNDO_AT)


if sys.argv[1] == "setup":
    sm.new_scene(c)
    steps.append({"do": "set", "id": sm.PAINT, "value": True})
    c.wait(3)
    sm.paint(c, "d9432b", False)
    sm.tool(c, sm.PAINT, 70, 1, sm.LOCK_RADIUS, sm.PENTAGON, tab=sm.TAB_ALPHA, pin=True)
    sm.view(c, VIEW)
    sm.park(c, START)
else:
    sm.begin(c, sys.argv, "alpha_tiling")
    c.wait(30)
    stamp()                               # Tiling 1: the alpha once
    undo()
    slide(TILING_FROM, TILING_TO)         # Tiling 3, X Repeat, Y None: a row
    stamp()
    undo()
    c.click(Y_REPEAT_AT)                  # a grid
    stamp()
    undo()
    c.click(X_MIRROR_AT)
    c.click(Y_MIRROR_AT)                  # every other tile flipped
    stamp()
    c.go(CORNER)
    c.wait(40)
    sm.end(c)
print(c.json())
