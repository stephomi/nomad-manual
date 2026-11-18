#!/usr/bin/env python3
"""Sphere with UVs and an embedded colour texture, for the Material > Textures screenshots.

textured_sphere.py <out.gltf>   (needs ImageMagick for the texture)
"""
import base64, json, math, struct, subprocess, sys

SEG, RINGS = 96, 48
pos, uv, idx = [], [], []
for j in range(RINGS + 1):
    t = math.pi * j / RINGS
    for i in range(SEG + 1):
        p = 2 * math.pi * i / SEG
        pos.append([math.sin(t) * math.cos(p), math.cos(t), math.sin(t) * math.sin(p)])
        uv.append([i / SEG, j / RINGS])
for j in range(RINGS):
    for i in range(SEG):
        a = j * (SEG + 1) + i
        b = a + SEG + 1
        idx += [a, a + 1, b, a + 1, b + 1, b]

# colourful, recognisable texture: a hue gradient with a checker on top
png = subprocess.run(["magick", "-size", "512x1", "gradient:", "-rotate", "90", "-resize", "512x512!",
                      "-set", "colorspace", "HSL", "(", "+clone", "-fill", "gray(75%)", "-colorize", "100", ")",
                      "(", "+clone", "-fill", "gray(55%)", "-colorize", "100", ")", "-combine", "-set", "colorspace", "HSL",
                      "-colorspace", "sRGB",
                      "(", "-size", "64x64", "pattern:checkerboard", "-scale", "800%", "-fill", "white", "-colorize", "55%", ")",
                      "-compose", "multiply", "-composite", "png:-"],
                     capture_output=True, check=True).stdout

blob = b""
views = []


def add(data, target=None):
    global blob
    while len(blob) % 4:
        blob += b"\0"
    view = {"buffer": 0, "byteOffset": len(blob), "byteLength": len(data)}
    if target:
        view["target"] = target
    views.append(view)
    blob += data
    return len(views) - 1


pv = add(b"".join(struct.pack("<3f", *p) for p in pos), 34962)
nv = add(b"".join(struct.pack("<3f", *p) for p in pos), 34962)
tv = add(b"".join(struct.pack("<2f", *t) for t in uv), 34962)
iv = add(b"".join(struct.pack("<I", i) for i in idx), 34963)
img = add(png)

gltf = {
    "asset": {"version": "2.0"}, "scene": 0, "scenes": [{"nodes": [0]}],
    "nodes": [{"name": "Textured", "mesh": 0}],
    "meshes": [{"name": "Textured", "primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2}, "indices": 3, "material": 0}]}],
    "materials": [{"name": "Textured", "pbrMetallicRoughness": {"baseColorTexture": {"index": 0}, "metallicFactor": 0, "roughnessFactor": 0.4}}],
    "textures": [{"source": 0}], "images": [{"name": "color", "mimeType": "image/png", "bufferView": img}],
    "accessors": [
        {"bufferView": pv, "componentType": 5126, "count": len(pos), "type": "VEC3", "min": [-1, -1, -1], "max": [1, 1, 1]},
        {"bufferView": nv, "componentType": 5126, "count": len(pos), "type": "VEC3"},
        {"bufferView": tv, "componentType": 5126, "count": len(uv), "type": "VEC2"},
        {"bufferView": iv, "componentType": 5125, "count": len(idx), "type": "SCALAR"},
    ],
    "bufferViews": views,
    "buffers": [{"byteLength": len(blob), "uri": "data:application/octet-stream;base64," + base64.b64encode(blob).decode()}],
}
json.dump(gltf, open(sys.argv[1], "w"))
print(sys.argv[1], len(blob), "bytes")
