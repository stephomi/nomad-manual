#!/usr/bin/env python3
"""docs/videos/layer_shell.mp4: a bandit mask painted on a new layer of Dracula's head, then the layer's
More popup > Extract tab: the Shell preview, Extract, and the extracted mask shown alone (Solo).
dracula.load() turns the project's post process off (as a new user sees the viewport) and sets the
exposure shared by the clips on that project. See .agents/videos.md for the workflow.

Prints the JSON steps for `ai.py send -`:
    layer_shell.py setup | python3 ../../.agents/ai.py send -
    layer_shell.py record [name] | python3 ../../.agents/ai.py send - 900
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild. Layer rows and their
popups get new ids when created, so the clip works by position. The extract settings are global: the
setup sets them on a scratch layer, then reloads the project."""
import sys

from clip import Clip
import dracula

MENUS = [108, 3326, 6399, 11516, 9959, 13905, 18138, 17912, 40184, 35769, 33760, 33331, 32972, 23086, 19331,
         27845]                       # top bar buttons: menus stay open across a project load
SCENE = 3326
ICONS = [4059, 4060, 4058]            # Scene footer: light, camera and mirror icons in the viewport
SYM, RADIUS, INTENSITY = 56799, 56725, 56745
LAYERS, ADD_LAYER, PAINT_MENU = 33760, 33777, 23086
PAINT_TOOL, CLAY, TOOLBOX = 67749, 67742, 58936
SOLO = 59913
HEAD_ROW = [209, 471]                # headhi in the Scene list
WINDOW = [1200, 900]

LAYERS_AT = [1025, 25]
ADD_AT = [918, 182]
MORE_AT = [1115, 332]                 # More of the active (new) layer
EXTRACT_TAB = [1028, 394]            # the popup opens under the More button on its Settings tab
EXTRACT_AT = [941, 418]               # the Extract button
POPUP_CLOSE = [1096, 153]
SOLO_AT = [175, 860]
PRESET_AT, RED_AT, PRESETS_CLOSE = [887, 375], [646, 390], [838, 100]
START = [1000, 760]                   # resting pointer, background right of the head
# from the nose bridge out over each eye: a stroke starting near the ears would land on the hair mesh
# (unselected) and orbit the camera instead
BAND = [([515, 300], [345, 296]), ([515, 300], [690, 296])]
BOW = 0.06

c = Clip(START, seed=7)
steps = c.steps


def prepare():
    steps.append({"do": "window", "size": WINDOW})
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": CLAY, "value": True})  # after Gizmo some menus are disabled: `set` fails
    for i in MENUS:
        steps.append({"do": "set", "id": i, "value": False})
    load()
    steps.append({"do": "click", "id": SCENE})
    for i in ICONS:
        steps.append({"do": "set", "id": i, "value": False})
    steps.append({"do": "click", "id": SCENE})
    steps.append({"do": "set", "id": SYM, "value": False})


def load():
    dracula.load(steps)               # post process off and the shared exposure, after every load
    steps.append({"do": "set", "id": SOLO, "value": False})  # a retake: the last take ends in Solo
    steps.append({"do": "click", "id": SCENE}); c.tap(HEAD_ROW); steps.append({"do": "click", "id": SCENE})
    c.wait(90)  # the selection flash fades


def glide(t, a=0.04, d=0.08):
    """Progress of a paint stroke: up to speed at once, steady, a short landing. With min_jerk the press
    stays within 7 px for 0.7 s at either end when recording runs slowly (a busy machine): the stroke
    snaps into a curve and the Stroke snap bar opens."""
    v = 1 / (1 - a / 2 - d / 2)
    if t < a:
        return v * t * t / (2 * a)
    if t < 1 - d:
        return v * (t - a / 2)
    return 1 - v * (1 - t) * (1 - t) / (2 * d)


def quick(p):
    """A short press: under recording 8 held frames last long enough to count as a long press."""
    c.go(p); c.wait(c.rng.randint(17, 23))
    c.tap(p, 2)
    c.wait(25)


if sys.argv[1] == "setup":
    prepare()
    steps.append({"do": "scroll", "id": TOOLBOX, "to": 0})
    steps.append({"do": "set", "id": PAINT_TOOL, "value": True})
    steps.append({"do": "set", "id": RADIUS, "value": 44})
    steps.append({"do": "set", "id": INTENSITY, "value": 1})
    steps.append({"do": "click", "id": PAINT_MENU})  # the tool material is global: red plastic
    c.tap(PRESET_AT); c.wait(10); c.tap(RED_AT); c.wait(5); c.tap(PRESETS_CLOSE)
    steps.append({"do": "click", "id": PAINT_MENU})
    # extract settings on a scratch layer: Shell, 0.03 outward, preview on, popup back on its Settings tab
    steps.append({"do": "click", "id": LAYERS})
    steps.append({"do": "click", "id": ADD_LAYER})
    c.tap(MORE_AT); c.wait(5)
    steps.append({"do": "click", "text": "Extract", "type": "radio_option"})
    steps.append({"do": "click", "text": "Shell", "type": "radio_option"})
    steps.append({"do": "set", "text": "Height", "type": "slider", "in": "Layer 1", "value": 0.03})
    steps.append({"do": "set", "text": "preview", "type": "checkbox", "in": "Layer 1", "value": True})
    steps.append({"do": "click", "text": "Settings", "type": "radio_option", "in": "Layer 1"})
    c.tap(POPUP_CLOSE)
    steps.append({"do": "click", "id": LAYERS})
    load()
    steps.append({"do": "action", "name": "view_reset"})
    c.wait(20)
    steps.append({"do": "camera", "dolly": 0.6, "frames": 1})
    steps.append({"do": "camera", "pan": [0.07, 0.1], "frames": 1})
    steps.append({"do": "drag", "points": [[1300, 880], START], "hover": True})
    c.wait(60)
    steps.append({"do": "stats"})
else:
    steps.append({"do": "record", "to": sys.argv[2] if len(sys.argv) > 2 else "layer_shell"})
    c.wait(40)
    c.click(LAYERS_AT); c.click(ADD_AT); c.click(LAYERS_AT)
    for a, b in BAND:
        c.go(a); c.wait(8)
        steps.append({"do": "drag", "points": c.path(a, b, 75, BOW, glide)})
        c.pos = list(b)
    c.wait(30)
    c.click(LAYERS_AT); c.click(MORE_AT)
    c.click(EXTRACT_TAB); c.wait(70)              # the Shell preview (the popup grows upward)
    c.click(EXTRACT_AT); c.wait(30)               # the popup closes, the new object is selected
    c.click(LAYERS_AT)
    c.click(SOLO_AT); c.wait(30)                  # the extracted mask alone
    c.go(START); c.wait(10)
    c.camera(240, yaw=[(0.5, -38), (1, -22)], pitch=[(0.5, 14), (1, 9)], dolly=[(0.45, 0.6), (1, 0.58)],
             pan_y=[(0.45, 0.1), (1, 0.1)])
    c.wait(40)
    steps.append({"do": "record"})
print(c.json())
