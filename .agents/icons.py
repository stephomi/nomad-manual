#!/usr/bin/env python3
"""Render app icons into docs/icons, from the masters in ../../tools/icons.

icons.py <name> [name ...]    # writes docs/icons/<name>.webp
icons.py --used               # every icon the English and translated pages reference

Same rules as the app's tools/conv-icons.py: an SVG is rasterized at 64px (tool_gizmo at 128px);
a painted tool PNG wins over an SVG of the same name, shaved 7% on each side, at 128px.
Colored icons (not inverted in light mode) go in the `colored` list of config.mts.
"""
import glob, os, re, subprocess, sys, tempfile

MANUAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTERS = os.path.join(os.path.dirname(os.path.dirname(MANUAL)), "tools", "icons")
OUT = os.path.join(MANUAL, "docs", "icons")
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"
PAD = 0.07


def render(name, tmp):
    png, svg = os.path.join(MASTERS, name + ".png"), os.path.join(MASTERS, name + ".svg")
    out_png = os.path.join(tmp, name + ".png")
    if os.path.exists(png):
        w = int(subprocess.check_output(["magick", png, "-format", "%w", "info:"], text=True))
        side = int(w * (1 - 2 * PAD) + 0.5)
        subprocess.run(["magick", png, "-background", "none", "-gravity", "center", "-extent", f"{side}x{side}",
                        "-filter", "Lanczos", "-resize", "128x128!", out_png], check=True)
    elif os.path.exists(svg):
        size = "128" if name == "tool_gizmo" else "64"
        subprocess.run([INKSCAPE, "--export-type=png", "-w", size, "-h", size, "-o", out_png, svg],
                       check=True, stderr=subprocess.DEVNULL)
    else:
        return False
    subprocess.run(["cwebp", "-quiet", "-lossless", "-exact", out_png, "-o", os.path.join(OUT, name + ".webp")], check=True)
    return True


def used():
    names = set()
    for f in glob.glob(os.path.join(MANUAL, "docs", "**", "*.md"), recursive=True):
        names |= set(re.findall(r"/icons/([A-Za-z0-9_]+)\.webp", open(f, encoding="utf8").read()))
    return sorted(names)


def main():
    names = used() if sys.argv[1:] == ["--used"] else sys.argv[1:]
    if not names:
        sys.exit(__doc__)
    missing = []
    with tempfile.TemporaryDirectory() as tmp:
        for n in names:
            if not render(n, tmp):
                missing.append(n)
    print("%d rendered" % (len(names) - len(missing)))
    if missing:
        print("no master:", " ".join(missing))


main()
