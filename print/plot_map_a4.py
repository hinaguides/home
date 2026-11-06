"""A4 portrait print of the plot map at exact 1:100 scale. Run from repo root:
    python3 print/plot_map_a4.py
Back wall runs down the left side of the page, front road on the right."""
import sys, math
sys.path.insert(0, "shared")
from plot import CORNERS, PLOT, BUILD
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
ax.fill(*zip(*pts), color="#F1EFE8", zorder=1)
ax.plot(*zip(*(pts + pts[:1])), color=ink, lw=1.6, zorder=3)
ax.plot(*zip(*[P(x, y) for x, y in BUILD.exterior.coords]), color=mid, lw=0.8, ls=(0, (4, 3)), zorder=2)

names = list(CORNERS); cx, cy = PLOT.centroid.x, PLOT.centroid.y
for i, a in enumerate(names):
    p, q = CORNERS[a], CORNERS[names[(i + 1) % len(names)]]
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = mx - cx, my - cy; d = math.hypot(dx, dy)
    ax.text(*P(mx + dx / d * 3.5, my + dy / d * 3.5), f"{math.dist(p, q):.1f} ft",
            ha="center", va="center", fontsize=9, color=ink)

def lab(x, y, t, size=10.5, rot=0, col=mid, w="normal"):
    ax.text(*P(x, y), t, ha="center", va="center", fontsize=size, color=col, rotation=rot, weight=w)
lab(41.6, -6.5, "BACK  ·  neighbours' houses", 10, rot=90)
ax.text(70, 258, "R2 road", ha="center", va="center", fontsize=11, color=mid, rotation=-18)
lab(84, 24, "R1 road", 11, rot=13)
lab(40, 54.5, "FRONT road", 10, rot=78)
lab(46, 24, f"Plot area  {PLOT.area:,.0f} sq ft", 13, col=ink, w="bold")
lab(51, 24, "6 marla + 8 marla, combined", 9.5)
lab(55, 24, f"Buildable ground floor ≈ {BUILD.area:,.0f} sq ft", 9.5)

ax.text(30, 284, "Plot map — New City, Wah Cantt", fontsize=15, color=ink, weight="bold", va="center")
ax.text(30, 277, "Scale 1:100  ·  1 cm on paper = 1 m  ·  print at 100% (actual size)", fontsize=9, color=mid, va="center")

y0 = 256; LX = 140
ax.plot([LX, LX+10], [y0 + 6, y0 + 6], color=ink, lw=1.6); ax.text(LX+12, y0 + 6, "Plot boundary", fontsize=8.5, color=mid, va="center")
ax.plot([LX, LX+10], [y0, y0], color=mid, lw=0.8, ls=(0, (4, 3))); ax.text(LX+12, y0, "5 ft setback, front and back", fontsize=8.5, color=mid, va="center")
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
