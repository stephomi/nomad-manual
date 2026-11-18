"""Shared by the Stroke page clips recorded 2026-11-20: stroke_drag, stroke_grab, stroke_lockradius_drag,
stroke_lazy_rope, stroke_silhouette. Scene setup, the Stroke menu's positions, hand paths, and `restore`,
which puts the shared sandbox settings back (other sessions record stroke clips too). See .agents/videos.md.

    stroke_common.py restore | python3 ../../.agents/ai.py send -
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import math
import sys

from clip import min_jerk  # noqa: F401 (the clip scripts use it as sc.min_jerk)

MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]
FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
POST_ENABLED = 13907                  # the `Post Process...` checkbox of that menu
TOPO, MULTIRES_TAB, DYN_TAB = 6399, 67820, 67822
LEVEL0_AT = [80, 341]                 # first tick of the multires slider (a slider `set` doesn't change the level)
TOOLBOX = 58936
CLAY, MOVE, DRAG, CREASE = 67742, 67744, 67745, 67754
SYM, RADIUS, INTENSITY, SUB = 56799, 56725, 56745, 57353
UNDO, WIREFRAME = 59988, 46039
STROKE, STROKE_PANEL = 19331, 19318
MODE_DRAG, MODE_GRAB, MODE_LOCK = 67909, 67910, 67911  # stroke types of Move and Drag
SILHOUETTE, LAZY_ROPE = 19569, 19423
DYN_SHORTCUT = 48842                  # left toolbar, under Sym, once DynTopo has been enabled on the mesh
WINDOW = [1200, 900]
HOME_Z = 3.359210729598999            # camera distance of a new scene (pivot at the origin)

# where the clips click
STROKE_AT = [825, 25]                 # Stroke menu, top bar
DRAG_AT, GRAB_AT, LOCK_AT = [862, 540], [965, 540], [1068, 540]  # Move's and Drag's stroke types
SILHOUETTE_AT = [1101, 686]           # its checkbox, in Move's Stroke tab
DYN_SHORTCUT_AT = [25, 150]
START = [1010, 640]                   # resting pointer, background right of the model
REST = [1085, 760]                    # parked for the look around

# stroke_drag and stroke_grab make the same two pulls on the same sphere: only the stroke type differs
SPHERE_VIEW = [0.04, 0.1, 4.03]       # the sphere a little smaller and lower (center 580,500): room to pull
PULL_RIGHT = [[720, 390], [810, 330], [870, 390], [950, 350], [1000, 260], [960, 190]]
PULL_LEFT = [[1160 - x, y] for x, y in PULL_RIGHT]  # mirrored around the sphere's center


def new_scene(c):
    """Files > New, menus closed, the post process as videos.md wants it."""
    steps = c.steps
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    c.wait(5)
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    # a new scene has the post process off (videos.md wants it off): made sure of, and the render resolution
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ENABLED, "value": False})
    steps.append({"do": "set", "id": POST, "value": False})
    steps.append({"do": "set", "id": WIREFRAME, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": SYM, "value": False})  # symmetry draws a mirrored ring even over the UI


def low_sphere(c):
    """The new scene's sphere at its lowest level (6146 vertices): its wireframe reads at the page's size,
    and with one level left DynTopo doesn't warn about losing the others."""
    steps = c.steps
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": MULTIRES_TAB})
    c.wait(3)
    c.tap(LEVEL0_AT)
    c.wait(5)
    steps.append({"do": "click", "text": "Delete higher"})
    c.wait(5)
    steps.append({"do": "set", "id": TOPO, "value": False})


def tool(c, tool_id, radius, intensity, mode=None):
    """Select a tool and give it the clip's settings (each tool keeps its own; the sandbox shares them)."""
    steps = c.steps
    steps.append({"do": "set", "id": tool_id, "value": True})
    c.wait(3)
    steps.append({"do": "set", "id": RADIUS, "value": radius})
    steps.append({"do": "set", "id": INTENSITY, "value": intensity})
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": STROKE, "value": True})
    c.wait(3)
    steps.append({"do": "click", "text": "Stroke", "type": "radio_option", "in": STROKE_PANEL})
    steps.append({"do": "scroll", "id": STROKE_PANEL, "to": 0})
    c.wait(3)
    if mode:
        pick_mode(steps, mode)
    steps.append({"do": "set", "id": SILHOUETTE, "value": False})
    steps.append({"do": "set", "id": STROKE, "value": False})


def pick_mode(steps, mode):
    """A stroke type of Move or Drag, by id (the Stroke tab must show). Through another one first: a tap on
    the active type could open its options."""
    steps.append({"do": "click", "id": MODE_DRAG if mode == MODE_GRAB else MODE_GRAB})
    steps.append({"do": "click", "id": mode})


