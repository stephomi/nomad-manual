"""Shared by the Stroke page clips recorded 2026-11-20 on a fresh-scene sphere: stroke_dot, stroke_roll,
stroke_lock_radius, stroke_lock_intensity (Brush tool) and alpha_tiling (Paint tool). Scene and tool setup,
the alpha library, the Stroke menu's positions, hand paths, and `restore`, which puts the shared sandbox
settings back (other sessions record stroke clips too). See .agents/videos.md.

    stroke_modes.py restore | python3 ../nomad/.agents/ai.py send -
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. The alpha library popup
opens next to the thumbnail tap, and its cells have no name: after a setup, check the alpha in a capture
(or the first recorded frames of a take)."""
import math
import sys

MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]
FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX, CLAY, BRUSH, PAINT = 58936, 67742, 67743, 67749
SYM, RADIUS, INTENSITY, SUB = 56799, 56725, 56745, 57353
WIREFRAME = 46039
STROKE, STROKE_PANEL, STROKE_PIN = 19331, 19318, 19324
ALPHA_PANEL, ALPHA_PIN = 19996, 20002
TAB_STROKE, TAB_ALPHA = 67829, 67830
# stroke types by their label: the list is rebuilt with the tool, its ids differ from one session to the next
DOT, ROLL, LOCK_RADIUS, LOCK_INTENSITY = "Dot", "Roll", "Lock + radius", "Lock + intensity"
SURFACE, SCALING, ROTATION, TILING = 21748, 21325, 21396, 21250
X_REPEAT, Y_NONE = 21743, 21745
LIBRARY, LIBRARY_CLOSE = 20025, 20014
PAINT_MENU, PAINT_FALLOFF, COLOR_ROW, HEX, PICKER_CLOSE = 23086, 23141, 23178, 23366, 23166
WINDOW = [1200, 900]

# alpha library cells: (scroll of the library, where the cell is then)
NONE = (0, [567, 152])
SQUARE = (0, [707, 152])              # soft-edged square, Clay's default
STRIPES = (0, [637, 252])             # Kenney/Base, three diagonal stripes: rolled, they read as stitches
PENTAGON = (1040, [777, 263])         # Kenney/Base pattern_64: one pentagon, parts of four more in the corners
ALPHA_THUMB_AT = [887, 310]           # Alpha tab, scrolled to its top

# where the clips click
STROKE_AT = [825, 25]                 # Stroke menu, top bar
DOT_AT, ROLL_AT, LOCK_RADIUS_AT, LOCK_INTENSITY_AT = [849, 540], [926, 540], [1004, 540], [1081, 540]
UNDO_AT = [25, 875]
START = [1010, 640]                   # resting pointer, background right of the sphere
REST = [1085, 770]                    # parked for the look around
HOME = [0, 0, 2.9]                    # a new scene is at z 3.359: closer, the sphere fills the view


def new_scene(c, subdivide=2):
    """Files > New, menus closed, the post process as videos.md wants it, the sphere subdivided (1.57M
    faces with 2: alpha edges stay clean)."""
    steps = c.steps
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    # a new scene has the post process off: only the render resolution to set
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": WIREFRAME, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    for _ in range(subdivide):
        steps.append({"do": "action", "name": "subdivide"})
        c.wait(5)
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI


def pick_alpha(c, alpha):
    """The Alpha tab must show, scrolled to its top. The library stays open after a pick: close it."""
    scroll, at = alpha
    c.tap(ALPHA_THUMB_AT)
    c.wait(15)
    c.steps.append({"do": "scroll", "id": LIBRARY, "to": scroll})
    c.wait(20)
    c.tap(at)
    c.wait(15)
    c.steps.append({"do": "click", "id": LIBRARY_CLOSE})
    c.wait(5)


def stroke_type(name):
    """The step that picks a stroke type (the Stroke tab must show)."""
    return {"do": "click", "text": name, "type": "radio_option", "in": STROKE_PANEL}


