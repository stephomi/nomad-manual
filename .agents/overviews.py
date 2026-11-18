#!/usr/bin/env python3
"""Retake the page overview screenshots (full window, highlighted menu) in one go.

overviews.py [name ...]   with a Nomad AI session running (../../.agents/ai.py start)

Without names it retakes them all. Each overview gets a scene that fits its page (a fresh stroke
for Stroke, a painted bust for Paint, a lit room for Shading...): the project is loaded, Max frame
sampling is set to 200, the tool is picked, the setup steps run, then the menu is opened, captured
with shot.py --full --highlight, and closed again.

Start a fresh session first: Nomad numbers a project saved twice in one session ("viking 1"), and
file_menu saves its project to show the thumbnail.

The background overview needs the reference image in the ai= sandbox, under the name its project
stores: it is copied from scenes/IMG_3307.webp.
"""
import glob, json, os, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shot as shot_cli  # noqa: E402

MANUAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMAD = os.path.dirname(os.path.dirname(MANUAL))
PROJECTS = os.path.expanduser("~/Downloads/data_nomad/cache/projects/manual/")
SESSION = os.path.expanduser("~/Downloads/data_nomad/cache/tmp_session/argB/")  # the ai= session's user folder
SANDBOX = SESSION + "projects/"  # where an ai= session saves
PARK = [1600, 1000]  # pointer off the window
# boring head, front view, moved left of the right-hand panels
BORING_FRONT = [{"do": "action", "name": "view_toggle_front"}, {"do": "wait", "frames": 40},
                {"do": "camera", "dolly": 1.35, "pan": [0.25, 0.05], "frames": 1}, {"do": "wait", "frames": 10}]
# elephant, default view: select it, then a few strokes so the History panel has entries
ELEPHANT_STROKES = [{"do": "drag", "points": [[630, 340], [655, 355], [680, 365]]},
                    {"do": "drag", "points": [[640, 395], [690, 400]]},
                    {"do": "action", "name": "tool_inflate"}, {"do": "drag", "points": [[660, 380], [680, 410]]},
                    {"do": "action", "name": "tool_smooth"}, {"do": "drag", "points": [[650, 360], [670, 380]]},
                    {"do": "wait", "frames": 120}]


def shot(scene, action, title, extra=(), setup=(), teardown=(), tool="Clay", hover=None):
    return dict(scene=scene, action=action, title=title, extra=list(extra), setup=list(setup),
                teardown=list(teardown), tool=tool, hover=hover)


def tab(name):
    return {"do": "click", "text": name, "type": "radio_option"}


def act(*names):
    return [{"do": "action", "name": n} for n in names]


SHOTS = {
    "scene_menu_summary": shot("dragon", "menu_scene", "Scene"),
    "topology_overview": shot("woman", "menu_topology", "Multires", [tab("Multires")],
                              setup=act("toggle_wireframe"), teardown=act("toggle_wireframe")),
    "file_menu": shot("viking", "menu_files", "Files", [tab("Files")]),
    "material_overview": shot("viking", "menu_material", "Material",
                              # tap the ring, then let the selection flash fade
                              setup=[{"do": "drag", "points": [[533, 568], [533, 568]]}, {"do": "wait", "frames": 150}]),
    "shading_overview": shot("elephant", "menu_shading", "Shading"),
    "background_overview": shot("dragon_reference", "menu_background", "Background"),
    "camera_overview2": shot("woman", "menu_camera", "Camera",
                             setup=act("add_camera") + [{"do": "wait", "frames": 5},
                                                         {"do": "camera", "orbit": [55, 10], "dolly": 2.2, "frames": 1}]),
    "paint_overview": shot("woman color", "menu_paint", "Paint", tool="Paint", hover=[560, 380]),
    "symmetry_overview": shot("boringhead", "menu_symmetry", "Symmetry",
                              setup=BORING_FRONT + act("shading_matcap", *["intensity_increase"] * 3) +
                              [{"do": "drag", "points": [[575, 300], [600, 270], [625, 250], [650, 245]]}] * 2 +
                              [{"do": "wait", "frames": 150}],
                              teardown=act("shading_pbr", *["intensity_decrease"] * 3)),
    "settings_overview": shot("elephant", "menu_settings", "Settings",
                              setup=act("toggle_wireframe", "toggle_grid"), teardown=act("toggle_wireframe", "toggle_grid")),
    "stroke_overview": shot("boringhead", "menu_stroke", "Stroke", [tab("Stroke")],
                            # MatCap, smaller radius and more intensity so the stroke reads at a glance;
                            # radius and intensity are global, the teardown puts them back
                            setup=BORING_FRONT + act("toggle_symmetry", "shading_matcap", *["radius_decrease"] * 3,
                                                     *["intensity_increase"] * 3) +
                            [{"do": "drag", "points": [[580, 190], [620, 250], [660, 190], [700, 250], [740, 190]]}] * 2 +
                            [{"do": "camera", "orbit": [-15, 0], "frames": 1}, {"do": "wait", "frames": 150}],
                            teardown=act("toggle_symmetry", "shading_pbr", *["radius_increase"] * 3,
                                         *["intensity_decrease"] * 3),
                            hover=[790, 430]),
    "tools_menu": shot("dracula", "button:toolbox", None),
    "postprocess_overview_drac": shot("dracula", "menu_postprocess", "PostProcess"),
    "history_overview": shot("elephant", None, "History", [tab("History")], setup=ELEPHANT_STROKES),
    "interface_overview2": shot("woman color", "menu_interface", "Interface", [tab("Interface"), tab("Appearance")]),
    "layers_overview": shot("boringhead", "menu_layers", "Layers"),
    "transform_overview": shot("dracula", "menu_transform", "Transform",
                               # tap the face (the hair is selected on load), step back so the gizmo shows
                               setup=[{"do": "drag", "points": [[648, 432], [648, 432]]},
                                      {"do": "camera", "dolly": 1.5, "pan": [0.15, 0], "frames": 1}] +
                               act("tool_gizmo") + [{"do": "wait", "frames": 150}]),
    "operation_overview": shot("dragon", "menu_operation", "Operation"),
}


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def send(steps, timeout=120):
    folder = open(os.path.join(NOMAD, "tmp/ai/current")).read().strip()
    return shot_cli.send(folder, steps, timeout)


