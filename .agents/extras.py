#!/usr/bin/env python3
"""Retake the images that need more than a menu overview: panel crops on a chosen model, and the
annotated screenshots (labels and arrows drawn with ImageMagick in the Nomad accent).

extras.py [name ...]   with a Nomad AI session running (../../.agents/ai.py start)

Never the default sphere: each image loads one of the manual projects (see overviews.py).
"""
import math, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import overviews as ov  # noqa: E402
import webp  # noqa: E402

SHOT = os.path.join(ov.MANUAL, ".agents/shot.py")
IMAGES = os.path.join(ov.MANUAL, "docs/images")
TMP = tempfile.mkdtemp(prefix="extras-")
ACCENT = "#ebbe6c"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def shot(name, *args, out=None):
    cmd = [sys.executable, SHOT, name, *args] + (["--out", out] if out else [])
    subprocess.run(cmd, check=True)


def capture():
    ov.send([{"do": "drag", "points": [ov.PARK, [ov.PARK[0] + 1, ov.PARK[1]]], "hover": True}, {"do": "wait", "frames": 5}])
    return ov.send([{"do": "capture"}])[-1]["path"]


def save(png, name):
    print(webp.encode(png, os.path.join(IMAGES, name + ".webp")))


def arrow(x0, y0, x1, y1, head=40):
    """magick -draw arguments for a line from (x0,y0) to (x1,y1) with a head at (x1,y1)"""
    a = math.atan2(y1 - y0, x1 - x0)
    pts = [(x1 - head * math.cos(a + s), y1 - head * math.sin(a + s)) for s in (0.45, -0.45)]
    return ["-draw", "line %d,%d %d,%d" % (x0, y0, x1, y1)] + \
           sum([["-draw", "line %d,%d %d,%d" % (x1, y1, px, py)] for px, py in pts], [])


def label(x, y, text, size=64):
    return ["-stroke", "none", "-fill", ACCENT, "-font", FONT, "-pointsize", str(size), "-annotate", "+%d+%d" % (x, y), text]


def prepare(scene, tool="Clay"):
    ov.load(scene)
    ov.pick_tool(tool)


def layers():
    prepare("boringhead")
    ov.send([{"do": "action", "name": "menu_layers"}, {"do": "wait", "frames": 5}])
    shot("layers_menu", "--panel", "Layers")
    expand = ov.widget(ov.send([{"do": "find", "type": "button", "in": "Layers"}])[0], lambda w: w.get("icon") == "sort_right.png")
    ov.send([{"do": "click", "id": expand["id"]}, {"do": "wait", "frames": 5}])
    shot("layers_expand", "--panel", "Layers")
    ov.send([{"do": "click", "id": expand["id"]}, {"do": "wait", "frames": 5}])
    # the More popup of the active layer, both tabs side by side
    more = ov.widget(ov.send([{"do": "find", "type": "button", "in": "Layers"}])[0], lambda w: w.get("icon") == "more.png")
    ov.send([{"do": "click", "id": more["id"]}, {"do": "wait", "frames": 5}])
    a, b = os.path.join(TMP, "more_a.png"), os.path.join(TMP, "more_b.png")
    shot("layers_more", "--panel", "smile", out=a)
    ov.send([{"do": "click", "text": "Extract", "type": "radio_option"}, {"do": "wait", "frames": 5}])
    shot("layers_more", "--panel", "smile", out=b)
    png = os.path.join(TMP, "more.png")
    subprocess.run(["magick", a, b, "-background", "#262322", "-gravity", "north", "+append", png], check=True)
    save(png, "layers_more")
    ov.send([{"do": "key", "key": "escape"}, {"do": "wait", "frames": 3}])
    ov.close_menus()


def history():
    prepare("elephant")
    ov.send(ov.ELEPHANT_STROKES)
    hist = ov.widget(ov.send([{"do": "find", "text": "History", "type": "button"}])[0], lambda w: w.get("panel"))
    ov.send([{"do": "click", "id": hist["id"]}, {"do": "wait", "frames": 5},
             {"do": "click", "text": "History", "type": "radio_option"}, {"do": "wait", "frames": 5}])
    shot("history_history", "--panel", "History")
    ov.send([{"do": "click", "id": hist["id"]}, {"do": "wait", "frames": 3}])


