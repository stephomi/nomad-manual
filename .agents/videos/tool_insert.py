#!/usr/bin/env python3
"""docs/videos/tool_insert.mp4: Insert over a small terrain with a tree on it (a sphere joined to a
cylinder). Insert is picked in the toolbox; `Quad Sphere` in the left toolbar, a click-drag on the ground
places a boulder, the drag sets its size. A tap selects the tree; `Instance`, a drag slides a copy over
the ground, but sunk to its middle: the anchor is the object's pivot, at its center. Undo; Gizmo, the top
toolbar's `Pivot` popup, `Bottom` puts the pivot at the foot of the trunk; back in Insert, each drag
plants an instance standing on the surface. A look around. See .agents/videos.md.

    AI_SESSION=<name> tool_insert.py setup | python3 ../../.agents/ai.py send -
    AI_SESSION=<name> tool_insert.py record [name] | python3 ../../.agents/ai.py send - 900
The scene is built by terrain.py. `setup` asks the running Nomad whether Insert shows its modes as a
list (set AI_SESSION). Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""
import json
import os
import subprocess
import sys

import terrain as T
from clip import Clip, min_jerk

AI_PY = os.environ.get("AI_PY", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../.agents/ai.py"))
START_TOOL = 67775                                 # toolbox: Select, nothing drawn over the viewport
SYNC, LAYOUT, MODES = 57159, 54629, 48750          # Insert's left toolbar: Sync, list / popup toggle, the list
MODE_VIEW, MODE_CLONE = 58888, 58889               # list entries
GIZMO_PIVOT = 56722                                # Gizmo's left toolbar Pivot toggle
HOME = {"pivot": [0, 0.05, 0], "rotation": [0.25, 0.25, 0.067, 0.933], "translation": [0, 0, 2.8]}
START = [1000, 730]
TREE = [-0.2, 0.14]                                # x, z of the tree, on the flat part
BARK, LEAVES = "#7d5b3d", "#5c9a48"
ROW2_CHECK = [310, 432]                            # Scene menu: the multi-selection box of the second row

# toolbox scrolled to its end (a validated mesh selected)
INSERT_AT = [1170, 153]
# Insert's list: View, Clone, Instance, Quad Sphere...
INSTANCE_AT, SPHERE_AT = [25, 310], [25, 370]
# the shortcuts at the bottom of the left toolbar, scrolled to their end: Gizmo is the last one. It
# borrows the Gizmo over Insert, a second press hands back to Insert. The toolbox would not do here: an
# unvalidated primitive selected (the boulder) shortens its list, which leaves it scrolled elsewhere
SHORTCUTS, GIZMO_AT = 48789, [25, 730]
UNDO_AT = [25, 858]
PIVOT_MENU_AT, BOTTOM_AT, POPUP_CLOSE = [447, 123], [492, 215], [603, 128]   # Gizmo: top toolbar, Pivot popup

c = Clip(START, seed=61)
steps = c.steps


def listed():
    """Whether Insert's left toolbar shows its modes as a list (the toggle above them has no state)."""
    q = [{"do": "scroll", "id": T.TOOLBOX, "to": 5000}, {"do": "wait", "frames": 3},
         {"do": "set", "id": T.INSERT, "value": True}, {"do": "wait", "frames": 3},
         {"do": "find", "in": MODES}]
    out = subprocess.run([sys.executable, AI_PY, "send", json.dumps(q)], capture_output=True, text=True).stdout
    return f"{MODE_CLONE} button" in out


def press_drag(a, b, n, hold=3):
    """Press at a, then drag to b: eased, landing slowly. The pointer must be at a."""
    pts = [a] * hold + [[a[0] + (b[0] - a[0]) * min_jerk(i / n), a[1] + (b[1] - a[1]) * min_jerk(i / n)]
                        for i in range(1, n + 1)] + [b] * 6
    steps.append({"do": "drag", "points": [[round(x, 1), round(y, 1)] for x, y in pts]})
    c.pos = list(b)


def insert(a, b, n=55, rest=35):
    c.go(a); c.wait(14)
    press_drag(a, b, n)
    c.wait(rest)


