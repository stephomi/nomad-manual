"""Shared by tip_pimples_before.py and tip_pimples_stable_smooth.py: the first two clips of the tips.md
section "Remove lumps or 'pimples' from a voxel remesh operation". A fresh scene (post process off, as
a new user sees it), its sphere painted as polished metal: the pimples are low bumps that a matte
material hides, and the default environment's two light panels bend on them (the page's "easier to see
with a high contrast matcap material"). See .agents/videos.md for the workflow. Widget ids are the
2026-11-20 build's (check them with `find` after a rebuild).

Sandbox settings are shared between sessions: the Paint menu's roughness and metalness, changed for
`Paint all`, are put back by setup (20 % and 0 %), and `Stable smoothing` by restore()."""
import math

from clip import Clip

# top bar buttons: a menu stays open across a new scene. The second list is disabled unless a mesh is
# selected with a sculpting tool, and a `set` on a disabled widget is an error
MENUS = [108, 3326, 9959, 13905, 18138, 17912, 40184, 35769]
MESH_MENUS = [6399, 11516, 33760, 33331, 32972, 23086, 19331, 27845]
FILES, NEW, YES = 108, 146, 147
TOPO, POST, POST_PANEL, RENDER_RES = 6399, 13905, 13892, 13908
CAMERA, PERSPECTIVE, FOV = 17912, 18085, 17914
SYM, SUB = 56799, 57353
CLAY, SMOOTH, PAINT, TOOLBOX = 67742, 67747, 67749, 58936
VOXEL_TAB, VOXEL_RES, VOXEL_MULTIRES, VOXEL_REMESH = 67821, 6814, 6835, 6954
TOOL_MENU, STABLE = 28318, 28518             # the Smooth tool's settings, `Stable smoothing`
PAINT_MENU, ROUGHNESS, METALNESS, ALL_ROUGHNESS, ALL_METALNESS = 23086, 23367, 23387, 23479, 23480
MATERIAL, SMOOTH_SHADING = 11516, 12425      # Material menu, Smooth shading: Yes
WINDOW = [1200, 900]
CENTER = [600, 450]                          # the sphere on screen
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 1.3]}  # a new scene is at 1.758
R = 330                                      # its radius on screen at HOME
START = [1030, 720]
SMOOTH_AT = [1170, 410]
RESOLUTION = 140                             # voxel resolution
RADIUS, INTENSITY = 150, 30                  # Smooth: "Smooth with high intensity". 300 % erases the swirl
#                                              and leaves bumps too low to see, they grow with more smoothing
TOPO_AT, TOOL_MENU_AT = [175, 25], [775, 25]
PASS = 175                                   # frames of one smoothing pass


def sliders(steps, radius, intensity):
    """By icon name: a tool can show them unlabelled."""
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": radius})
    steps.append({"do": "set", "text": "intensity.png", "type": "slider", "value": intensity})


