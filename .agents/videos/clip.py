"""Helpers shared by the clip scripts in this folder: they build the AI API steps of a recording with
hand-like pointer and camera moves. See .agents/videos.md.

    from clip import Clip
    c = Clip(start=[1030, 620])
    c.click([175, 25]); c.stroke([840, 300], [960, 230]); c.camera([(0.4, ...)])
    print(c.json())

Everything is deterministic (fixed seed): a retake gives the same clip."""
import json
import math
import random


def min_jerk(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def reach(t):
    """Progress of a pointing move: quick start, longer landing (the speed peaks at ~40% of the time)."""
    return min_jerk(1 - (1 - t) ** 1.4)


def smooth_keys(keys, t):
    """Cubic Hermite through [(time, value)...], Catmull-Rom tangents, zero speed at both ends."""
    for i in range(len(keys) - 1):
        (t0, v0), (t1, v1) = keys[i], keys[i + 1]
        if t <= t1 or i == len(keys) - 2:
            break

    def tangent(j):
        if j == 0 or j == len(keys) - 1:
            return 0.0
        return (keys[j + 1][1] - keys[j - 1][1]) / (keys[j + 1][0] - keys[j - 1][0])

    h = t1 - t0
    u = min(max((t - t0) / h, 0.0), 1.0)
    m0, m1 = tangent(i) * h, tangent(i + 1) * h
    u2, u3 = u * u, u * u * u
    return (2 * u3 - 3 * u2 + 1) * v0 + (u3 - 2 * u2 + u) * m0 + (-2 * u3 + 3 * u2) * v1 + (u3 - u2) * m1


class Clip:
    def __init__(self, start, seed=1):
        self.steps = []
        self.pos = list(start)
        self.rng = random.Random(seed)

    def json(self):
        return json.dumps(self.steps)

    def wait(self, n):
        self.steps.append({"do": "wait", "frames": n})

    def path(self, a, b, n, bow, profile):
        """Points from a to b over n frames, bowed sideways by `bow` (fraction of the length, signed):
        a wrist moves in arcs, not straight lines."""
        dx, dy = b[0] - a[0], b[1] - a[1]
        nx, ny = -dy, dx  # perpendicular, same length as the move
        pts = []
        for i in range(n + 1):
            s = profile(i / n)
            side = bow * math.sin(math.pi * s)
            pts.append([round(a[0] + dx * s + nx * side, 1), round(a[1] + dy * s + ny * side, 1)])
        return pts

    def go(self, to, n=None):
        """Glide the pointer (no press) at a hand's pace: longer moves take longer, never twice the same."""
        dist = math.dist(self.pos, to)
        if n is None:
            n = int((18 + dist / 20) * self.rng.uniform(0.9, 1.1))
        bow = self.rng.uniform(0.04, 0.08) * self.rng.choice([-1, 1])
        self.steps.append({"do": "drag", "points": self.path(self.pos, to, max(n, 2), bow, reach), "hover": True})
        self.pos = list(to)

    def tap(self, p, hold=1):
        self.steps.append({"do": "drag", "points": [p] * (hold + 1)})
        self.pos = list(p)

    def click(self, p, hold=8):
        """Viewers must see what gets clicked: arrive, rest on the button, press long enough to read, let
        the result show. A `click` by id would jump the pointer to the widget's center. Left toolbar
        shortcuts (Sub, Unmask...) treat a held press as hold-to-use: pass hold=1 for them (the marker
        still shows the press for a few frames)."""
        self.go(p)
        self.wait(self.rng.randint(17, 23))
        self.tap(p, hold)
        self.wait(20)

    def stroke(self, a, b, n, bow=0.06):
        """A sculpting drag from a to b, slightly curved, eased at both ends. The pointer must be at a."""
        self.steps.append({"do": "drag", "points": self.path(a, b, n, bow, min_jerk)})
        self.pos = list(b)

    def camera(self, frames, yaw=(), pitch=(), dolly=(), pan_x=(), pan_y=()):
        """One continuous camera move. Each channel is a list of (time 0..1, value) keys, starting from
        0 at time 0: degrees for yaw and pitch, a zoom factor for dolly (0.9 = 10% closer), a fraction of
        the distance for pans. Channels with keys at different times overlap, as a hand would."""
        def channel(keys, start=0.0):
            keys = [(0.0, start)] + list(keys)
            if keys[-1][0] < 1.0:
                keys.append((1.0, keys[-1][1]))
            return lambda t: smooth_keys(keys, t)

        curves = [channel(yaw), channel(pitch), channel([(t, math.log(v)) for t, v in dolly]),
                  channel(pan_x), channel(pan_y)]
        prev = [0.0] * 5
        entries = []
        for i in range(1, frames + 1):
            cur = [c(i / frames) for c in curves]
            d = [c - p for c, p in zip(cur, prev)]
            prev = cur
            entries.append({"orbit": [round(d[0], 4), round(d[1], 4)], "dolly": round(math.exp(d[2]), 6),
                            "pan": [round(d[3], 5), round(d[4], 5)]})
        self.steps.append({"do": "camera", "path": entries})
