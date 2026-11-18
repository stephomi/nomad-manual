#!/usr/bin/env python3
"""docs/videos/symmetry_demo.mp4: a new scene's sphere, the Symmetry menu pinned open (it draws the
symmetry planes on the model while it is open). A Brush stroke with the default X plane is mirrored;
the Y plane is added, a stroke now makes four; Radial Z dragged to 6, a stroke makes twelve rays; a short
look around. See .agents/videos.md for the workflow.

    symmetry_demo.py setup | python3 ../../.agents/ai.py send -
    symmetry_demo.py record [name] | python3 ../../.agents/ai.py send - 900
    symmetry_demo.py restore | python3 ../../.agents/ai.py send -
`restore` unpins and closes the Symmetry menu (the pin outlives the scene). `record dry` runs the same
steps unrecorded. The symmetry settings belong to the object: a new scene has the defaults again.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import math
import sys

from clip import Clip, min_jerk

# top bar buttons, Symmetry apart. The second list is disabled unless a mesh is selected with a
# sculpting tool, and a `set` on a disabled widget is an error
MENUS = [108, 3326, 9959, 13905, 18138, 17912, 40184, 35769]
MESH_MENUS = [6399, 11516, 33760, 33331, 23086, 19331, 27845]
FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
CAMERA, PERSPECTIVE, FOV = 17912, 18085, 17914
SYM, SUB = 56799, 57353
SYMMETRY, PIN = 32972, 32965          # top bar button, the pin of its panel header
PLANES, RADIALS, TILES = (32975, 32976, 32977), (32978, 32998, 33018), (33038, 33039, 33040)
CLAY, BRUSH, TOOLBOX = 67742, 67743, 58936
WINDOW = [1200, 900]
# Files > New keeps the camera and field of view of the previous scene: both are set. The sphere is
# then at 406,450, radius ~262, left of the pinned panel
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0.31, 0, 3.3]}
CENTER = [406, 450]
START = [690, 780]
Y_AT = [1003, 250]                    # Planes: Y
RADIAL_Z = ([1050, 302], [1170, 302]) # Radial Z, a relative slider: 120 px to the right takes 1 to 6
#                                       (8 needs 150 px, which ends on the window edge)

c = Clip(START, seed=37)
steps = c.steps


def polar(r, deg):
    a = math.radians(deg)
    return [round(CENTER[0] + r * math.cos(a), 1), round(CENTER[1] + r * math.sin(a), 1)]


def glide(t, a=0.06, d=0.2):
    """Up to speed at once, steady, a soft landing: an eased start counts as a long press while recording."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def stroke(pts_of, n):
    """One Brush stroke along pts_of(0..1)."""
    c.go(pts_of(0)); c.wait(10)
    steps.append({"do": "drag", "points": [pts_of(glide(i / n)) for i in range(n + 1)]})
    c.pos = list(pts_of(1))
    c.wait(50)


def unpin():
    steps.append({"do": "set", "id": SYMMETRY, "value": True})
    c.wait(10)
    steps.append({"do": "set", "id": PIN, "value": False})
    steps.append({"do": "set", "id": SYMMETRY, "value": False})
    c.wait(20)


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": FILES, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": NEW})
    c.wait(5)
    steps.append({"do": "click", "id": YES})
    c.wait(10)
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": POST, "value": True})    # post process is off in a new scene
    c.wait(5)
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": CAMERA, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": PERSPECTIVE})          # a saved view can leave it orthographic
    steps.append({"do": "set", "id": FOV, "value": 25})
    steps.append({"do": "set", "id": CAMERA, "value": False})
    c.wait(20)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})    # the tool survives a new scene (View, Gizmo...)
    c.wait(5)
    unpin()
    for i in MESH_MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": BRUSH, "value": True})
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 18})
    steps.append({"do": "set", "text": "intensity.png", "type": "slider", "value": 0.5})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "action", "name": "subdivide"})       # 393k: at 98k the arcs come out in steps
    c.wait(10)
    steps.append({"do": "set", "id": SYM, "value": True})
    steps.append({"do": "set", "id": SYMMETRY, "value": True})
    c.wait(10)
    steps.append({"do": "set", "id": PIN, "value": True})
    for i, on in zip(PLANES, (True, False, False)):           # the defaults, whatever a take left
        steps.append({"do": "set", "id": i, "value": on})
    for i in RADIALS:
        steps.append({"do": "set", "id": i, "value": 1})
    for i in TILES:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "drag", "points": [[600, 700], START], "hover": True})
    c.wait(90)
    steps.append({"do": "stats"})
elif sys.argv[1] == "restore":
    unpin()
else:
    name = sys.argv[2] if len(sys.argv) > 2 else "symmetry_demo"
    if name != "dry":
        steps.append({"do": "record", "to": name})
    c.wait(55)                                            # Planes: X, the red line
    stroke(lambda u: polar(70, -80 + 70 * u), 40)         # an arc right of the center: mirrored on the left
    c.click(Y_AT); c.wait(15)                             # + Y: a second line
    stroke(lambda u: polar(140, 68 - 46 * u), 50)         # an arc, lower right: four of them
    a, b = RADIAL_Z                                       # Radial Z: 6 repeats around the view axis
    c.go(a); c.wait(16)
    steps.append({"do": "drag", "points": [[round(a[0] + (b[0] - a[0]) * min_jerk(i / 70), 1), a[1]]
                                           for i in range(71)]})
    c.pos = list(b)
    c.wait(30)
    # one ray near the rim, 15° off the X axis: the 6 repeats and their mirrors make 12 even rays
    stroke(lambda u: polar(186 + 50 * u, 15), 34)
    c.go(START); c.wait(15)
    steps.append(dict({"do": "camera"}, **HOME))          # strokes moved the orbit pivot (same view)
    c.camera(190, yaw=[(0.5, -34), (1, -22)], pitch=[(0.5, 12), (1, 8)])
    c.wait(50)
    if name != "dry":
        steps.append({"do": "record"})
print(c.json())