def swirl_sphere(c):
    """A new scene, its sphere turned to polished metal, with a crease swirl."""
    steps = c.steps
    steps.append({"do": "window", "size": WINDOW})
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)                                # a top bar button reads as on a moment after its menu closes:
    steps.append({"do": "set", "id": FILES, "value": True})   # without the waits a `set` can skip its click
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
    steps.append({"do": "set", "id": CAMERA, "value": True})  # Files > New keeps the previous scene's camera,
    c.wait(5)                                                 # projection and field of view: HOME is for these
    steps.append({"do": "click", "id": PERSPECTIVE})
    steps.append({"do": "set", "id": FOV, "value": 48.85})    # (Dracula's, the project loaded before the takes)
    steps.append({"do": "set", "id": CAMERA, "value": False})
    c.wait(20)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    c.wait(5)
    steps.append({"do": "set", "id": CLAY, "value": True})    # the tool survives a new scene (View, Gizmo...)
    c.wait(5)
    for i in MESH_MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": SYM, "value": False})    # Files > New turns it back on
    # polished metal
    steps.append({"do": "set", "id": PAINT, "value": True})
    steps.append({"do": "set", "id": PAINT_MENU, "value": True})
    c.wait(5)
    steps.append({"do": "set", "id": ROUGHNESS, "value": 25})
    steps.append({"do": "set", "id": METALNESS, "value": 100})
    steps.append({"do": "click", "id": ALL_ROUGHNESS})
    steps.append({"do": "click", "id": ALL_METALNESS})
    steps.append({"do": "set", "id": METALNESS, "value": 0})  # as found: other sessions paint too
    steps.append({"do": "set", "id": ROUGHNESS, "value": 20})
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})
    # the swirl: a crease spiral
    steps.append({"do": "action", "name": "tool_crease"})
    sliders(steps, 40, 1)
    steps.append({"do": "set", "id": SUB, "value": False})
    # at constant speed (~9 px a frame): a slow start near the center stays within 7 px for 0.7 s when
    # the machine is busy, which snaps the stroke into a curve
    n, r0, k = 280, 20, 235 / (6 * math.pi)                   # radius r0 + k * angle, three turns
    length = r0 * 6 * math.pi + k * (6 * math.pi) ** 2 / 2
    pts = []
    for i in range(n + 1):
        a = (-r0 + math.sqrt(r0 * r0 + 2 * k * length * i / n)) / k
        pts.append([round(CENTER[0] + (r0 + k * a) * math.cos(a), 1),
                    round(CENTER[1] + (r0 + k * a) * math.sin(a), 1)])
    steps.append({"do": "drag", "points": pts})
    steps.append({"do": "set", "id": SMOOTH, "value": True})
    steps.append({"do": "set", "id": TOOL_MENU, "value": False})  # disabled with Clay: it has no settings
    sliders(steps, RADIUS, INTENSITY)
    steps.append({"do": "set", "id": SUB, "value": False})    # Relax off
    steps.append({"do": "set", "id": CLAY, "value": True})
    steps.append({"do": "set", "text": "radius.png", "type": "slider", "value": 70})  # the ring of frame 0
    steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "click", "id": VOXEL_TAB})
    steps.append({"do": "set", "id": VOXEL_RES, "value": RESOLUTION})
    steps.append({"do": "set", "id": VOXEL_MULTIRES, "value": 0})
    steps.append({"do": "set", "id": TOPO, "value": False})
    c.wait(20)
    steps.append({"do": "set", "id": MATERIAL, "value": True})  # facets would break up the reflections
    c.wait(5)
    steps.append({"do": "click", "id": SMOOTH_SHADING})
    steps.append({"do": "set", "id": MATERIAL, "value": False})
    steps.append(dict({"do": "camera"}, **HOME))              # the stroke moved the orbit pivot


def smooth_tool(c, stable_on):
    """Select Smooth and set `Stable smoothing` in its settings (unrecorded)."""
    steps = c.steps
    steps.append({"do": "set", "id": SMOOTH, "value": True})
    c.wait(5)
    steps.append({"do": "set", "id": TOOL_MENU, "value": True})
    c.wait(5)
    steps.append({"do": "set", "id": STABLE, "value": stable_on})
    steps.append({"do": "set", "id": TOOL_MENU, "value": False})
    c.wait(20)


def remesh(c, multires=3):
    """Topology > Voxel: Build multiresolution, Remesh (unrecorded)."""
    steps = c.steps
    steps.append({"do": "set", "id": TOPO, "value": True})
    steps.append({"do": "set", "id": VOXEL_MULTIRES, "value": multires})
    steps.append({"do": "click", "id": VOXEL_REMESH})
    steps.append({"do": "click", "text": "Ok"})               # the sphere had multires levels
    c.wait(5)
    steps.append({"do": "set", "id": TOPO, "value": False})


def glide(t, a=0.05, d=0.15):
    """Progress of a long stroke: up to speed at once, steady, a soft landing (an eased start counts as
    a long press while recording, see tool_smooth.py)."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def zigzag():
    """Waypoints of one scrubbing stroke over the whole swirl, every point well inside the sphere."""
    way = []
    for k, dy in enumerate(range(-200, 201, 80)):
        half = math.sqrt((R - 70) ** 2 - dy ** 2)
        xs = [CENTER[0] - half, CENTER[0] + half]
        if k % 2:
            xs.reverse()
        way += [[x, CENTER[1] + dy] for x in xs]
    return way


def scrub(c, way, n):
    c.go(way[0]); c.wait(12)
    c.steps.append({"do": "drag", "points": [[round(v, 1) for v in catmull(way, glide(i / n))]
                                             for i in range(n + 1)]})
    c.pos = list(way[-1])


def pick(c, p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


def smooth_hard(c):
    """Two scrubbing passes over the swirl, back to the resting place."""
    for _ in range(2):
        scrub(c, zigzag(), PASS)
        c.wait(10)
    c.go(START); c.wait(15)


def look_around(c):
    """Strokes moved the orbit pivot onto the surface: back to the center (same view), then one move
    that slides the reflections over the surface."""
    c.steps.append(dict({"do": "camera"}, **HOME))
    c.camera(200, yaw=[(0.5, 28), (1, 10)], pitch=[(0.45, 12), (1, 4)], dolly=[(0.6, 0.86), (1, 0.88)])
