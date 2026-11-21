"""Shared by the clips recorded on the Dracula project (multiresolution, merge_separate, layer_shell):
load() opens it the way a new user sees a viewport, post process off. See .agents/videos.md.

The project is saved with post process on (strong chromatic aberration) and lit for its tone mapping
(exposure 3.25): with post process alone turned off, the model is dark on a dark background. So load()
also raises the exposure in the Shading menu, the same for every clip on this project: more light
than environment, which alone turns the shading flat and hazy. Materials, paint and the background are
untouched. Widget ids are the 2026-11-20 build's (check them with `find` after a rebuild); the light's
settings popup gets new ids at each load, so it is addressed through its `Softness` slider."""

PROJECT = "/Users/steph/Downloads/data_nomad/cache/projects/manual/dracula.nom"
POST, POST_PANEL = 13905, 13892
POST_ON = 13907                  # the `Post Process` checkbox, above the effects
RENDER_RES = 13908
SHADING, SHADING_PANEL, ENV_EXPOSURE = 9959, 9946, 10033
# Chosen on two scenes: Dracula's head (mid-tones clearly visible; an environment above 0.5 turns it
# hazy) and the white sphere of merge_separate (a light of 12 blows out its lit side)
EXPOSURE = 0.4                   # Shading > Environment > Exposure (saved: 0.2421)
LIGHT = 10                       # Shading > Lights > Light > ... > Intensity (saved: 3.425)


def wait(steps, n):
    steps.append({"do": "wait", "frames": n})


def post_off(steps):
    """The whole post process off, render resolution x1 (x1.25 renders banded shadows in a 1200 window)."""
    steps.append({"do": "set", "id": POST, "value": True})
    wait(steps, 5)
    steps.append({"do": "scroll", "id": POST_PANEL, "to": 0})
    steps.append({"do": "set", "id": RENDER_RES, "value": 1})
    steps.append({"do": "set", "id": POST_ON, "value": False})
    steps.append({"do": "set", "id": POST, "value": False})
    wait(steps, 20)              # a top bar button reads as on a moment after its menu closes


def expose(steps):
    """Light and environment up, to make up for the tone mapping the project was lit for."""
    steps.append({"do": "set", "id": SHADING, "value": True})
    wait(steps, 5)
    steps.append({"do": "scroll", "id": SHADING_PANEL, "to": 0})
    steps.append({"do": "click", "text": "more.png", "in": SHADING_PANEL})  # the light's settings
    wait(steps, 10)
    steps.append({"do": "set", "text": "Intensity", "in": "Softness", "value": LIGHT})
    steps.append({"do": "set", "id": ENV_EXPOSURE, "value": EXPOSURE})
    steps.append({"do": "set", "id": SHADING, "value": False})             # closes the popup too
    wait(steps, 20)


def load(steps):
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    wait(steps, 10)
    post_off(steps)
    expose(steps)
