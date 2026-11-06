"""
True plot boundary for the New City, Wah Cantt house (6 marla + 8 marla combined).

All coordinates are in feet. Origin = back-left corner (where the back wall meets R2).
x runs along the back wall towards R1, y runs from the back wall towards the front road.

Use this as the starting point for every new layout so drawings are always to scale.

    python3 shared/plot.py            # prints areas and checks room fits
    from plot import PLOT, BUILD      # reuse in other scripts

Needs: pip install shapely
"""
import math
from shapely.geometry import Polygon, LineString, box

# Corners traced from the society map, converted to feet (back wall = 83.2 ft)
# B = back-left (R2 end), R1 = back-right, C2/F2 = cut corner on R1 front,
# F1 = front midpoint, C1/R2 = cut corner on R2 front
CORNERS = {
    "B":  (0.0, 0.0),
    "R1": (83.2, 0.0),
    "C2": (71.3, 52.4),
    "F2": (64.4, 56.3),
    "F1": (39.8, 49.9),
    "C1": (19.1, 44.6),
    "R2": (12.6, 38.8),
}
PLOT = Polygon(list(CORNERS.values()))

# Setbacks (New City rule for 6 and 8 marla plots): 5 ft front, 5 ft back, none on R1/R2 sides.
# Confirm in writing that this still applies after the plots are merged.
FRONT_SETBACK = 5
BACK_SETBACK = 5

_front_edge = LineString([CORNERS[k] for k in ("R2", "C1", "F1", "F2", "C2")])
_build = PLOT.difference(_front_edge.buffer(FRONT_SETBACK, cap_style=3, join_style=2))
_build = _build.difference(box(-10, -10, 100, BACK_SETBACK))
BUILD = max(_build.geoms, key=lambda g: g.area) if _build.geom_type != "Polygon" else _build


def edge_lengths():
    pts = list(CORNERS.items())
    return {f"{a}-{b}": round(math.dist(p, q), 1)
            for (a, p), (b, q) in zip(pts, pts[1:] + pts[:1])}


def fit(rooms):
    """rooms = {name: (x1, y1, x2, y2)} in feet. Returns the clipped shapes inside BUILD."""
    out = {}
    for name, r in rooms.items():
        g = box(*r).intersection(BUILD)
        b = g.bounds
        out[name] = {"shape": g, "area": round(g.area),
                     "w": round(b[2] - b[0], 1), "d": round(b[3] - b[1], 1)}
    return out


def svg_path(g, scale=6.6, ox=50, oy=40):
    """Polygon in feet -> SVG path string (default scale matches the layout drawings)."""
    polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
    return " ".join("M" + " L".join(f"{ox + x * scale:.1f} {oy + y * scale:.1f}"
                                     for x, y in p.exterior.coords) + "Z" for p in polys)


if __name__ == "__main__":
    print("Plot area:", round(PLOT.area), "sq ft")
    print("Buildable ground floor:", round(BUILD.area), "sq ft")
    print("Edges (ft):", edge_lengths())
