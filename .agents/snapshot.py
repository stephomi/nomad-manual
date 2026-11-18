#!/usr/bin/env python3
"""Snapshot a menu for the page audit: every tab's options with their help texts, and a stitched capture.

snapshot.py <out dir> <menu action> [tab ...]   with a Nomad AI session running

Opens the menu, then for each tab (or the menu as it opens, without tabs) writes <tab>.txt (one line
per widget in layout order: type, label, value, help text from english.strings) and <tab>.webp.
Closes the menu by its active top bar button at the end.
"""
import json, os, re, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shot as shot_cli  # noqa: E402

MANUAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMAD = os.path.dirname(os.path.dirname(MANUAL))
PARK = {"do": "drag", "points": [[1300, 880], [1600, 1100]], "hover": True}

STRINGS = {}
_txt = open(os.path.join(NOMAD, "lib/nomad-translation/locales/english.strings"), encoding="utf8").read()
for _m in re.finditer(r'^([\w.]+)\s*=\s*"(.*?)";', _txt, re.M | re.S):
    STRINGS[_m.group(1)] = " ".join(_m.group(2).split())
HELP = {}  # label -> help texts of the keys showing that label
for _k, _v in STRINGS.items():
    if _k + ".help" in STRINGS:
        HELP.setdefault(_v, []).append(STRINGS[_k + ".help"])


def send(steps, timeout=120):
    folder = open(os.path.join(NOMAD, "tmp/ai/current")).read().strip()
    return shot_cli.send(folder, steps, timeout)


def menu_panel():
    panels = [w for w in send([{"do": "find", "type": "panel"}])[0]["widgets"] if w["text"] and "panel" not in w]
    return panels[0] if panels else None


def dump(panel, path):
    smax, h = panel["scroll"][1], panel["rect"][3]
    items, s = {}, 0.0
    while True:
        res = send([{"do": "scroll", "id": panel["id"], "to": s}, {"do": "wait", "frames": 3}, {"do": "find", "in": panel["id"]}])
        for w in res[-1]["widgets"]:
            if w["type"] == "panel":
                continue
            items.setdefault((w.get("key") or w["text"], w["type"], round(w["rect"][0])), (w["rect"][1] + s, w))
        if s >= smax:
            break
        s = min(s + h * 0.6, smax)
    send([{"do": "scroll", "id": panel["id"], "to": 0}])
    lines = []
    for (label, kind, x), (y, w) in sorted(items.items(), key=lambda i: (round(i[1][0] / 8), i[0][2])):
        text = w["text"] or w.get("icon", "")
        line = "%5d %-12s %s" % (y, kind, text)
        if "value" in w:
            line += "  = %s" % json.dumps(w["value"])
        if w.get("enabled") is False:
            line += "  (disabled)"
        for hp in list(dict.fromkeys(HELP.get(w["text"], [])))[:2] if w["text"] else []:
            line += "\n        ? " + hp[:400]
        lines.append(line)
    open(path, "w").write("\n".join(lines) + "\n")


def close():
    for _ in range(3):
        if not menu_panel():
            return
        buttons = send([{"do": "find", "type": "button"}])[0]["widgets"]
        active = [w for w in buttons if w["rect"][1] == 0 and w["rect"][3] == 50 and w.get("value") is True]
        send([{"do": "click", "id": w["id"]} for w in active] + [{"do": "wait", "frames": 3}])


def main():
    out, action, tabs = sys.argv[1], sys.argv[2], sys.argv[3:]
    os.makedirs(out, exist_ok=True)
    close()
    send([{"do": "action", "name": action}, {"do": "wait", "frames": 5}])
    for tab in tabs or [None]:
        if tab:
            send([{"do": "click", "text": tab, "type": "radio_option"}, {"do": "wait", "frames": 5}])
        panel = menu_panel()
        if not panel:
            sys.exit("no menu panel open for %s %s" % (action, tab))
        name = (tab or panel["text"]).replace(" ", "_").replace("/", "_")
        send([{"do": "scroll", "id": panel["id"], "to": 0}, PARK, {"do": "wait", "frames": 3}])
        dump(panel, os.path.join(out, name + ".txt"))
        r = subprocess.run([sys.executable, os.path.join(MANUAL, ".agents/shot.py"), name, "--panel", panel["text"],
                            "--out", os.path.join(out, name + ".webp")], capture_output=True, text=True)
        print(name, r.stdout.strip() or r.stderr.strip().splitlines()[-1])
    close()


main()
