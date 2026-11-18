#!/usr/bin/env python3
"""A plane of raised stone tiles with grooves between them, for the Depth filter clips
(stroke_depth_bump, stroke_depth_cavity): a heightfield written as OBJ.

stone_tiles.py <out.obj>
"""
import math
import random
import sys

W, H = 2.0, 1.5              # plane size
NX, NY = 320, 240            # grid resolution
COLS, ROWS = 5, 4            # tiles
GROOVE = 0.065             # half width of the groove between tiles
BEVEL = 0.05                 # width of the rounded tile border
DEPTH = 0.07                 # groove depth

rng = random.Random(3)
tiles = [[(rng.uniform(-0.012, 0.012), rng.uniform(-0.06, 0.06), rng.uniform(-0.06, 0.06))
          for _ in range(ROWS)] for _ in range(COLS)]
waves = [(rng.uniform(4, 9), rng.uniform(4, 9), rng.uniform(0, 6.3), rng.uniform(0, 6.3)) for _ in range(4)]


def height(x, y):
    u, v = (x + W / 2) / W * COLS, (y + H / 2) / H * ROWS
    i, j = min(int(u), COLS - 1), min(int(v), ROWS - 1)
    fu, fv = u - i, v - j
    # distance to the tile border, in plane units
    d = min(fu, 1 - fu) * W / COLS, min(fv, 1 - fv) * H / ROWS
    edge = min(d)
    t = min(max((edge - GROOVE) / BEVEL, 0.0), 1.0)
    profile = math.sin(t * math.pi / 2)            # rounded shoulder from the groove floor to the top
    off, tx, ty = tiles[i][j]
    top = off + tx * (fu - 0.5) * 0.3 + ty * (fv - 0.5) * 0.3
    top += sum(0.004 * math.sin(a * x + p) * math.sin(b * y + q) for a, b, p, q in waves)  # a worn surface
    return -DEPTH + profile * (DEPTH + top)


out = open(sys.argv[1], "w")
for j in range(NY + 1):
    for i in range(NX + 1):
        x, y = -W / 2 + W * i / NX, -H / 2 + H * j / NY
        out.write("v %.5f %.5f %.5f\n" % (x, height(x, y), -y))
for j in range(NY):
    for i in range(NX):
        a = j * (NX + 1) + i + 1
        b = a + NX + 1
        out.write("f %d %d %d %d\n" % (a, a + 1, b + 1, b))
out.close()
