"""The Getting Started set, docs/videos/gettingstarted_01.mp4 to _11.mp4: one plain sphere (Files > New)
sculpted into a simple cartoon face, symmetry on, front view, one idea per clip, the face building up
from clip to clip. The page is written for a touch screen: every input is a finger (`touch`), one for
strokes, slider drags, taps and the orbit, two for the pinch, the pan and the undo tap. A finger's
marker only shows while it touches, so taps are paced to read: a pause, a press held a few frames, a
pause for the result. See .agents/videos.md.

Each clip has its own script, gettingstarted_NN.py, that calls `main(NN)`:
    gettingstarted_NN.py setup | python3 ../nomad/.agents/ai.py send -
    gettingstarted_NN.py record [name] | python3 ../nomad/.agents/ai.py send - 900
`setup` rebuilds the scene from scratch and replays clips 1 to NN-1 (not recorded), so any clip can
be retaken alone. Recording the set in one go also works: setup of 01, then each `record` in turn
(each clip starts from the home camera, as the replay does).

Widget ids and positions are the 2026-11-20 build's: check them with `find` after a rebuild."""
import sys

from clip import Clip, min_jerk

FILES, NEW, YES = 108, 146, 147
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
TOOLBOX, CLAY, SMOOTH_TOOL, PAINT = 58936, 67742, 67747, 67749
SYM, RADIUS, INTENSITY, SUB, SMOOTH = 56799, 56725, 56745, 57353, 57354
PAINT_SLIDERS = (55532, 55552)        # Paint has its sliders in an extra column
MATERIAL, PICKER = 49853, 49959       # Paint: the material button (opens the popup), the popup's color swatch
PAINT_POPUP = 49839
# Files > New keeps the camera of the previous scene: set it. The sphere is then centered at 600,442
HOME = {"pivot": [0, 0, 0], "rotation": [0, 0, 0, 1], "translation": [0, 0, 3.0]}
WINDOW = [1200, 900]
REST = [1040, 760]                    # empty space, bottom right: a finger there only turns the camera

# left toolbar (Clay): sliders are relative drags, up = more
RADIUS_X, RADIUS_Y = 25, 205
INTENSITY_X, INTENSITY_Y = 25, 365
SUB_AT, SMOOTH_AT = [25, 478], [25, 542]   # Sub turns into Erase with Paint
UNDO_AT = [25, 860]                   # bottom bar
PAINT_AT = [1170, 540]                # toolbox, scrolled to the top
MATERIAL_AT = [25, 795]               # left toolbar, bottom: the paint material, opens the Paint popup
POPUP_CLOSE = [401, 85]
# Paint popup scrolled to its end (the picker sits below the fold): hue bar (red at the top, blue a third
# down), then the color square, near its saturated top right corner
HUE_X, BLUE_Y = 338, 561
SQUARE_AT = [285, 506]


def catmull(pts, u):
    k = len(pts) - 1
    i = min(int(u * k), k - 1)
    t = u * k - i
    p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k)]
    return [0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t * t * t) for j in range(2)]


def r(p):
    return [round(p[0], 1), round(p[1], 1)]


class Touch(Clip):
    """Finger input on top of clip.py's pacing."""

    def touch(self, pts, pts2=None):
        step = {"do": "touch", "points": [r(p) for p in pts]}
        if pts2:
            step["points2"] = [r(p) for p in pts2]
        self.steps.append(step)
        self.pos = list(pts[-1])

    def tap(self, p, hold=3, after=22):
        """A finger tap: a pause so the eye can get there, a press held `hold` frames, the result.
        Left toolbar shortcuts (Sub, Smooth, Erase) and tool buttons treat a long press as hold-to-use:
        keep `hold` short (2 to 4)."""
        self.wait(self.rng.randint(14, 20))
        self.touch([p] * hold)
        self.wait(after)

    def stroke(self, way, n, rest=16, land=2):
        """One finger stroke through the waypoints, eased at both ends."""
        self.wait(self.rng.randint(8, 12))
        self.touch([way[0]] * land + [catmull(way, min_jerk(i / n)) for i in range(1, n + 1)])
        self.wait(rest)

    def loop(self, p, rx, ry, n, turns=1.5, rest=16):
        """A small round scrub around p, as you'd rub a cheek on."""
        import math
        way = [[p[0] + rx * math.cos(2 * math.pi * turns * i / 12 + 2.4), p[1] + ry * math.sin(2 * math.pi * turns * i / 12 + 2.4)]
               for i in range(13)]
        self.stroke(way, n, rest)

    def slide(self, x, y, dy, n=34):
        """Press a left toolbar slider, hold, slide it by dy (up is negative), hold, lift."""
        self.wait(self.rng.randint(14, 20))
        a = [x, y]
        pts = [a] * 6 + [[x + 1.5 * min_jerk(i / n), y + dy * min_jerk(i / n)] for i in range(1, n + 1)]
        self.touch(pts + [pts[-1]] * 8)
        self.wait(18)

    def drag2(self, a, b, da, db, n):
        """Two fingers, pressed at a and b, moved by da and db. A pinch whose midpoint stays put does
        nothing in Nomad (the camera waits for the mean position to move): real hands drift.
        Two fingers held still for 500 ms (wall clock, and recorded frames are slow) start the undo
        history scrub: they set off at once, quick at first, and land slowly."""
        self.wait(self.rng.randint(12, 18))

        def ease(t):
            return 1 - (1 - t) ** 3

        pa = [[a[0] + da[0] * ease(i / n), a[1] + da[1] * ease(i / n)] for i in range(n + 1)]
        pb = [[b[0] + db[0] * ease(i / n), b[1] + db[1] * ease(i / n)] for i in range(n + 1)]
        self.touch(pa + [pa[-1]] * 2, pb + [pb[-1]] * 2)
        self.wait(20)


