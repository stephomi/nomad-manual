#!/usr/bin/env python3
"""docs/videos/tool_transform.mp4: Transform, with fingers, scattering rocks over a small terrain. One
finger on the rock slides it over the surface (`Snap` is on). `Clone` in the left toolbar, and the next
drag pulls a copy out; two fingers on it, spread apart, scale it up. `Clone` again, drag the copy away;
`Rotate`, a finger turns it around the surface normal; back to `Move`; `Clone`, another copy, pinched
smaller. A finger in empty space turns the view to end on. See .agents/videos.md.

    AI_SESSION=<name> tool_transform.py setup | python3 ../nomad/.agents/ai.py send -
    AI_SESSION=<name> tool_transform.py record [name] | python3 ../nomad/.agents/ai.py send - 900
The scene is built by terrain.py, the finger helpers are gettingstarted.py's. The API presses and lifts
both fingers together: the page's "hold one finger, add a second" gestures can't be played, so the
second finger lands on the rock with the first (Transform only takes two fingers that are both on the
object, otherwise it is a camera gesture), and the mode changes use the left toolbar.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import math
import sys

import terrain as T
from clip import min_jerk
from gettingstarted import Touch

CLONE, INSTANCE, MOVE, PIVOT = 56723, 56724, 58466, 56722   # Transform's left toolbar
SNAP = 62180                                                # top toolbar
HOME = {"pivot": [0, 0.05, 0], "rotation": [0.25, 0.25, 0.067, 0.933], "translation": [0, 0, 2.65]}
REST = [1000, 730]
ROCK = [-0.2, 0.14]                                # x, z of the first rock, on the flat part
STONE = "#a3a7ab"

CLONE_AT, MOVE_AT, ROTATE_AT = [25, 160], [25, 284], [25, 344]
# in the viewport (HOME camera): where the rock is, where it goes, then where each copy is dropped
A0, A_VIA, A1 = [517, 545], [455, 500], [420, 450]
B_VIA, B = [480, 410], [565, 420]
C_VIA, C = [635, 480], [655, 570]
D_VIA, D = [735, 545], [790, 470]
ORBIT = ([1020, 752], [905, 722])                  # below the terrain

c = Touch(REST, seed=62)
steps = c.steps


LAG = 16    # px: Transform starts once the finger has travelled that far, the rock stays that much behind


def slide(a, b, via, n=60, rest=26):
    """One finger pressed on the rock's center a, slid so that the rock lands on b."""
    d = math.dist(a, via)
    end = [b[0] + LAG * (via[0] - a[0]) / d, b[1] + LAG * (via[1] - a[1]) / d]
    c.stroke([a, via, end], n, rest=rest, land=3)


def pinch(center, r0, r1, angle=25, drift=(3, -2), n=42):
    """Two fingers on the rock, r0 px from its center each, spread (or closed) to r1. Transform only
    starts once a finger has travelled ~20 px, and scales by what the fingers do from there on: the
    gesture is wider than the scale it gives."""
    u = [math.cos(math.radians(angle)), math.sin(math.radians(angle))]
    a = [center[0] - u[0] * r0, center[1] - u[1] * r0]
    b = [center[0] + u[0] * r0, center[1] + u[1] * r0]
    d = r1 - r0
    c.drag2(a, b, [-u[0] * d + drift[0], -u[1] * d + drift[1]], [u[0] * d + drift[0], u[1] * d + drift[1]], n)


def turn(center, r, a0, a1, n=56, rest=24):
    """One finger pressed on the rock, r px from its center, swung around it from a0 to a1 (degrees)."""
    p = lambda a: [center[0] + r * math.cos(math.radians(a)), center[1] + r * math.sin(math.radians(a))]
    c.wait(c.rng.randint(8, 12))
    c.touch([p(a0)] * 3 + [p(a0 + (a1 - a0) * min_jerk(i / n)) for i in range(1, n + 1)])
    c.wait(rest)


if sys.argv[1] == "setup":
    T.new_scene(steps)
    T.terrain(steps)
    x, z = ROCK
    T.add(steps, T.ADD_ICOSAHEDRON)
    T.matrix(steps, pos=[x, 0.03, z], scale=[0.12, 0.09, 0.105], rot=[14, 25, -8])
    T.validate(steps)
    T.bake(steps)
    T.paint_all(steps, STONE, roughness=70)
    T.uniform_scale(steps)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "scroll", "id": T.TOOLBOX, "to": 5000})
    c.wait(5)
    steps.append({"do": "set", "id": T.TRANSFORM, "value": True})
    c.wait(3)
    for i, v in ((MOVE, True), (SNAP, True), (CLONE, False), (INSTANCE, False), (PIVOT, False)):
        steps.append({"do": "set", "id": i, "value": v})
    # the setup clicks left the mouse pointer (and its marker) on a button: out of the window with it
    steps.append({"do": "drag", "points": [[1100, 700], [1300, 1000]], "hover": True})
    c.wait(10)
    steps.append({"do": "stats"})
    steps.append({"do": "find", "text": "Surface"})
else:
    dry = sys.argv[1] == "dry"      # `dry`: the same steps, not recorded, with a capture after each beat
    shot = (lambda: steps.append({"do": "capture"})) if dry else (lambda: None)
    if not dry:
        c.wait(300)                 # unrecorded: lets the last toast fade
        steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_transform"})
    c.wait(36)
    slide(A0, A1, A_VIA); shot()                        # move the rock into place
    c.tap(CLONE_AT, 4, after=30)
    slide(A1, B, B_VIA); shot()                         # the drag pulls a copy out
    pinch(B, 16, 62, n=56); shot()                      # two fingers on it: scale
    c.tap(CLONE_AT, 4, after=30)
    slide(B, C, C_VIA); shot()
    c.tap(ROTATE_AT, 4, after=26)
    turn(C, 24, 200, 95); shot()                        # one finger turns it around the normal
    c.tap(MOVE_AT, 4, after=24)
    c.tap(CLONE_AT, 4, after=30)
    slide(C, D, D_VIA, n=64); shot()
    pinch(D, 52, 18, angle=-20, drift=(-2, 3), n=52); shot()
    c.wait(14)
    # a finger in empty space turns the view: the rocks sit on the slopes
    c.stroke([ORBIT[0], [(ORBIT[0][0] + ORBIT[1][0]) / 2, (ORBIT[0][1] + ORBIT[1][1]) / 2 - 6], ORBIT[1]], 84,
             rest=45, land=3); shot()
    if not dry:
        steps.append({"do": "record"})
print(c.json())
