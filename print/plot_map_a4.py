"""A4 portrait print of the plot map at exact 1:100 scale. Run from repo root:
    python3 print/plot_map_a4.py
Back wall runs down the left side of the page, front road on the right."""
import sys, math
sys.path.insert(0, "shared")
from plot import CORNERS, PLOT
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

S = 0.3048 * 1000 / 100          # 1:100 -> 3.048 mm on paper per ft
W, H = 210, 297                   # A4 portrait, mm
fig = plt.figure(figsize=(W / 25.4, H / 25.4))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

OX, OY = 30, 265                  # paper position of corner B (back wall, R2 end)
def P(x, y): return OX + y * S, OY - x * S   # plot y (towards front) -> right; plot x (along back) -> down

ink, mid = "#2C2C2A", "#5F5E5A"
pts = [P(*c) for c in CORNERS.values()]
# the 2 original plots: dividing line runs from the front point F1 square to the back wall
from shapely.geometry import Polygon
DX = CORNERS["F1"][0]
plot3 = Polygon([(DX, 0), CORNERS["R1"], CORNERS["C2"], CORNERS["F2"], CORNERS["F1"]])  # R1 side, 8 marla
plot1 = PLOT.difference(plot3)                                                           # R2 side, 6 marla
ax.fill(*zip(*[P(x, y) for x, y in plot1.exterior.coords]), color="#E8F0F8", zorder=1)
ax.fill(*zip(*[P(x, y) for x, y in plot3.exterior.coords]), color="#EAF4EC", zorder=1)
ax.plot(*zip(P(DX, 0), P(*CORNERS["F1"])), color="#5F5E5A", lw=0.9, ls=(0, (5, 3)), zorder=2)
ax.plot(*zip(*(pts + pts[:1])), color=ink, lw=1.6, zorder=3)

names = list(CORNERS); cx, cy = PLOT.centroid.x, PLOT.centroid.y
for i, a in enumerate(names):
    if a == "B":
        continue
    p, q = CORNERS[a], CORNERS[names[(i + 1) % len(names)]]
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = mx - cx, my - cy; d = math.hypot(dx, dy)
    ax.text(*P(mx + dx / d * 3.5, my + dy / d * 3.5), f"{math.dist(p, q):.1f} ft",
            ha="center", va="center", fontsize=9, color=ink)

def lab(x, y, t, size=10.5, rot=0, col=mid, w="normal"):
    ax.text(*P(x, y), t, ha="center", va="center", fontsize=size, color=col, rotation=rot, weight=w)
lab(41.6, -7.5, "BACK  ·  neighbours' houses  ·  83.2 ft", 10, rot=90)
ax.text(70, 258, "R2 road", ha="center", va="center", fontsize=11, color=mid, rotation=-18)
lab(84, 24, "R1 road", 11, rot=13)
lab(40, 54.5, "FRONT road", 10, rot=78)
lab(DX / 2, -3.2, f"{DX:.1f} ft", 9, col=ink, rot=90)
lab((DX + 83.2) / 2, -3.2, f"{83.2 - DX:.1f} ft", 9, col=ink, rot=90)
lab(DX - 2.2, 26, f"{CORNERS['F1'][1]:.1f} ft", 9, col=ink)
lab(19, 22, "Plot 1", 13, col=ink, w="bold")
lab(23, 22, f"6 marla  ·  {plot1.area:,.0f} sq ft", 9.5)
lab(60, 26, "Plot 3", 13, col=ink, w="bold")
lab(64, 26, f"8 marla  ·  {plot3.area:,.0f} sq ft", 9.5)

ax.text(30, 284, "Plot map — New City, Wah Cantt", fontsize=15, color=ink, weight="bold", va="center")
ax.text(30, 277, f"Total {PLOT.area:,.0f} sq ft (14 marla)  ·  scale 1:100, about 3 mm on paper = 1 ft  ·  print at 100%", fontsize=9, color=mid, va="center")

y0 = 256; LX = 140
sx = LX; y0 = 238
for i in range(4):
    ax.fill_between([sx + i * 5 * S, sx + (i + 1) * 5 * S], y0 + 1.8, y0 + 4.2,
                    color=ink if i % 2 == 0 else "white", edgecolor=ink, lw=0.6)
for i in range(5):
    ax.text(sx + i * 5 * S, y0 - 1, f"{i*5}", ha="center", fontsize=7.5, color=mid)
ax.text(sx + 20 * S + 3, y0 + 3, "ft", fontsize=8, color=mid, va="center")

fig.savefig("print/plot-map-A4.pdf")
fig.savefig("print/plot-map-A4.png", dpi=300)
xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
print("plot extent mm x", round(min(xs)), round(max(xs)), "y", round(min(ys)), round(max(ys)))
