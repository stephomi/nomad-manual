#!/usr/bin/env python3
"""Capture a manual screenshot from a running Nomad AI session (../../.agents/ai.py start).

shot.py <name> [--steps '<json steps>'] [--panel <title> | --rect x,y,w,h | --full] [--pad N]

Runs the steps, captures the window, crops it, and writes docs/images/<name>.webp through
webp.encode (width capped at 1440 px, lossy or lossless, whichever fits). An --out ending in .png
gets the raw full-resolution capture instead, for scripts that draw on it first.
--panel crops to the panel with that title; a panel taller than the window is scrolled and
stitched into one image. --rect crops to a GUI rect, --full keeps the whole window.
--pad grows the crop by N GUI points on each side.
--highlight <title> (with --full) surrounds that panel with a wide pale yellow halo, the style of
the page overviews. --dim N darkens the rest of the window to N% (default 100, no dimming).
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import webp  # noqa: E402

MANUAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMAD = os.path.dirname(os.path.dirname(MANUAL))
CURRENT = os.path.join(NOMAD, "tmp/ai/current")
PROBE = 20  # GUI points scrolled to find which rows of a panel scroll (its body)


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def send(folder, steps, timeout=120):
    with open(os.path.join(folder, "port")) as f:
        port = int(f.read())
    steps = [dict(s, max=4000) if s.get("do") == "capture" and "max" not in s else s for s in steps]
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": "steps", "arguments": {"steps": steps}}}).encode()
    request = urllib.request.Request("http://127.0.0.1:%d/mcp" % port, body, {"Content-Type": "application/json"})
    try:
        response = json.loads(urllib.request.urlopen(request, timeout=timeout).read())
    except OSError as e:
        fail("request failed: %s" % e)
    if "error" in response:
        fail("error: %s" % response["error"]["message"])
    content = response["result"]["content"]
    js = json.loads(content[0]["text"])
    if not js["ok"]:
        fail("error at step %d: %s" % (js["step"], js["error"]))
    frames = os.path.join(folder, "frames")
    os.makedirs(frames, exist_ok=True)
    for index, result in enumerate(js["results"]):
        if "image" in result:
            result["path"] = os.path.join(frames, "%s-%d-%d.png" % (js["id"], index, time.time() * 1e6))
            with open(result["path"], "wb") as f:
                f.write(base64.b64decode(content[1 + result["image"]]["data"]))
    return js["results"]


def crop(src, dst, box, scale):
    x, y, w, h = [round(v * scale) for v in box]
    subprocess.run(["magick", src, "-crop", "%dx%d+%d+%d" % (w, h, x, y), "+repage", dst], check=True)
    return dst


def rows(path):
    # gray pixel rows, without the right edge where the scrollbar moves
    size = subprocess.run(["magick", "identify", "-format", "%w %h", path], capture_output=True, text=True).stdout
    w, h = [int(v) for v in size.split()]
    data = subprocess.run(["magick", path, "-alpha", "off", "-colorspace", "gray", "-depth", "8", "gray:-"], capture_output=True).stdout
    keep = w - 40
    return [data[i * w:i * w + keep] for i in range(h)]


def panel_shot(folder, steps, title, pad):
    results = send(folder, steps + [{"do": "find", "type": "panel", "text": title}, {"do": "capture"}])
    panels = [w for w in results[-2]["widgets"] if w["text"].lower() == title.lower()]
    if len(panels) != 1:
        fail("expected one panel titled '%s', found %d" % (title, len(panels)))
    panel, capture = panels[0], results[-1]
    scale = capture["size"][0] / capture["gui_size"][0]
    x, y, w, h = panel["rect"]
    x, w = x - pad, w + 2 * pad
    bottom = y + h
    smax = panel.get("scroll", [0, 0])[1]
    if smax <= 0:
        return [crop(capture["path"], capture["path"] + ".crop.png", (x, y - pad, w, h + 2 * pad), scale)]

    # the body is the band of rows that changes when the panel scrolls; title bar and footer stay put
    def scrolled(s):
        return send(folder, [{"do": "scroll", "id": panel["id"], "to": s}, {"do": "wait", "frames": 4}, {"do": "capture"}])[-1]["path"]

    whole = (x, y, w, h)
    probe_s = min(PROBE, smax)
    first = rows(crop(scrolled(0), capture["path"] + ".a.png", whole, scale))
    probe = rows(crop(scrolled(probe_s), capture["path"] + ".b.png", whole, scale))
    shift = round(probe_s * scale)
    # a body row moves up by the probe shift; title bar, sticky tabs and footer rows stay in place
    moved = [i for i in range(shift, len(first)) if first[i] == probe[i - shift] and first[i] != probe[i]]
    if not moved:
        fail("could not find the scrolling part of panel '%s'" % title)
    body_top, body_bottom = y + (moved[0] - shift) / scale, y + (moved[-1] + 1) / scale

    step = body_bottom - body_top - 10
    positions = [0.0]
    while positions[-1] < smax:
        positions.append(min(positions[-1] + step, smax))
    pieces = [crop(scrolled(0), capture["path"] + ".0.png", (x, y - pad, w, body_bottom - y + pad), scale)]
    for k in range(1, len(positions)):
        delta = positions[k] - positions[k - 1]
        path = scrolled(positions[k])
        pieces.append(crop(path, path + ".crop.png", (x, body_bottom - delta, w, delta), scale))
    pieces.append(crop(path, path + ".foot.png", (x, body_bottom, w, bottom + pad - body_bottom), scale))
    send(folder, [{"do": "scroll", "id": panel["id"], "to": 0}])
    return pieces


GLOW = "#e9d66a"  # yellow halo of the original manual overviews, saturated enough to read on grey scenes
GLOW_WIDTH = 24   # blur sigma in GUI points: the halo fades out ~60 points from the panel
GLOW_ALPHA = 1.6  # the blur leaves 0.5 at the panel edge: this boosts it to 0.8


def highlight(src, dst, rect, scale, dim):
    x, y, w, h = [round(v * scale) for v in rect]
    radius = round(10 * scale)
    size = subprocess.run(["magick", "identify", "-format", "%wx%h", src], capture_output=True, text=True).stdout
    shape = "roundrectangle %d,%d %d,%d %d,%d" % (x, y, x + w, y + h, radius, radius)
    subprocess.run([
        "magick", src, "-modulate", str(dim),
        "(", "-size", size, "xc:none", "-fill", GLOW, "-draw", shape, "-blur", "0x%d" % (GLOW_WIDTH * scale),
        "-channel", "A", "-evaluate", "multiply", str(GLOW_ALPHA), "+channel", ")",
        "-composite",
        "(", src, "(", "-size", size, "xc:black", "-fill", "white", "-draw", shape, ")", "-alpha", "off", "-compose", "CopyOpacity", "-composite", ")",
        "-compose", "Over", "-composite", dst,
    ], check=True)
    return dst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--steps", default="[]")
    parser.add_argument("--panel")
    parser.add_argument("--rect")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--pad", type=float, default=0)
    parser.add_argument("--out", help="write here instead of docs/images/<name>.webp")
    parser.add_argument("--highlight")
    parser.add_argument("--dim", type=int, default=100, help="brightness of the window around the highlighted panel, %%")
    args = parser.parse_args()

    if not os.path.exists(CURRENT):
        fail("no Nomad session, run: python3 ../../.agents/ai.py start")
    with open(CURRENT) as f:
        folder = f.read().strip()
    steps = json.loads(args.steps)

    if args.panel:
        pieces = panel_shot(folder, steps, args.panel, args.pad)
    elif args.highlight and args.highlight.replace(",", "").replace(".", "").isdigit():
        # an untitled panel (the toolbox) is given by its rect: x,y,w,h
        capture = send(folder, steps + [{"do": "capture"}])[-1]
        scale = capture["size"][0] / capture["gui_size"][0]
        rect = [float(v) for v in args.highlight.split(",")]
        pieces = [highlight(capture["path"], capture["path"] + ".highlight.png", rect, scale, args.dim)]
    elif args.highlight:
        results = send(folder, steps + [{"do": "find", "type": "panel", "text": args.highlight}, {"do": "capture"}])
        panels = [w for w in results[-2]["widgets"] if w["text"].lower() == args.highlight.lower()]
        if len(panels) != 1:
            fail("expected one panel titled '%s', found %d" % (args.highlight, len(panels)))
        capture = results[-1]
        scale = capture["size"][0] / capture["gui_size"][0]
        pieces = [highlight(capture["path"], capture["path"] + ".highlight.png", panels[0]["rect"], scale, args.dim)]
    else:
        capture = send(folder, steps + [{"do": "capture"}])[-1]
        scale = capture["size"][0] / capture["gui_size"][0]
        if args.full:
            box = [0, 0] + capture["gui_size"]
        elif args.rect:
            box = [float(v) for v in args.rect.split(",")]
            box = (box[0] - args.pad, box[1] - args.pad, box[2] + 2 * args.pad, box[3] + 2 * args.pad)
        else:
            fail("needs --panel, --rect or --full")
        pieces = [crop(capture["path"], capture["path"] + ".crop.png", box, scale)]

    png = pieces[0] + ".stitch.png"
    subprocess.run(["magick"] + pieces + ["-append", png], check=True)
    out = args.out or os.path.join(MANUAL, "docs/images", args.name + ".webp")
    if out.endswith(".png"):
        os.replace(png, out)  # full resolution, for a script that draws on it before encoding
    else:
        webp.encode(png, out)
    size = subprocess.run(["magick", "identify", "-format", "%wx%h", out], capture_output=True, text=True).stdout
    print(out, size)


if __name__ == "__main__":
    main()