def widget(results, pred):
    for w in results["widgets"]:
        if pred(w):
            return w
    return None


def titled_panels():
    return [w for w in send([{"do": "find", "type": "panel"}])[0]["widgets"] if w["text"]]


def close_menus():
    # a menu action can switch tabs instead of closing (Topology), and escape closes nothing:
    # clicking the active top bar button is what closes a menu
    for _ in range(3):
        if not titled_panels():
            return
        buttons = send([{"do": "find", "type": "button"}])[0]["widgets"]
        active = [w for w in buttons if w["rect"][1] == 0 and w["rect"][3] == 50 and w.get("value") is True]
        send([{"do": "click", "id": w["id"]} for w in active] + [{"do": "wait", "frames": 3}])
    if titled_panels():
        fail("panels still open: %s" % [p["text"] for p in titled_panels()])


def pick_tool(label):
    # the tool actions toggle back to the previous tool when the tool is already active: click its button
    btn = widget(send([{"do": "find", "text": label, "type": "button"}])[0], lambda w: w.get("panel"))
    if btn and not btn["value"]:
        send([{"do": "click", "id": btn["id"]}])


def sampling():
    send([{"do": "action", "name": "menu_postprocess"}, {"do": "wait", "frames": 3},
          {"do": "set", "text": "Max frame sampling", "type": "slider", "value": 200},
          {"do": "action", "name": "menu_postprocess"}, {"do": "wait", "frames": 3}])


def scene_row(y):
    # a row of the scene tree, by its top in the panel
    rows = send([{"do": "find", "type": "button", "in": "Scene"}])[0]["widgets"]
    return widget({"widgets": rows}, lambda w: w["rect"][2] == 350 and abs(w["rect"][1] - y) < 2)


