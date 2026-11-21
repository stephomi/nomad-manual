#!/usr/bin/env python3
"""docs/videos/tool_smudge.mp4: a sphere painted yellow (Paint all, in setup); Paint lays red stripes
across it, then Smudge drags through them and blends the two colors like wet paint. See .agents/videos.md.

    tool_smudge.py setup | python3 ../nomad/.agents/ai.py send -
    tool_smudge.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX, CLAY, PAINT, SMUDGE = 58936, 67742, 67749, 67750
SYM, RADIUS, INTENSITY, SUB, PAINT_MENU, LAYOUT = 56799, 56725, 56745, 57353, 23086, 54629
# Files > New keeps the camera of the previous scene: set it. The sphere is then centered at 600,450, radius
# ~215: every stroke starts inside it (off the mesh, a drag turns the camera)
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0.04, 1.3]}
CAMERA_MENU, ORTHO = 17912, 18086
WINDOW = [1200, 900]
START = [1010, 700]
PAINT_AT, SMUDGE_AT = [1170, 540], [1170, 604]   # toolbox, scrolled to the top
COLOR_ROW, PAINT_ALL = [900, 498], [886, 696]    # Paint menu
HUE_X, SQUARE_CORNER, PICKER_CLOSE = 1038, [1004, 602], [1058, 502]
YELLOW_Y, RED_Y = 820, 596                        # on the hue bar

c = Clip(START, seed=61)
steps = c.steps


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def color(hue_y):
    """Setup only: Paint menu (open) > color row > picker, hue then the saturated corner."""
    c.tap(COLOR_ROW, 2); c.wait(10)
    c.tap([HUE_X, hue_y], 2); c.wait(5)
    c.tap(SQUARE_CORNER, 2); c.wait(5)
    c.tap(PICKER_CLOSE, 2); c.wait(5)


def stroke(way, n, rest=15):
    """One stroke through the waypoints (straight segments), eased at both ends."""
    c.go(way[0]); c.wait(8)
    segs = [(way[i], way[i + 1]) for i in range(len(way) - 1)]
    pts = []
    for i in range(n + 1):
        u = min_jerk(i / n) * len(segs)
        k = min(int(u), len(segs) - 1)
        t = u - k
        a, b = segs[k]
        pts.append([round(a[0] + (b[0] - a[0]) * t, 1), round(a[1] + (b[1] - a[1]) * t, 1)])
    steps.append({"do": "drag", "points": pts})
    c.pos = list(way[-1]); c.wait(rest)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": True})   # orthographic: the size HOME expects
    steps.append({"do": "click", "id": ORTHO})
    steps.append({"do": "set", "id": CAMERA_MENU, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "camera", "dolly": 0.72})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    # radius and intensity per tool, set from the compact layout of the left bar (the stroke list hides them)
    # (Smudge has no stroke list: its sliders are always there)
    steps.append({"do": "set", "id": SMUDGE, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 45})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "set", "id": PAINT, "value": True})
    steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "set", "id": RADIUS, "value": 26})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": PAINT_MENU, "value": True})   # yellow everywhere, then red for the clip
    c.wait(5)
    color(YELLOW_Y)
    c.tap(PAINT_ALL, 2); c.wait(10)
    color(RED_Y)
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})
    steps.append({"do": "set", "id": CLAY, "value": True})         # the clip picks Paint itself
    steps.append({"do": "drag", "points": [[1100, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "capture", "converge": False})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_smudge"})
    c.wait(30)
    pick(PAINT_AT)                                       # red stripes on the yellow
    for y in (330, 410, 490, 570):
        stroke([[478, y + 8], [600, y - 6], [722, y + 8]], 34, rest=10)
    c.wait(15)
    pick(SMUDGE_AT)                                      # Smudge: drag the wet paint around
    # (the sphere: center 600,461, radius ~198; strokes start on it, off it a drag turns the camera)
    stroke([[495, 335], [515, 590]], 50, rest=15)
    stroke([[585, 600], [610, 320]], 50, rest=15)
    stroke([[690, 340], [705, 590]], 50, rest=15)
    stroke([[465, 465], [530, 425], [600, 475], [670, 425], [735, 465]], 80, rest=30)
    c.go(START); c.wait(40)
    steps.append({"do": "record"})
print(c.json())
