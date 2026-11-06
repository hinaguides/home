"""A4 portrait print of the plot map, filling the page. Run from repo root:
    python3 print/plot_map_a4.py
Same orientation as the society map: back wall on the left, front road on the right,
R1 road at the top, R2 road at the bottom. Compass from the map: R1 faces north-east."""
import sys, math
sys.path.insert(0, "shared")
from plot import CORNERS, PLOT
from shapely.geometry import Polygon
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

W, H = 210, 297
S = 3.15                          # mm per ft, sized to fill the page
OX, OY = 14, 15                   # paper position of corner B (back wall, R2 end); y measured upward
def P(x, y): return OX + y * S, OY + x * S   # towards front -> right, along back wall from R2 -> up

fig = plt.figure(figsize=(W / 25.4, H / 25.4))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
ink, mid = "#2C2C2A", "#5F5E5A"

# the 2 original plots: dividing line from the front point F1 square to the back wall
DX = CORNERS["F1"][0]
r1_side = Polygon([(DX, 0), CORNERS["R1"], CORNERS["C2"], CORNERS["F2"], CORNERS["F1"]])
r2_side = PLOT.difference(r1_side)
ax.fill(*zip(*[P(x, y) for x, y in r2_side.exterior.coords]), color="#E8F0F8", zorder=1)
ax.fill(*zip(*[P(x, y) for x, y in r1_side.exterior.coords]), color="#EAF4EC", zorder=1)
ax.plot(*zip(P(DX, 0), P(*CORNERS["F1"])), color=mid, lw=0.9, ls=(0, (5, 3)), zorder=2)
pts = [P(*c) for c in CORNERS.values()]
ax.plot(*zip(*(pts + pts[:1])), color=ink, lw=1.8, zorder=3)

def lab(x, y, t, size=10, rot=0, col=mid, w="normal"):
    ax.text(*P(x, y), t, ha="center", va="center", fontsize=size, color=col, rotation=rot, weight=w)

# edge lengths (back wall shown as its 2 parts)
names = list(CORNERS); cx, cy = PLOT.centroid.x, PLOT.centroid.y
for i, a in enumerate(names):
    if a == "B":
        continue
    p, q = CORNERS[a], CORNERS[names[(i + 1) % len(names)]]
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = mx - cx, my - cy; d = math.hypot(dx, dy)
    lab(mx + dx / d * 3.3, my + dy / d * 3.3, f"{math.dist(p, q):.1f} ft", 10, col=ink)
lab(DX / 2, -3, f"{DX:.1f} ft", 10, rot=90, col=ink)
lab((DX + 83.2) / 2, -3, f"{83.2 - DX:.1f} ft", 10, rot=90, col=ink)
lab(DX + 2.2, 26, f"{CORNERS['F1'][1]:.1f} ft", 10, col=ink)

# roads and back
lab(62, 2.6, "BACK  ·  neighbours  ·  83.2 ft", 10, rot=90)
lab(84.5, 26, "R1 road", 12, rot=-13)
ax.text(118, 33, "R2 road", ha="center", va="center", fontsize=12, color=mid, rotation=18)
ax.text(199, 140, "FRONT road", ha="center", va="center", fontsize=12, color=mid, rotation=-76)

# plot areas
lab(18, 22, "6 marla", 15, col=ink, w="bold")
lab(14, 22, f"{r2_side.area:,.0f} sq ft", 11)
lab(62, 24, "8 marla", 15, col=ink, w="bold")
lab(58, 24, f"{r1_side.area:,.0f} sq ft", 11)

# title, bottom-right empty corner
ax.text(200, 46, "Plot map", fontsize=17, color=ink, weight="bold", ha="right")
ax.text(200, 38, "New City, Wah Cantt", fontsize=11, color=mid, ha="right")
ax.text(200, 31, f"Total {PLOT.area:,.0f} sq ft  ·  14 marla", fontsize=10, color=mid, ha="right")

# compass: R1 faces north-east (up on this page), front faces south-east (right)
CXc, CYc, R = 183, 80, 10
for ang, txt, strong in ((135, "N", True), (45, "E", False), (315, "S", False), (225, "W", False)):
    a = math.radians(ang); ex, ey = CXc + R * math.cos(a), CYc + R * math.sin(a)
    ax.annotate("", xy=(ex, ey), xytext=(CXc, CYc),
                arrowprops=dict(arrowstyle="-|>" if strong else "-", color=ink if strong else mid,
                                lw=1.6 if strong else 0.8, mutation_scale=12))
    ax.text(CXc + (R + 5) * math.cos(a), CYc + (R + 5) * math.sin(a), txt, ha="center", va="center",
            fontsize=13 if strong else 10, color=ink if strong else mid, weight="bold" if strong else "normal")

fig.savefig("print/plot-map-A4.pdf")
fig.savefig("print/plot-map-A4.png", dpi=300)
xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
print("extent mm x", round(min(xs)), round(max(xs)), "y", round(min(ys)), round(max(ys)))