def load(scene):
    if scene == "dragon_reference":
        # the user's scene: background settings and a reference image, no mesh. The image itself is not
        # in the .nom, only its name, so it goes in the session's backgrounds folder first.
        ref = SESSION + "backgrounds/IMG_3307.png"
        if not os.path.exists(ref):
            subprocess.run(["magick", os.path.join(MANUAL, ".agents/scenes/IMG_3307.webp"), ref], check=True)
            fail("reference image copied: restart the Nomad session so it loads it")
        send([{"do": "import", "path": PROJECTS + scene + ".nom", "replace": True},
              {"do": "import", "path": PROJECTS + "dragon.nom", "replace": False}, {"do": "wait", "frames": 30}])
        sampling()
        send(act("tool_clay"))  # the user's scene leaves the Gizmo tool on (Clay's button only shows for a mesh)
        send([{"do": "action", "name": "menu_scene"}, {"do": "wait", "frames": 5}])
        row = scene_row(292)  # the dragon group, first row
        send([{"do": "click", "id": row["id"]}, {"do": "action", "name": "menu_scene"}, {"do": "wait", "frames": 120}])
        return
    send([{"do": "import", "path": PROJECTS + scene + ".nom", "replace": True}, {"do": "wait", "frames": 30}])
    sampling()
    if scene == "elephant":  # opens with nothing selected: tap it, let the selection flash fade
        send([{"do": "drag", "points": [[625, 450], [625, 450]]}, {"do": "wait", "frames": 120}])
    if scene == "dragon":
        # select the head mesh: expand the group in the scene tree and tap its row
        send([{"do": "action", "name": "menu_scene"}, {"do": "wait", "frames": 5}])
        expand = widget(send([{"do": "find", "type": "button", "text": "sort_right", "in": "Scene"}])[0],
                        lambda w: w["rect"][1] > 300)
        if expand:
            send([{"do": "click", "id": expand["id"]}, {"do": "wait", "frames": 5}])
        send([{"do": "drag", "points": [[145, 660], [145, 660]]}, {"do": "wait", "frames": 3},
              {"do": "action", "name": "menu_scene"}, {"do": "wait", "frames": 3}])


def open_panel(s):
    """opens the shot's menu, returns its panel"""
    if s["action"] and s["action"].startswith("button:"):  # a top bar button without a binding (the toolbox)
        icon = s["action"][7:] + ".png"
        btn = widget(send([{"do": "find", "type": "button"}])[0], lambda w: w.get("icon") == icon and w["rect"][1] == 0)
        send([{"do": "click", "id": btn["id"]}, {"do": "wait", "frames": 5}])
        s["close"] = btn["id"]
    elif s["action"]:
        send([{"do": "action", "name": s["action"]}, {"do": "wait", "frames": 5}])
    else:  # History is a bottom-bar button
        hist = widget(send([{"do": "find", "text": "History", "type": "button"}])[0], lambda w: w.get("panel"))
        send([{"do": "click", "id": hist["id"]}, {"do": "wait", "frames": 5}])
        s["close"] = hist["id"]
    if s["extra"]:
        send(s["extra"] + [{"do": "wait", "frames": 5}])
    panels = send([{"do": "find", "type": "panel"}])[0]
    if s["title"]:
        return widget(panels, lambda w: w["text"] == s["title"])
    # the toolbox has no title: it is the right sidebar's panel, widened
    return widget(panels, lambda w: w["rect"][0] > 700 and w["rect"][2] > 200)


def main():
    names = sys.argv[1:] or list(SHOTS)
    for n in names:
        if n not in SHOTS:
            fail("unknown overview %s" % n)
    for name in names:
        s = SHOTS[name]
        load(s["scene"])
        pick_tool(s["tool"])
        if s["setup"]:
            send(s["setup"] + [{"do": "wait", "frames": 10}])
        panel = open_panel(s)
        if not panel:
            fail("%s: menu panel not found" % name)
        if name == "file_menu":
            # save, so the Project card shows a thumbnail instead of "Unsaved changes!": an ai= session
            # saves into its sandbox, never the user's projects. Earlier saves left there would make
            # Nomad propose "viking 1", so those sandbox copies go first.
            for old in glob.glob(os.path.join(SANDBOX, s["scene"] + "*.nom")):
                os.remove(old)
            send([{"do": "click", "text": "Save", "type": "button", "in": panel["id"]}, {"do": "wait", "frames": 5}])
            dialog = widget(send([{"do": "find", "type": "panel"}])[0], lambda w: w["text"].startswith("Save"))
            if dialog:
                send([{"do": "click", "text": "Ok", "in": dialog["id"]}, {"do": "wait", "frames": 60}])
        pos = s["hover"] or PARK
        send([{"do": "scroll", "id": panel["id"], "to": 0},
              {"do": "drag", "points": [pos, [pos[0] + 1, pos[1]]], "hover": True}, {"do": "wait", "frames": 5}])
        cmd = [sys.executable, os.path.join(MANUAL, ".agents/shot.py"), name, "--full",
               "--highlight", s["title"] or ",".join("%g" % v for v in panel["rect"])]
        subprocess.run(cmd, check=True)
        if "close" in s:
            send([{"do": "click", "id": s["close"]}, {"do": "wait", "frames": 3}])
        close_menus()
        if s["teardown"]:
            send(s["teardown"] + [{"do": "wait", "frames": 3}])


if __name__ == "__main__":
    main()
