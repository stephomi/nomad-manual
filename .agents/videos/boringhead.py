"""The look shared by every clip recorded on boringhead.nom: `look()` returns the setup steps to run once the
project has loaded. See .agents/videos.md.

    from boringhead import PROJECT, look
    steps.append({"do": "import", "path": PROJECT, "replace": True})
    steps.extend(look())

The project is saved with post process on (chromatic aberration, SSAO, tone mapping with an exposure of
2.5) over a nearly black environment (exposure 0.02345): with post process off, as a new user has it, the
head is dark and murky on its black background. So the environment exposure is raised instead, in the
Shading menu, until the skin's mid-tones show without blown highlights. The two lights, the materials,
the paint and the background stay as saved. One value for all the clips, so they match each other.
Widget ids are the 2026-11-20 build's: check them with `find` after a rebuild."""

import os

PROJECT = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/boringhead.nom")
POST, POST_PANEL, RENDER_RES = 13905, 13892, 13908
POST_ON = 13907                       # the Post Process checkbox, above the effects: all of them at once
SHADING, SHADING_PANEL, ENV_EXPOSURE = 9959, 9946, 10033
EXPOSURE = 0.1                        # Shading > Environment > Exposure (0.3 washes the skin out, 1 burns it)


def look():
    """Render resolution x1 (x1.25 renders banded shadows in a 1200 window), the whole post process off,
    the environment exposure up. Both menus end closed, scrolled back to the top."""
    wait = {"do": "wait", "frames": 5}
    return [
        {"do": "set", "id": POST, "value": True}, wait,
        {"do": "scroll", "id": POST_PANEL, "to": 0}, wait,
        {"do": "set", "id": RENDER_RES, "value": 1},
        {"do": "set", "id": POST_ON, "value": False}, wait,   # `set`, not the toggle_postprocess action
        {"do": "set", "id": POST, "value": False},
        {"do": "set", "id": SHADING, "value": True}, wait,
        {"do": "scroll", "id": SHADING_PANEL, "to": 300}, wait,  # the slider well inside the panel
        {"do": "set", "id": ENV_EXPOSURE, "value": EXPOSURE},
        {"do": "scroll", "id": SHADING_PANEL, "to": 0}, wait,
        {"do": "set", "id": SHADING, "value": False},
    ]
