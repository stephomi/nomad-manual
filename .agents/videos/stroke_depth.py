"""Shared by stroke_depth_bump.py and stroke_depth_cavity.py: a plane of stone tiles
(.agents/scenes/stone_tiles.py), painted across with and without the Paint tool's Depth filter.
See .agents/videos.md for the workflow. Widget ids are the 2026-11-20 build's.

The setup expects the Paint tool's stroke types shown as a list in the left bar (as
paint_color_texture.py leaves them)."""
import os
import subprocess
import tempfile

from clip import Clip

HERE = os.path.dirname(os.path.abspath(__file__))
SCENE_SCRIPT = os.path.join(HERE, "..", "scenes", "stone_tiles.py")
OBJ = os.path.join(tempfile.gettempdir(), "nomad_manual_stone_tiles.obj")

MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]
SCENE, POST, POST_PANEL, RENDER_RES = 3326, 13905, 13892, 13908
ICONS = [4059, 4060, 4058]
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
PAINT_MENU, PAINT_TOOL, TOOLBOX = 23086, 67749, 58936
LAYOUT = 54629
FILTER_PANEL, AREA_NORMAL, FALLOFF_NORMAL, AREA_RADIUS = 21752, 22019, 22075, 21889
AREA_POSITION = 21849
DEPTH, DEPTH_FALLOFF, OFFSET, TOP, BOTTOM = 21942, 21958, 21999, 21979, 21959
WINDOW = [1200, 900]

PRESET_AT, PRESETS_CLOSE = [887, 375], [838, 100]
SLOT_AT, EMPTY_AT, SLOT_CLOSE = [1015, 496], [729, 459], [996, 354]
STROKE_MENU_AT = [825, 25]
UNDO_AT = [25, 858]
START = [1000, 780]
DEPTH_AT = [1100, 785]                # Depth filter's checkbox, the Filter panel scrolled to its end
SCROLL_FROM, SCROLL_TO = [800, 700], [800, 300]
STROKES = [([240, 425], [960, 420]), ([950, 495], [230, 500])]  # across two rows of tiles and grooves


def setup(c, color_at, offset, top, bottom, falloff, area):
    steps = c.steps
    subprocess.run(["python3", SCENE_SCRIPT, OBJ], check=True)
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "import", "path": OBJ, "replace": True})
    c.wait(10)
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": POST})  # an imported OBJ comes with the post process off
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "click", "id": POST})
    steps.append({"do": "click", "id": SCENE})
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": SYM, "value": False})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": PAINT_TOOL, "value": True})
    steps.append({"do": "click", "id": LAYOUT})          # list -> compact: the radius slider
    steps.append({"do": "set", "id": RADIUS, "value": 110})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "click", "id": LAYOUT})
    steps.append({"do": "click", "id": PAINT_MENU})      # the color, no texture
    c.tap(PRESET_AT); c.wait(10); c.tap(color_at); c.wait(5); c.tap(PRESETS_CLOSE)
    c.tap(SLOT_AT); c.wait(10); c.tap(EMPTY_AT); c.wait(5); c.tap(SLOT_CLOSE)
    steps.append({"do": "set", "id": PAINT_MENU, "value": False})
    steps.append({"do": "action", "name": "menu_filter"})
    steps.append({"do": "scroll", "id": FILTER_PANEL, "to": 300})
    steps.append({"do": "set", "id": AREA_NORMAL, "value": False})
    steps.append({"do": "set", "id": FALLOFF_NORMAL, "value": False})
    steps.append({"do": "set", "id": AREA_RADIUS, "value": area})  # the plane the depth is measured from
    steps.append({"do": "set", "id": AREA_POSITION, "value": area})
    steps.append({"do": "scroll", "id": FILTER_PANEL, "to": 2000})
    steps.append({"do": "set", "id": DEPTH, "value": True})     # its sliders show once it's on
    steps.append({"do": "set", "id": DEPTH_FALLOFF, "value": True})  # Top/Bottom area only with it
    steps.append({"do": "set", "id": OFFSET, "value": offset})
    steps.append({"do": "set", "id": TOP, "value": top})
    steps.append({"do": "set", "id": BOTTOM, "value": bottom})
    steps.append({"do": "set", "id": DEPTH_FALLOFF, "value": falloff})
    steps.append({"do": "set", "id": DEPTH, "value": False})
    steps.append({"do": "scroll", "id": FILTER_PANEL, "to": 2000})
    steps.append({"do": "action", "name": "menu_filter"})
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(10)
    steps.append({"do": "camera", "orbit": [0, 40], "frames": 1})  # from above, at an angle
    steps.append({"do": "camera", "dolly": 0.8, "frames": 1})
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(200)  # the "Reset view" toast fades on wall-clock time
    steps.append({"do": "stats"})


def record(c, name, strokes):
    steps = c.steps

    def paint():
        for a, b in strokes:
            c.go(a); c.wait(10)
            c.stroke(a, b, 80, bow=0.04)
        c.wait(50)

    steps.append({"do": "record", "to": name})
    c.wait(40)
    paint()                                 # everything gets painted
    for _ in strokes:
        c.click(UNDO_AT)
    c.wait(15)
    c.click(STROKE_MENU_AT)                 # Filter tab, scrolled to the Depth filter
    c.click(DEPTH_AT); c.wait(15)           # Depth filter on: its graph and settings show below...
    c.go(SCROLL_FROM); c.wait(10)
    c.stroke(SCROLL_FROM, SCROLL_TO, 45, bow=0.0)  # ...scrolled into view by a drag on the panel's margin
    c.wait(90)
    c.click(STROKE_MENU_AT)
    paint()                                 # only part of the relief
    c.go(START); c.wait(10)
    c.camera(180, yaw=[(0.5, -10), (1, -7)], pitch=[(0.5, -5), (1, -3)])
    c.wait(30)
    steps.append({"do": "record"})
