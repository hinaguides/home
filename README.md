# Home — New City, Wah Cantt

Joint-family courtyard house on 2 combined plots (6 marla + 8 marla) in New City, Wah Cantt. This repo keeps the layouts, 3D models, simulations and notes in one place, so new drawings build on the old ones instead of starting from scratch.

Open any `.html` file in a browser. Pages load three.js from a CDN, so they need internet.

## Start here

- **Fixed design rules (read first):** [`notes/design-rules.md`](notes/design-rules.md). Rule 1: noise stays at the front.
- **What each 3D concept tried and why:** [`notes/concepts.md`](notes/concepts.md)
- **Latest 3D concept:** [`models/08-concept-2-noise-zoned-3d.html`](models/08-concept-2-noise-zoned-3d.html)
- **Current plan:** [`layouts/13-ground-floor-centre-courtyard.html`](layouts/13-ground-floor-centre-courtyard.html) and [`layouts/14-first-floor-centre-courtyard.html`](layouts/14-first-floor-centre-courtyard.html)
- **Decisions and what we've learned:** [`notes/design-notes.md`](notes/design-notes.md)
- **True plot shape (use for every new drawing):** [`shared/plot.py`](shared/plot.py)
- **Printable plot map (A4):** [`print/plot-map-A4.pdf`](print/plot-map-A4.pdf), redrawn with `python3 print/plot_map_a4.py`

## Folders

| Folder | What's in it |
|---|---|
| `layouts/` | Floor plans, oldest to newest. 08 onward are to scale on the real plot. |
| `models/` | 3D models and airflow/window simulations. |
| `notes/` | Fixed rules (`design-rules.md`), decisions, constraints, physics, costs. |
| `print/` | Printable A4 plot map (PDF and PNG) and the script that draws it. |
| `shared/` | Plot geometry (`plot.py`) and the shared stylesheet (`base.css`). |

## Layouts

| File | What it shows |
|---|---|
| 00 | Ground floor plan from 4 Nov |
| 05 | Great room concept, folding doors on both sides |
| 06 | Shuttered garage, 5 ft front setback |
| 07 | Doors, windows and walking routes (interactive) |
| 08 | First to-scale layout on the real wedge plot |
| 09 | Kitchen moved to the courtyard |
| 10 | Parents, kitchen and great room all on the courtyard, sizes in feet |
| 11 | Service passage along R1 for day staff |
| 12 | First floor, R1-courtyard version |
| **13** | **Ground floor, courtyard in the centre (current)** |
| **14** | **First floor, courtyard in the centre (current)** |

05–12 were drawn with the courtyard on the R1 side; kept for history.

## Models

| File | What it shows |
|---|---|
| 00 | 3D courtyard house from 4 Nov |
| 01 | 3D massing with animated airflow (R1 courtyard) |
| 02 | One room's courtyard wall in 3D: top vents, folding doors, gallery roof |
| 03 | Window modes: cool evening, street side hot, all closed |
| 04 | Courtyard glass wall: front view and side cut with sun angles |
| 05 | Modern haveli concept: 6 design ideas, season and time-of-day sun |
| 06 | Sun study on the real plot and true north: shadows, courtyard sun through the day, heat on each side |
| 07 | Concept 1 (8 Nov): split levels, spiral stair tower, rooms let off different landings. Breaks rules 1 and 2. |
| **08** | **Concept 2 (9 Nov): noise zoned front to back, one gate at F1, solid R1/R2, back terrace. Noise zones and let-rooms views.** |

## Reusing the code

- `shared/plot.py` — `PLOT`, `BUILD` (after setbacks), `fit(rooms)` to clip room boxes to the plot, `svg_path()` to draw them at the same scale as the layouts.
- `models/01` and `02` — `box()` for massing blocks, `label()` for floating labels, and the particle airflow loop (blue in, coral out).
- `shared/base.css` — colours and room classes (`c-gray`, `c-coral`, `c-teal`, `c-amber`, `c-purple`) used by all drawings.