# ---- the clips: each one starts from the home camera and the previous clip's sculpt ----

def clip01(c):
    """First strokes with Clay, symmetry on: cheeks, then a brow ridge (both sides at once)."""
    c.wait(30)
    c.loop([505, 500], 26, 18, 46)
    c.loop([508, 496], 22, 16, 40, rest=20)
    c.stroke([[597, 372], [560, 360], [518, 360], [480, 376]], 44)
    c.stroke([[594, 380], [556, 368], [516, 368], [482, 384]], 40, rest=40)


def clip02(c):
    """Radius slider: bigger, a broad stroke for the chin; smaller, a thin lower lip."""
    c.wait(25)
    c.slide(RADIUS_X, RADIUS_Y, -60)
    c.stroke([[600, 618], [565, 612], [528, 592]], 40, rest=22)
    c.slide(RADIUS_X, RADIUS_Y - 60, 110, n=40)
    c.stroke([[600, 574], [574, 572], [548, 563]], 34, rest=40)


def clip03(c):
    """Intensity slider: weak, a nose stroke barely shows; strong, the nose comes out."""
    c.wait(25)
    c.slide(INTENSITY_X, INTENSITY_Y, 70)
    c.stroke([[600, 418], [601, 446], [600, 480]], 36, rest=22)
    c.slide(INTENSITY_X, INTENSITY_Y + 70, -150, n=44)
    c.stroke([[600, 418], [601, 446], [600, 480]], 36, rest=14)
    c.loop([600, 482], 10, 7, 34, rest=40)


def clip04(c):
    """Sub: carve the eye sockets and the mouth, then back to adding."""
    c.wait(25)
    c.tap(SUB_AT)
    c.loop([530, 424], 20, 13, 44)
    c.loop([531, 425], 16, 11, 38)
    c.loop([530, 424], 12, 8, 32, rest=18)
    c.stroke([[600, 549], [572, 547], [544, 538], [524, 524]], 40, rest=18)
    c.tap(SUB_AT)
    c.wait(30)


def clip05(c):
    """Smooth: soften the cheeks and the brow, then back to sculpting. The shortcut keeps the current
    radius (Clay's, small since clip 02) and has its own intensity (Smooth's, full in setup)."""
    c.wait(25)
    c.tap(SMOOTH_AT)
    c.loop([505, 498], 40, 30, 56)
    c.loop([505, 498], 30, 22, 46)
    c.stroke([[598, 366], [558, 356], [518, 358], [478, 374]], 40, rest=10)
    c.stroke([[480, 384], [518, 370], [558, 370], [598, 380]], 40, rest=18)
    c.tap(SMOOTH_AT)
    c.wait(30)


def clip06(c):
    """Orbit: one finger dragged in empty space turns the view, and back."""
    c.wait(30)
    a = REST
    way = [a, [1010, 744], [970, 722], [952, 714]]
    c.stroke(way, 66, rest=30, land=3)
    back = [way[-1], [982, 724], [1018, 748], a]
    c.stroke(back, 70, rest=40, land=3)


def clip07(c):
    """Pinch: fingers together zoom out, apart zoom back in."""
    c.wait(30)
    c.drag2([470, 520], [760, 380], [95, -40], [-90, 47], 50)
    c.wait(10)
    c.drag2([560, 482], [668, 425], [-92, 38], [94, -44], 55)
    c.wait(30)


def clip08(c):
    """Pan: two fingers dragged together slide the view, and back."""
    c.wait(30)
    c.drag2([540, 520], [680, 470], [170, 60], [168, 62], 55)
    c.wait(10)
    c.drag2([720, 585], [855, 530], [-170, -60], [-168, -62], 55)
    c.wait(30)


