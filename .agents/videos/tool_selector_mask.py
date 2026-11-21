#!/usr/bin/env python3
"""docs/videos/tool_selector_mask.mp4: the Mask tool with shapes (the former Selection Mask tool). On the
boring head, the stroke popup of the left toolbar picks `Lasso`, `Rect` and `Ellipse` in turn, each drawn
shape masks the area inside it; then `Unmask` with a `Rect` erases a band across the masks. Post process
off and the scene brightened: boringhead.py. See .agents/videos.md.

Prints the JSON steps for `ai.py send -`:
    tool_selector_mask.py setup | python3 ../nomad/.agents/ai.py send -
    tool_selector_mask.py record [name] | python3 ../nomad/.agents/ai.py send - 900
Widget ids are the 2026-11-19 build's: check them with `find` after a rebuild."""
import sys

from boringhead import PROJECT, look
from clip import Clip

SHADING, SHADING_PANEL, LIGHT_ICONS = 9959, 9946, 11359
SCENE, SCENE_ICONS = 3326, [4058, 4060]  # mirror and camera gizmos in the viewport
LAYERS = 33760
TOOLBOX = 58936
CLAY, MASK, MASK_AT = 67742, 67748, [1170, 476]
SYM, SUB, UNMASK_AT = 56799, 57353, [25, 477.5]  # the Unmask button's exact center
STROKE_BUTTON = 56703
STROKE_DOT_AT, STROKE_SHAPE_AT = [25, 190], [25, 221]  # the stroke button moves down once a shape is picked
POPUP = {"Dot": [98, 86], "Lasso": [173, 288], "Rect": [173, 408], "Ellipse": [98, 462]}
VIEW = {"pivot": [-0.15, -0.1, 0], "rotation": [-0.0553415, -0.6072785, 0.042465, 0.7914208],
        "translation": [0.05, 0.2, 3.2]}
WINDOW = [1200, 885]                  # what macOS clamped [1200, 900] to when the clip was written
START = [1010, 700]

c = Clip(START)
steps = c.steps


def pick(p):
    """Tool buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def toggle(widget, value):
    """A sticky button turned on or off for sure: a recorded tap's length in wall-clock time varies, and a
    long one only holds the mode until release. Glide onto the button's center, then `set` it there: the
    click by id lands where the pointer already is."""
    c.go(UNMASK_AT); c.wait(c.rng.randint(17, 23))
    steps.append({"do": "set", "id": widget, "value": value})
    c.wait(20)


def shape(name, button):
    """The stroke button opens the popup of brush strokes and shapes: pick one."""
    pick(button)
    c.wait(10)
    pick(POPUP[name])


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def draw(points):
    """A shape drag. No slow landing: shapes have `Edit: Hold`, a still pointer at the end would keep the
    shape for editing instead of applying it."""
    c.go(points[0]); c.wait(10)
    steps.append({"do": "drag", "points": [[round(v, 1) for v in p] for p in points]})
    c.pos = list(points[-1])
    c.wait(30)


def lasso(way, n):
    ease = lambda t: 0.5 * t + 0.5 * t * t  # quick start, no stop: see draw()
    draw([catmull(way, ease(i / n)) for i in range(n + 1)])


def diagonal(a, b, n):
    ease = lambda t: t * (2 - t) * 0.35 + t * 0.65
    draw([[a[0] + (b[0] - a[0]) * ease(i / n), a[1] + (b[1] - a[1]) * ease(i / n)] for i in range(n + 1)])


if sys.argv[1] == "setup":
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    c.wait(30)
    for menu in (LAYERS, 17912, SCENE, SHADING, 6399):  # no menu left open from an earlier take
        steps.append({"do": "set", "id": menu, "value": False})
    steps.extend(look())
    steps.append({"do": "set", "id": SHADING, "value": True})
    c.wait(5)
    steps.append({"do": "scroll", "id": SHADING_PANEL, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": LIGHT_ICONS, "value": False})
    steps.append({"do": "set", "id": SHADING, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": True})
    c.wait(5)
    for i in SCENE_ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "set", "id": SCENE, "value": False})
    steps.append(dict({"do": "camera"}, **VIEW))
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": MASK, "value": True})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "click", "id": STROKE_BUTTON})      # back to the Dot brush, whatever a take left
    c.wait(10)
    c.tap(POPUP["Dot"], 3)
    c.wait(10)
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 25})  # the rings at rest, as
    steps.append({"do": "set", "id": CLAY, "value": True})  # other takes leave theirs; the clip picks Mask
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 42})
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_selector_mask"})
    c.wait(25)
    c.go(MASK_AT); c.wait(c.rng.randint(17, 23))      # the tool by `set`, as toggle() does: see there
    steps.append({"do": "set", "id": MASK, "value": True})
    c.wait(24)
    shape("Lasso", STROKE_DOT_AT)
    lasso([[440, 290], [500, 240], [590, 245], [630, 290], [600, 335], [560, 320], [510, 365], [445, 345], [440, 290]], 75)
    shape("Rect", STROKE_SHAPE_AT)
    diagonal([670, 235], [795, 365], 40)
    shape("Ellipse", STROKE_SHAPE_AT)
    diagonal([600, 640], [740, 730], 40)
    shape("Rect", STROKE_SHAPE_AT)
    toggle(SUB, True)                                  # Unmask works with shapes too
    diagonal([420, 282], [810, 340], 50)
    toggle(SUB, False)
    c.go(START); c.wait(40)
    steps.append({"do": "record"})
print(c.json())
