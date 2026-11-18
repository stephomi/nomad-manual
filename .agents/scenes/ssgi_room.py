#!/usr/bin/env python3
"""Cornell-style room for the SSGI comparison (docs/images/ssgi_off.webp, ssgi_on.webp): open front,
red left wall, blue right wall, white sphere, a spotlight behind the sphere aimed at the ceiling.

ssgi_room.py <out.gltf>

In Nomad, after importing it with "replace": true (the import resets these):
- PostProcess: turn the Post Process checkbox on. Shading: turn Environment off.
- Select the Spot light row in Shading: Intensity 80, Cone angle 70, Softness 40 (the glTF intensity
  is not imported).
- Scene: select the Back wall, so the light gizmo hides. Camera: translation [0, 0, 15],
  rotation [0, 0, 0, 1], pivot [0, 2, 0]. Hover the pointer off the room.
- shot.py ssgi_on / ssgi_off --rect 405,135,630,630 (1440x900 window), toggling the SSGI checkbox.
"""
import base64, json, math, struct, sys

N = 16  # quads per wall side, enough for smooth lighting


def quad_grid(origin, du, dv, color):
    pos, col, idx = [], [], []
    for j in range(N + 1):
        for i in range(N + 1):
            u, v = i / N, j / N
            pos.append([origin[k] + du[k] * u + dv[k] * v for k in range(3)])
            col.append(color)
    for j in range(N):
        for i in range(N):
            a = j * (N + 1) + i
            idx += [a, a + 1, a + N + 2, a, a + N + 2, a + N + 1]
    return pos, col, idx


def sphere(center, r, color, seg=160, rings=80):
    pos, col, idx = [], [], []
    for j in range(rings + 1):
        t = math.pi * j / rings
        for i in range(seg + 1):
            p = 2 * math.pi * i / seg
            pos.append([center[0] + r * math.sin(t) * math.cos(p), center[1] + r * math.cos(t), center[2] + r * math.sin(t) * math.sin(p)])
            col.append(color)
    for j in range(rings):
        for i in range(seg):
            a = j * (seg + 1) + i
            b = a + seg + 1
            idx += [a, a + 1, b, a + 1, b + 1, b]
    return pos, col, idx


S = 2.0  # half size of the room, floor at y = 0
WHITE, RED, BLUE = [0.8, 0.8, 0.8, 1], [0.8, 0.04, 0.04, 1], [0.04, 0.08, 0.8, 1]
# each wall faces inward (winding chosen so the normal points into the room)
meshes = {
    "Floor": quad_grid([-S, 0, S], [2 * S, 0, 0], [0, 0, -2 * S], WHITE),
    "Ceiling": quad_grid([-S, 2 * S, -S], [2 * S, 0, 0], [0, 0, 2 * S], WHITE),
    "Back": quad_grid([-S, 0, -S], [2 * S, 0, 0], [0, 2 * S, 0], WHITE),
    "Left": quad_grid([-S, 0, S], [0, 0, -2 * S], [0, 2 * S, 0], RED),
    "Right": quad_grid([S, 0, -S], [0, 0, 2 * S], [0, 2 * S, 0], BLUE),
    "Sphere": sphere([0, 0.9, 0.6], 0.9, WHITE),
}

blob = b""
# Nomad reads the cone angles from the light itself, glTF puts them under "spot": write both
gltf = {"asset": {"version": "2.0"}, "scene": 0, "scenes": [{"nodes": []}], "nodes": [], "meshes": [],
        "accessors": [], "bufferViews": [], "buffers": [],
        "extensionsUsed": ["KHR_lights_punctual"],
        "extensions": {"KHR_lights_punctual": {"lights": [
            {"name": "Spot", "type": "spot", "color": [1, 1, 1], "intensity": 40.0,
             "innerConeAngle": 0.25, "outerConeAngle": 0.6,
             "spot": {"innerConeAngle": 0.25, "outerConeAngle": 0.6}}]}}}


def add_view(data, target):
    global blob
    while len(blob) % 4:
        blob += b"\0"
    gltf["bufferViews"].append({"buffer": 0, "byteOffset": len(blob), "byteLength": len(data), "target": target})
    blob += data
    return len(gltf["bufferViews"]) - 1


for name, (pos, col, idx) in meshes.items():
    pv = add_view(b"".join(struct.pack("<3f", *p) for p in pos), 34962)
    cv = add_view(b"".join(struct.pack("<4f", *c) for c in col), 34962)
    iv = add_view(b"".join(struct.pack("<I", i) for i in idx), 34963)
    lo = [min(p[k] for p in pos) for k in range(3)]
    hi = [max(p[k] for p in pos) for k in range(3)]
    a = len(gltf["accessors"])
    gltf["accessors"] += [
        {"bufferView": pv, "componentType": 5126, "count": len(pos), "type": "VEC3", "min": lo, "max": hi},
        {"bufferView": cv, "componentType": 5126, "count": len(col), "type": "VEC4"},
        {"bufferView": iv, "componentType": 5125, "count": len(idx), "type": "SCALAR"},
    ]
    gltf["meshes"].append({"name": name, "primitives": [{"attributes": {"POSITION": a, "COLOR_0": a + 1}, "indices": a + 2}]})
    gltf["nodes"].append({"name": name, "mesh": len(gltf["meshes"]) - 1})
    gltf["scenes"][0]["nodes"].append(len(gltf["nodes"]) - 1)

# spot behind the sphere, aimed up: glTF lights shine along -Z, a +90 degree turn around X points it to +Y
s = math.sqrt(0.5)
gltf["nodes"].append({"name": "Spot", "translation": [0, 1.0, -0.6], "rotation": [s, 0, 0, s],
                      "extensions": {"KHR_lights_punctual": {"light": 0}}})
gltf["scenes"][0]["nodes"].append(len(gltf["nodes"]) - 1)

gltf["buffers"].append({"byteLength": len(blob), "uri": "data:application/octet-stream;base64," + base64.b64encode(blob).decode()})
json.dump(gltf, open(sys.argv[1], "w"))
print(sys.argv[1], len(blob), "bytes")