def symmetry_button():
    prepare("woman")
    sym = ov.widget(ov.send([{"do": "find", "text": "Sym", "type": "button"}])[0], lambda w: w.get("panel"))
    if not sym["value"]:
        ov.send([{"do": "click", "id": sym["id"]}, {"do": "wait", "frames": 5}])
    png = os.path.join(TMP, "sym.png")
    subprocess.run(["magick", capture(), "-crop", "700x560+0+0", "+repage", "-fill", "none", "-stroke", ACCENT,
                    "-strokewidth", "6", "-draw", "ellipse 50,202 62,62 0,360"] + arrow(200, 330, 120, 250) +
                   label(190, 400, "Symmetry button", 58) + [png], check=True)
    save(png, "symmetry_button")


def interface_overview1():
    prepare("viking")
    regions = [("rgba(235,190,108,0.30)", (0, 0, 900, 100)), ("rgba(235,190,108,0.30)", (1876, 0, 2880, 100)),
               ("rgba(120,150,255,0.30)", (116, 116, 460, 236)), ("rgba(255,150,80,0.30)", (2430, 120, 2720, 280)),
               ("rgba(80,220,230,0.30)", (0, 120, 100, 1670)), ("rgba(120,230,120,0.30)", (2760, 120, 2880, 1670)),
               ("rgba(240,100,220,0.30)", (0, 1690, 1100, 1790))]
    labels = [("#ebbe6c", 1220, 80, "Top menus"), ("#8fa6ff", 500, 200, "Stats"), ("#ff9650", 2030, 220, "Navigator"),
              ("#50dce6", 150, 880, "Left toolbar"), ("#78e678", 2370, 880, "Toolbox"), ("#f064dc", 1140, 1765, "Bottom toolbar")]
    cmd = ["magick", capture()]
    for color, (x0, y0, x1, y1) in regions:
        cmd += ["-fill", color, "-draw", "roundrectangle %d,%d %d,%d 16,16" % (x0, y0, x1, y1)]
    cmd += ["-font", FONT, "-pointsize", "64", "-stroke", "rgba(0,0,0,0.6)", "-strokewidth", "3"]
    for color, x, y, text in labels:
        cmd += ["-fill", color, "-annotate", "+%d+%d" % (x, y), text]
    png = os.path.join(TMP, "if1.png")
    subprocess.run(cmd + [png], check=True)
    save(png, "interface_overview1")


def tool_left_panel():
    prepare("dracula")
    cmd = ["magick", capture(), "-crop", "2400x1800+0+0", "+repage", "-fill", "none", "-stroke", ACCENT, "-strokewidth", "8"]
    rows = [(414, "Radius"), (734, "Intensity"), (974, "Sub"), (1300, "Shortcuts")]
    for y, _ in rows:
        cmd += arrow(240, y, 110, y, 30)
    for y, text in rows:
        cmd += label(270, y + 22, text)
    png = os.path.join(TMP, "left.png")
    subprocess.run(cmd + [png], check=True)
    save(png, "tool_left_panel")


def tools_settings_menu():
    prepare("viking", tool="Smooth")
    ov.send([{"do": "action", "name": "menu_tool"}, {"do": "wait", "frames": 5}, {"do": "scroll", "text": "Tool", "to": 0},
             {"do": "drag", "points": [ov.PARK, [ov.PARK[0] + 1, ov.PARK[1]]], "hover": True}])
    raw = os.path.join(TMP, "tool_raw.png")
    shot("tools_settings_menu", "--full", "--highlight", "Tool", out=raw)
    png = os.path.join(TMP, "tool.png")
    subprocess.run(["magick", raw, "-fill", "none", "-stroke", ACCENT, "-strokewidth", "8"] + arrow(1480, 125, 1975, 78, 36) +
                   label(1110, 150, "Tool menu", 70) + [png], check=True)
    save(png, "tools_settings_menu")
    ov.close_menus()


JOBS = {"layers": layers, "history_history": history, "symmetry_button": symmetry_button,
        "interface_overview1": interface_overview1, "tool_left_panel": tool_left_panel,
        "tools_settings_menu": tools_settings_menu}

if __name__ == "__main__":
    for n in sys.argv[1:] or list(JOBS):
        if n not in JOBS:
            ov.fail("unknown job %s (%s)" % (n, ", ".join(JOBS)))
        JOBS[n]()
