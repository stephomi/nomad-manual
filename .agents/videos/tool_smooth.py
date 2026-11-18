#!/usr/bin/env python3
"""docs/videos/tool_smooth.mp4: a sphere with three sculpted ridges and a hard-edged painted patch. Smooth is
picked in the toolbox: one scrubbing stroke melts the ridges, a second one along the patch blurs its edge;
a short look around. See .agents/videos.md.

`Relax` (the sub mode) is not in the clip: its effect on the wireframe is too subtle to read at the size of
the page, even zoomed in on polygons that were dragged out of shape first (tried 2026-11-20).

Prints the JSON steps for `ai.py send -`:
    tool_smooth.py setup | python3 ../../.agents/ai.py send -
    tool_smooth.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
CAMERA, FOV = 17912, 17914
TOPO, MULTIRES, DELETE_HIGHER = 6399, 67820, 6499
LEVEL_1 = [235, 341]                  # multires slider, middle tick (a slider `set` doesn't change the level)
TOOLBOX = 58936
CLAY, BRUSH, SMOOTH, PAINT, SMOOTH_AT = 67742, 67743, 67747, 67749, [1170, 410]
SYM, SUB, WIREFRAME = 56799, 57353, 46039
PAINT_MENU, PAINT_FALLOFF, COLOR_ROW, HEX, PICKER_CLOSE = 23086, 23141, 23178, 23366, 23166
RED = "a81420"
WINDOW = [1200, 900]
START = [1010, 640]
HOME_Z = 2.956                        # a new scene is at 3.359: a little closer, the sphere fills the view

c = Clip(START)
steps = c.steps


def new_scene():
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    # a new scene has the post process off: only the render resolution to set
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": CAMERA, "value": True})  # HOME_Z frames the sphere for this field of view
    steps.append({"do": "set", "id": FOV, "value": 25})
    steps.append({"do": "set", "id": CAMERA, "value": False})
    steps.append({"do": "camera", "pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, HOME_Z]})


def fewer_polygons():
    """Down one multires level, 24.5k quads: "if you have many polygons, the smoothing will be less
    effective", and on the 98k of a new scene a stroke only softens the ridges, at any intensity. Clay is
    active: a tool with a second slider column would shift the menu."""
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": MULTIRES})
    c.wait(5)
    steps.append({"do": "drag", "points": [LEVEL_1] * 3})
    c.wait(5)
    steps.append({"do": "click", "id": DELETE_HIGHER})
    steps.append({"do": "set", "id": TOPO, "value": False})


def tool(button, radius, intensity):
    """Select a tool and set it up. Sliders by icon name: Paint shows them unlabelled next to its stroke list."""
    steps.append({"do": "set", "id": button, "value": True})
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": radius})
    steps.append({"do": "set", "text": "intensity.png", "type": "slider", "value": intensity})
    steps.append({"do": "set", "id": SUB, "value": False})  # each tool keeps its own, a new scene too


def paint_setup(hex_color, falloff):
    """Paint menu: the color by its hex value, and whether the stroke fades toward its edge."""
    steps.append({"do": "set", "id": PAINT_MENU, "value": True})
    steps.append({"do": "set", "id": PAINT_FALLOFF, "value": falloff})
    if hex_color:
        steps.append({"do": "click", "id": COLOR_ROW})
        steps.append({"do": "click", "id": HEX})
        c.wait(5)
        steps.append({"do": "type", "input": hex_color})  # no id: the field is already being edited
        steps.append({"do": "click", "text": "Ok"})   # by text: the dialog is built when it first opens
        steps.append({"do": "click", "id": PICKER_CLOSE})
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})


def pick(p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def catmull(pts, u):
    """Point at u (0..1) on a Catmull-Rom curve through pts."""
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def glide(t, a=0.04, d=0.2):
    """Progress of a long stroke: up to speed at once, steady, a soft landing. An eased start (min_jerk)
    leaves the press almost still for a second while recording, which Smooth takes for a long press: it
    switches to the Select tool for that stroke."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def scrub(way, n, rest=18):
    """One drag back and forth through the waypoints: how a hand rubs with Smooth."""
    c.go(way[0]); c.wait(12)
    pts = [[round(v, 1) for v in catmull(way, glide(i / n))] for i in range(n + 1)]
    steps.append({"do": "drag", "points": pts})
    c.pos = list(way[-1])
    c.wait(rest)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    new_scene()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "set", "id": WIREFRAME, "value": False})
    fewer_polygons()
    tool(BRUSH, 24, 0.65)                        # three strong ridges, upper right
    scrub([[545, 255], [615, 222], [685, 258], [750, 240]], 45)
    scrub([[540, 345], [615, 312], [690, 348], [760, 330]], 45)
    scrub([[545, 435], [615, 402], [685, 438], [755, 420]], 45)
    tool(PAINT, 34, 1)                           # a red patch with a hard, uneven edge, on the left
    paint_setup(RED, False)
    scrub([[370, 300], [470, 310], [380, 350], [490, 370], [360, 400], [480, 430], [370, 460], [490, 500],
           [380, 530], [470, 550]], 150)
    paint_setup(None, True)                      # the falloff back on: the setting is shared with other clips
    tool(SMOOTH, 70, 2)                          # the default 75 % softens the ridges, 200 % melts them
    steps.append({"do": "set", "id": CLAY, "value": True})  # the clip picks Smooth itself
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(90)                                   # the Paint menu button stays lit a moment after it closes
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_smooth"})
    c.wait(25)
    pick(SMOOTH_AT)
    # down the ridges in a zigzag, then back up: they melt
    # (every point on the sphere, 287 px around [600, 442]: a drag that starts beside it orbits the camera)
    scrub([[775, 240], [560, 262], [785, 325], [555, 352], [785, 415], [560, 442], [770, 345], [565, 250],
           [760, 238]], 220)
    # along the edge of the paint, down and back: it blurs
    scrub([[490, 290], [470, 400], [495, 540], [475, 420], [490, 300]], 120)
    c.go(START); c.wait(10)
    # strokes moved the orbit pivot onto the surface: back to the center, same view (no visible change)
    steps.append({"do": "camera", "pivot": [0, 0, 0], "translation": [0, 0, HOME_Z]})
    c.camera(140, yaw=[(0.55, 24), (1, 15)], pitch=[(0.5, 10), (1, 6)])
    c.wait(30)
    steps.append({"do": "record"})
print(c.json())