def tool(c, button, radius, intensity, mode, alpha, tab=TAB_STROKE, pin=False):
    """Select a tool and give it the clip's stroke settings (each tool keeps its own; the sandbox shares
    them): stroke type, alpha, and the alpha options back to their defaults. Leaves the Stroke menu closed
    on `tab`, or open and pinned on it."""
    steps = c.steps
    steps.append({"do": "set", "id": button, "value": True})
    c.wait(3)
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": STROKE, "value": True})
    c.wait(5)
    steps.append({"do": "click", "id": TAB_STROKE})
    c.wait(5)
    steps.append({"do": "scroll", "id": STROKE_PANEL, "to": 0})
    steps.append({"do": "set", "id": STROKE_PIN, "value": False})
    # through Dot: Lock + intensity disables the intensity slider, Lock + radius rewrites the radius
    steps.append(stroke_type(ROLL))
    steps.append(stroke_type(DOT))
    c.wait(3)
    steps.append({"do": "set", "id": RADIUS, "value": radius})
    steps.append({"do": "set", "id": INTENSITY, "value": intensity})
    steps.append({"do": "click", "id": TAB_ALPHA})
    c.wait(5)
    steps.append({"do": "scroll", "id": ALPHA_PANEL, "to": 0})
    steps.append({"do": "set", "id": ALPHA_PIN, "value": False})
    steps.append({"do": "click", "id": SURFACE})
    steps.append({"do": "set", "id": SCALING, "value": 1})
    steps.append({"do": "set", "id": ROTATION, "value": 0})
    steps.append({"do": "set", "id": TILING, "value": 3})  # the tiling modes are disabled at 1
    steps.append({"do": "click", "id": X_REPEAT})
    steps.append({"do": "click", "id": Y_NONE})
    steps.append({"do": "set", "id": TILING, "value": 1})
    pick_alpha(c, alpha)
    steps.append({"do": "click", "id": TAB_STROKE})
    c.wait(5)
    if mode != DOT:
        steps.append(stroke_type(mode))
        c.wait(3)
    if tab != TAB_STROKE:
        steps.append({"do": "click", "id": tab})
        c.wait(5)
    if pin:
        steps.append({"do": "set", "id": ALPHA_PIN if tab == TAB_ALPHA else STROKE_PIN, "value": True})
    else:
        steps.append({"do": "set", "id": STROKE, "value": False})


def paint(c, hex_color, falloff):
    """Paint menu: the color by its hex value, and whether a stroke fades toward its edge."""
    steps = c.steps
    steps.append({"do": "set", "id": PAINT_MENU, "value": True})
    c.wait(5)
    steps.append({"do": "set", "id": PAINT_FALLOFF, "value": falloff})
    steps.append({"do": "click", "id": COLOR_ROW})
    c.wait(10)  # the picker's first opening of a session settles over a few frames: a click by id sent at
    steps.append({"do": "click", "id": HEX})  # once landed beside it, on the Metalness checkbox
    c.wait(10)
    steps.append({"do": "type", "input": hex_color})  # no id: the field is already being edited
    steps.append({"do": "click", "text": "Ok"})       # by text: the dialog is built when it first opens
    steps.append({"do": "click", "id": PICKER_CLOSE})
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})


def view(c, translation=HOME):
    """The front view around the origin. Also re-sent before a camera path: a press moves the orbit pivot."""
    c.steps.append({"do": "camera", "pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": list(translation)})


def park(c, at=START):
    """End of setup: the pointer glides to its resting place, top bar buttons lose their glow and the
    toasts (Undo, Subdivision) fade: those run on wall-clock time."""
    c.steps.append({"do": "drag", "points": [[780, 450], list(at)], "hover": True})
    c.pos = list(at)
    c.wait(200)
    c.steps.append({"do": "stats"})


