"""The scene shared by tool_insert.py and tool_transform.py: a small sandy terrain (a Plane primitive,
validated, a few broad Brush strokes for hills, painted matte) seen from three quarters above. The front
left of the plane stays flat (y = 0): objects placed there by their matrix sit on the ground.
See .agents/videos.md.

Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES, DITHERING, POST_ON = 13905, 13892, 13908, 14346, 13907
SCENE, ADD, DELETE, JOIN = 3326, 3911, 3912, 3929
ADD_PLANE, ADD_CYLINDER, ADD_SPHERE, ADD_ICOSAHEDRON = 3453, 3451, 3447, 3449
XDIVISION, VALIDATE = 62297, 63231                 # primitive toolbar
CAMERA_MENU, PERSPECTIVE = 17912, 18085
TOOLBOX, BRUSH = 58936, 67743
INSERT, TRANSFORM, GIZMO = 67767, 67768, 67769     # toolbox, scrolled to its end
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
# Transform menu > Matrix
TRANSFORM_MENU, UNIFORM, BAKE = 27845, 28176, 27863
TX, TY, TZ = 27936, 27956, 27976
RX, RY, RZ = 27996, 28016, 28036
SX, SY, SZ = 28056, 28076, 28096                   # SX is the only scale slider with Uniform scale on
# Paint menu: the global material, `Paint all`
PAINT_MENU, COLOR, ROUGHNESS, METALNESS, PAINT_ALL = 23086, 23178, 23367, 23387, 23482
PICKER_HEX, PICKER_CLOSE = 23366, 23166            # in the color popup

WINDOW = [1200, 900]
TOP = {"pivot": [0, 0, 0], "rotation": [0.70710678, 0, 0, 0.70710678], "translation": [0, 0, 2.6]}
# top view at that distance: 768 px per unit, the plane's center at 600,442
SAND = "#d6c193"


def wait(steps, n):
    steps.append({"do": "wait", "frames": n})


def menu(steps, button, inside):
    steps.append({"do": "set", "id": button, "value": True})
    wait(steps, 3)
    steps.extend(inside)
    steps.append({"do": "set", "id": button, "value": False})
    wait(steps, 3)


def new_scene(steps):
    """Files > New, render resolution x1 with nothing grainy, perspective camera."""
    steps.append({"do": "window", "size": WINDOW})
    menu(steps, FILES, [{"do": "click", "id": NEW}, {"do": "click", "id": YES}])
    wait(steps, 5)
    menu(steps, POST, [{"do": "scroll", "id": POST_PANEL, "to": 0}, {"do": "wait", "frames": 3},
                       {"do": "set", "id": RENDER_RES, "value": 1}, {"do": "set", "id": DITHERING, "value": False},
                       {"do": "set", "id": POST_ON, "value": False}])
    menu(steps, CAMERA_MENU, [{"do": "click", "id": PERSPECTIVE}])


def add(steps, primitive):
    menu(steps, SCENE, [{"do": "click", "id": ADD}, {"do": "click", "id": primitive}])
    wait(steps, 5)


def matrix(steps, pos=None, scale=None, rot=None):
    """Place the selected object with the Transform menu's sliders. `scale` is a number or [x, y, z]:
    a list turns `Uniform scale` off, and turning it back on evens the selected object's scale out
    again (a joined mesh keeps the matrix of one of its parts): bake() the matrix of each validated
    mesh, then call uniform_scale()."""
    inside = []
    if scale is not None:
        uniform = not isinstance(scale, (list, tuple))
        inside.append({"do": "set", "id": UNIFORM, "value": uniform})
        inside.append({"do": "wait", "frames": 3})
        for i, v in zip((SX, SY, SZ), [scale] if uniform else scale):
            inside.append({"do": "set", "id": i, "value": v})
    for ids, values in ((((RX, RY, RZ)), rot), ((TX, TY, TZ), pos)):
        for i, v in zip(ids, values or []):
            inside.append({"do": "set", "id": i, "value": v})
    menu(steps, TRANSFORM_MENU, inside)


def bake(steps):
    """Transform menu > Bake: the matrix goes into the vertices of the selected (validated) mesh."""
    menu(steps, TRANSFORM_MENU, [{"do": "click", "id": BAKE}, {"do": "wait", "frames": 3}])


def uniform_scale(steps):
    """The setting outlives the scene, and other scripts expect it on."""
    menu(steps, TRANSFORM_MENU, [{"do": "set", "id": UNIFORM, "value": True}])


def validate(steps):
    steps.append({"do": "click", "id": VALIDATE})
    wait(steps, 5)


def paint_all(steps, color, roughness=100):
    """Paint the selected (validated) mesh with one matte color: the hex field of the color popup."""
    menu(steps, PAINT_MENU, [
        {"do": "set", "id": ROUGHNESS, "value": roughness}, {"do": "set", "id": METALNESS, "value": 0},
        {"do": "click", "id": COLOR}, {"do": "wait", "frames": 5},
        {"do": "click", "id": PICKER_HEX}, {"do": "wait", "frames": 5},
        {"do": "type", "input": color, "enter": True}, {"do": "wait", "frames": 5},
        {"do": "click", "id": PICKER_CLOSE}, {"do": "wait", "frames": 3},
        {"do": "click", "id": PAINT_ALL}, {"do": "wait", "frames": 5}])


def terrain(steps):
    """Replace the default sphere with the terrain."""
    menu(steps, SCENE, [{"do": "click", "id": DELETE}, {"do": "wait", "frames": 3},
                        {"do": "click", "id": ADD}, {"do": "click", "id": ADD_PLANE}])
    wait(steps, 5)
    steps.append({"do": "set", "id": XDIVISION, "value": 120})
    validate(steps)
    # hills: broad Brush strokes from above, the front left stays flat
    steps.append(dict({"do": "camera"}, **TOP))
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    wait(steps, 3)
    steps.append({"do": "set", "id": BRUSH, "value": True})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "set", "id": RADIUS, "value": 150})
    steps.append({"do": "set", "id": INTENSITY, "value": 0.3})
    wait(steps, 3)
    for a, b in HILLS:
        n = 30
        steps.append({"do": "drag", "points": [[a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n]
                                               for i in range(n + 1)]})
    paint_all(steps, SAND)


# strokes in the top view (px): a long ridge at the back, a mound on the right, a low one front right
HILLS = [([300, 190], [560, 250]), ([330, 200], [520, 240]), ([560, 250], [700, 200]),
         ([850, 420], [900, 560]), ([860, 450], [890, 520]),
         ([640, 700], [760, 740])]