def park(c):
    """End of setup: the pointer glides to its resting place, top bar buttons lose their glow."""
    c.steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.pos = list(START)
    c.wait(90)
    c.steps.append({"do": "stats"})


def view(c, translation, rotation=(0, 0, 0, 1)):
    """An absolute view around the origin. Also re-sent before a camera path: a press moves the orbit pivot."""
    c.steps.append({"do": "camera", "pivot": [0, 0, 0], "rotation": list(rotation), "translation": list(translation)})


def catmull(pts, u):
    """Point at u (0..1) on a Catmull-Rom curve through pts."""
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def glide(t, a=0.06, d=0.15):
    """Progress of a long stroke: up to speed at once, steady, a soft landing. Both ends keep some speed, or
    a recorded stroke counts as a long press (start) or snaps into a curve (end): see videos.md."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def winding(way, n, profile=glide):
    """n+1 points along the Catmull-Rom curve through the waypoints, at the profile's speed along its
    length (the curve's own parameter would rush the long spans)."""
    m = 400
    pts = [catmull(way, i / m) for i in range(m + 1)]
    acc = [0.0]
    for a, b in zip(pts, pts[1:]):
        acc.append(acc[-1] + math.dist(a, b))
    out, i = [], 0
    for k in range(n + 1):
        d = profile(k / n) * acc[-1]
        while i < m - 1 and acc[i + 1] < d:
            i += 1
        f = (d - acc[i]) / max(acc[i + 1] - acc[i], 1e-9)
        out.append([round(pts[i][j] + (pts[i + 1][j] - pts[i][j]) * f, 1) for j in range(2)])
    return out


def pull(c, way, n, profile=glide, rest=22):
    """Glide to the first waypoint, rest, one drag through the others."""
    c.go(way[0]); c.wait(12)
    c.steps.append({"do": "drag", "points": winding(way, n, profile)})
    c.pos = list(way[-1])
    c.wait(rest)


def begin(c, mode, name):
    """`record [name]` records; `dry` plays the same steps unrecorded (a capture is added by `end`)."""
    if mode == "record":
        c.steps.append({"do": "record", "to": name})


def end(c, mode):
    c.steps.append({"do": "record"} if mode == "record" else {"do": "capture", "converge": False})
    c.steps.append({"do": "stats"})


def restore(c):
    """Defaults back for the settings these clips change: stroke types, intensities, stabilizer,
    silhouette, DynTopo, wireframe. On a new scene's sphere with one level (no multires warning from
    DynTopo)."""
    steps, wait = c.steps, c.wait
    new_scene(c)
    low_sphere(c)
    for tool_id, mode, intensity in ((MOVE, MODE_GRAB, 0.5), (DRAG, MODE_DRAG, 1)):
        steps.append({"do": "set", "id": tool_id, "value": True})
        wait(3)
        steps.append({"do": "set", "id": INTENSITY, "value": intensity})
        steps.append({"do": "set", "id": STROKE, "value": True})
        wait(3)
        steps.append({"do": "click", "text": "Stroke", "type": "radio_option", "in": STROKE_PANEL})
        steps.append({"do": "scroll", "id": STROKE_PANEL, "to": 0})
        wait(3)
        pick_mode(steps, mode)
        steps.append({"do": "set", "id": SILHOUETTE, "value": False})
        steps.append({"do": "set", "id": STROKE, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 300})
    wait(3)
    steps.append({"do": "set", "id": CREASE, "value": True})
    wait(3)
    steps.append({"do": "set", "id": INTENSITY, "value": 0.8})
    steps.append({"do": "set", "id": STROKE, "value": True})
    wait(3)
    steps.append({"do": "set", "id": LAZY_ROPE, "value": 0})
    steps.append({"do": "set", "id": STROKE, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    wait(3)
    steps.append({"do": "set", "id": CLAY, "value": True})
    # DynTopo: its left toolbar shortcut (shown while `Enabled` is checked) keeps its own on/off state,
    # on by default; then `Enabled` off
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": DYN_TAB})
    wait(3)
    steps.append({"do": "set", "text": "Enabled", "value": True})
    wait(5)
    steps.append({"do": "set", "id": DYN_SHORTCUT, "value": True})
    steps.append({"do": "set", "text": "Enabled", "value": False})
    steps.append({"do": "click", "id": MULTIRES_TAB})
    steps.append({"do": "set", "id": TOPO, "value": False})
    steps.append({"do": "stats"})


if __name__ == "__main__" and sys.argv[1:] == ["restore"]:
    from clip import Clip
    clip = Clip(START)
    restore(clip)
    print(clip.json())
