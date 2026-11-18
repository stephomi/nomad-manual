#!/usr/bin/env python3
"""Encode manual images for the web: the rule every screenshot goes through.

webp.py <image> [image ...]        # re-encode in place (webp, png or jpg; png/jpg become .webp)

- Width capped at MAX_WIDTH: the page column is ~690 css px, so 1440 px is sharp on a 2x screen.
- Lossy WebP at QUALITY, unless lossless is about as small (clean UI crops), then lossless.
  UI text stays sharp at quality 90; renders and noisy overviews shrink ~20x.

shot.py and extras.py call encode() for every image they write.
"""
import os, subprocess, sys, tempfile

MAX_WIDTH = 1440
QUALITY = 90
LOSSLESS_MARGIN = 1.15  # keep lossless when it is at most 15% bigger than lossy


def encode(src, out):
    """src: any image magick or dwebp reads; out: the .webp to write (may be src itself)"""
    with tempfile.TemporaryDirectory() as tmp:
        png = os.path.join(tmp, "in.png")
        if src.lower().endswith(".webp"):
            subprocess.run(["dwebp", "-quiet", src, "-o", png], check=True)
        else:
            subprocess.run(["magick", src, png], check=True)
        width = int(subprocess.check_output(["magick", "identify", "-format", "%w", png], text=True))
        if width > MAX_WIDTH:
            subprocess.run(["magick", png, "-filter", "Lanczos", "-resize", f"{MAX_WIDTH}x", png], check=True)
        lossy, lossless = os.path.join(tmp, "lossy.webp"), os.path.join(tmp, "lossless.webp")
        subprocess.run(["cwebp", "-quiet", "-q", str(QUALITY), "-m", "6", "-metadata", "icc", png, "-o", lossy], check=True)
        subprocess.run(["cwebp", "-quiet", "-lossless", "-metadata", "icc", png, "-o", lossless], check=True)
        best = lossless if os.path.getsize(lossless) <= os.path.getsize(lossy) * LOSSLESS_MARGIN else lossy
        os.replace(best, out)
    return out


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    before = sum(os.path.getsize(f) for f in files)

    def one(f):
        out = os.path.splitext(f)[0] + ".webp"
        encode(f, out)
        if out != f:
            os.remove(f)
        return os.path.getsize(out)

    with ThreadPoolExecutor(8) as ex:
        after = sum(ex.map(one, files))
    print("%d images: %.1f MB -> %.1f MB" % (len(files), before / 1e6, after / 1e6))