def clip09(c):
    """Undo: a stray stroke, a two-finger tap takes it back; another, the undo button."""
    c.wait(25)
    c.stroke([[470, 290], [540, 270], [600, 268]], 34, rest=20)
    c.wait(10)
    c.touch([[560, 470]] * 2, [[650, 455]] * 2)   # a tap is under 230 ms, wall clock: keep it to 2 frames
    c.wait(40)
    c.stroke([[520, 640], [560, 660], [600, 664]], 32, rest=20)
    c.tap(UNDO_AT, 4, after=40)


def clip10(c):
    """Add color: Paint in the toolbox, the material at the bottom of the left toolbar opens the color
    picker, pick a blue, then paint eyes into the sockets."""
    c.wait(25)
    c.tap(PAINT_AT, 4, after=26)
    c.tap(MATERIAL_AT, 3, after=30)
    c.stroke([[250, 640], [254, 490], [258, 330]], 32, rest=24, land=3)   # swipe the popup up to its picker
    c.tap([HUE_X, BLUE_Y], 4, after=16)
    c.tap(SQUARE_AT, 4, after=26)
    c.tap(POPUP_CLOSE, 3, after=16)
    c.loop([530, 425], 9, 7, 40)
    c.loop([530, 426], 6, 5, 30, rest=40)


def clip11(c):
    """Erase: rub out the bottom of the eyes, then back to painting."""
    c.wait(25)
    c.tap(SUB_AT)
    c.stroke([[516, 434], [530, 438], [544, 434]], 30, rest=20)
    c.tap(SUB_AT)
    c.wait(30)


CLIPS = [clip01, clip02, clip03, clip04, clip05, clip06, clip07, clip08, clip09, clip10, clip11]


def post_process(steps):
    """A new scene has the post process off: only the render resolution to set."""
    steps.append({"do": "set", "id": POST, "value": True})
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST, "value": False})


def setup(n):
    steps = []
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "set", "id": FILES, "value": True})
    steps.append({"do": "click", "id": NEW})
    steps.append({"do": "click", "id": YES})
    steps.append({"do": "set", "id": FILES, "value": False})
    steps.append({"do": "wait", "frames": 5})
    post_process(steps)
    steps.append({"do": "set", "id": SYM, "value": True})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    # the Paint popup shows its color picker (the color swatch toggles it, and the state survives)
    steps.append({"do": "set", "id": PAINT, "value": True})
    steps.append({"do": "set", "id": MATERIAL, "value": True})
    steps.append({"do": "wait", "frames": 5})
    steps.append({"do": "set", "id": PICKER, "value": True})
    steps.append({"do": "scroll", "id": PAINT_POPUP, "to": 0})   # the scroll survives too
    steps.append({"do": "set", "id": MATERIAL, "value": False})
    # tool settings (they survive in the user folder), the clip starts on Clay; Sub / Erase off
    for tool, radius, intensity, sliders in ((PAINT, 22, 1.0, PAINT_SLIDERS), (SMOOTH_TOOL, 50, 1.0, (RADIUS, INTENSITY)),
                                             (CLAY, 48, 0.5, (RADIUS, INTENSITY))):
        steps.append({"do": "set", "id": tool, "value": True})
        steps.append({"do": "set", "id": sliders[0], "value": radius})
        steps.append({"do": "set", "id": sliders[1], "value": intensity})
        steps.append({"do": "set", "id": SUB, "value": False})
    steps.append({"do": "set", "id": SMOOTH, "value": False})
    for k in range(1, n):
        steps += start(k)
        c = Touch(REST, seed=k)
        CLIPS[k - 1](c)
        steps += c.steps
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "wait", "frames": 10})
    steps.append({"do": "stats"})
    return steps


def start(n):
    """Each clip starts from the home camera. The brush ring stays where the last finger left the viewport:
    the next clips start with it there (clip 02 grows it), but the first one starts clean. The setup clicks
    also left the mouse pointer (and its marker) on a button: a mouse hover out of the window hides both."""
    steps = [dict({"do": "camera"}, **HOME)]
    if n == 1:
        steps.append({"do": "drag", "points": [[1100, 700], [1300, 1000]], "hover": True})
    steps.append({"do": "wait", "frames": 300})   # unrecorded: lets the last toast ("Undo: Clay") fade
    return steps


def record(n, name):
    c = Touch(REST, seed=n)
    CLIPS[n - 1](c)
    return start(n) + [{"do": "record", "to": name}] + c.steps + [{"do": "record"}]


def main(n):
    import json
    if sys.argv[1] == "setup":
        print(json.dumps(setup(n)))
    else:
        print(json.dumps(record(n, sys.argv[2] if len(sys.argv) > 2 else "gettingstarted_%02d" % n)))