def glide(t, a=0.06, d=0.15):
    """Progress of a long stroke: up to speed at once, steady, a soft landing. Both ends keep some speed, or
    a recorded stroke counts as a long press (start) or snaps into a curve (end): see videos.md."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def catmull(pts, u):
    """Point at u (0..1) on a Catmull-Rom curve through pts."""
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def along(pts, n, profile=glide):
    """n+1 points along a polyline, at the profile's speed along its length."""
    acc = [0.0]
    for a, b in zip(pts, pts[1:]):
        acc.append(acc[-1] + math.dist(a, b))
    out, i = [], 0
    for k in range(n + 1):
        d = profile(k / n) * acc[-1]
        while i < len(pts) - 2 and acc[i + 1] < d:
            i += 1
        f = (d - acc[i]) / max(acc[i + 1] - acc[i], 1e-9)
        out.append([round(pts[i][j] + (pts[i + 1][j] - pts[i][j]) * f, 1) for j in range(2)])
    return out


def winding(way, n):
    """One drag along the Catmull-Rom curve through the waypoints."""
    return along([catmull(way, i / 400) for i in range(401)], n)


def wave(x0, x1, y, amplitude, n):
    """One drag along a full sine period from x0 to x1: up first when x grows."""
    return along([[x0 + (x1 - x0) * i / 300, y - amplitude * math.sin(2 * math.pi * i / 300)]
                  for i in range(301)], n)


def draw(c, pts, rest=22):
    """Glide to the first point, rest, one drag through the others."""
    c.go(pts[0]); c.wait(12)
    c.steps.append({"do": "drag", "points": pts})
    c.pos = list(pts[-1])
    c.wait(rest)


def stamp(c, p, d, n=None, rest=24):
    """A Lock + radius / Lock + intensity stamp: press at p, held a moment, then drag by d. The stamp
    grows (or rises) and turns with the drag. The drag keeps some speed to its end: a soft landing
    (within 7 px for 0.7 s) turns the stamp into a snapped stroke, with its Stroke snap bar."""
    if n is None:
        n = int(18 + math.hypot(*d) / 5)
    c.go(p); c.wait(10)
    c.tap(p, 2)
    c.steps[-1]["points"] += c.path(p, [p[0] + d[0], p[1] + d[1]], n, 0.0, glide)[1:]
    c.pos = [p[0] + d[0], p[1] + d[1]]
    c.wait(rest)


def look(c, frames=170, yaw=((0.55, 24), (1, 18)), pitch=((0.5, -8), (1, -5)), translation=HOME):
    """Park the pointer and look around the sphere in one move."""
    c.go(REST); c.wait(10)
    view(c, translation)  # the strokes moved the orbit pivot onto the surface: back to the center, same view
    c.camera(frames, yaw=list(yaw), pitch=list(pitch))


def begin(c, argv, name):
    """Start recording. A hover on the spot first: the user's real mouse, moved over the Nomad window since
    the setup, takes the brush ring with it (the touch marker stays), and frame 0 is the poster."""
    c.steps.append({"do": "drag", "points": [list(c.pos), list(c.pos)], "hover": True})
    c.steps.append({"do": "record", "to": argv[2] if len(argv) > 2 else name})


def end(c):
    c.steps.append({"do": "record"})


def restore(c):
    """The settings these clips change, back to what the sandbox had: Brush on Dot with no alpha, Paint on
    Dot with the square alpha, its falloff and the yellow of its default material. Clay too (Dot, its
    square alpha: the tests for these clips changed it), left selected."""
    new_scene(c, subdivide=0)
    tool(c, PAINT, 70, 1, DOT, SQUARE)
    paint(c, "e7bc59", True)
    tool(c, BRUSH, 50, 0.5, DOT, NONE)
    tool(c, CLAY, 80, 0.5, DOT, SQUARE)
    c.steps.append({"do": "stats"})


if __name__ == "__main__" and sys.argv[1:] == ["restore"]:
    from clip import Clip
    clip = Clip(START)
    restore(clip)
    print(clip.json())