def pick(p):
    """Toolbox buttons are sticky: a long hold only borrows the tool until release. A short press picks it."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 4)
    c.wait(20)


# in the viewport (HOME camera)
BOULDER = ([640, 648], [676, 664])                 # center, then how far the drag goes: its radius
TREE_AT = [520, 452]                               # the tree's crown
SUNK = ([700, 535], [748, 568])                    # where the first instance lands, and slides to
PLANTED = (([445, 440], [428, 324]), ([700, 500], [790, 395]), ([765, 600], [850, 500]))


if sys.argv[1] == "setup":
    toggle = not listed()
    T.new_scene(steps)
    T.terrain(steps)
    # the tree: trunk and crown placed by their matrix, painted, joined (the pivot ends at its center)
    x, z = TREE
    T.add(steps, T.ADD_CYLINDER)
    T.matrix(steps, pos=[x, 0.06, z], scale=[0.034, 0.13, 0.034])
    T.validate(steps)
    T.bake(steps)
    T.paint_all(steps, BARK)
    T.add(steps, T.ADD_SPHERE)
    T.matrix(steps, pos=[x, 0.175, z], scale=[0.14, 0.14, 0.14])
    T.validate(steps)
    T.bake(steps)
    T.paint_all(steps, LEAVES)
    T.menu(steps, T.SCENE, [{"do": "drag", "points": [ROW2_CHECK, ROW2_CHECK]}, {"do": "wait", "frames": 5},
                            {"do": "click", "id": T.JOIN}, {"do": "wait", "frames": 5}])
    T.uniform_scale(steps)
    steps.append(dict({"do": "camera"}, **HOME))
    steps.append({"do": "scroll", "id": T.TOOLBOX, "to": 5000})
    c.wait(5)
    steps.append({"do": "set", "id": T.GIZMO, "value": True})
    c.wait(3)
    steps.append({"do": "set", "id": GIZMO_PIVOT, "value": False})   # the toggle outlives a new scene
    steps.append({"do": "set", "id": T.INSERT, "value": True})
    c.wait(3)
    if toggle:
        steps.append({"do": "click", "id": LAYOUT})
        c.wait(3)
    steps.append({"do": "scroll", "id": MODES, "to": 0})
    steps.append({"do": "scroll", "id": SHORTCUTS, "to": 500})
    c.wait(3)
    steps.append({"do": "set", "id": MODE_VIEW, "value": True})
    steps.append({"do": "set", "id": SYNC, "value": False})
    steps.append({"do": "set", "id": START_TOOL, "value": True})     # the clip picks Insert itself
    steps.append({"do": "drag", "points": [[780, 450], START], "hover": True})
    c.wait(10)
    steps.append({"do": "stats"})
else:
    dry = sys.argv[1] == "dry"      # `dry`: the same steps, not recorded, with a capture after each beat
    shot = (lambda: steps.append({"do": "capture"})) if dry else (lambda: None)
    if not dry:
        steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "tool_insert"})
    c.wait(30)
    pick(INSERT_AT)
    c.click(SPHERE_AT, hold=3); c.wait(10)             # a primitive: the drag sets its size
    insert(BOULDER[0], BOULDER[1]); shot()
    c.click(TREE_AT, hold=2); c.wait(15); shot()        # a tap selects another object: the tree
    c.click(INSTANCE_AT, hold=3); c.wait(10)
    insert(SUNK[0], SUNK[1], rest=50); shot()           # its pivot, at its center, lands on the surface
    c.click(UNDO_AT, hold=2); c.wait(20); shot()
    c.click(GIZMO_AT, hold=1); c.wait(15); shot()       # the Gizmo shortcut: the pivot is where the gizmo is
    c.click(PIVOT_MENU_AT, hold=2); c.wait(15)
    c.click(BOTTOM_AT, hold=2); c.wait(30); shot()      # the pivot goes to the foot of the trunk
    c.click(POPUP_CLOSE, hold=2)
    c.click(GIZMO_AT, hold=1); c.wait(10); shot()       # back to Insert, still on Instance
    for a, b in PLANTED:
        insert(a, b, rest=22)
    shot()
    c.go(START); c.wait(10)
    # every press on a surface moved the orbit pivot there: the same view around the terrain's center again
    steps.append(dict({"do": "camera"}, **HOME))
    c.camera(220, yaw=[(0.5, -34), (1, -26)], pitch=[(0.5, -9), (1, -6)], dolly=[(0.5, 0.95), (1, 0.97)],
             pan_y=[(0.5, -0.02), (1, -0.02)])
    c.wait(40); shot()
    if not dry:
        steps.append({"do": "record"})
print(c.json())
