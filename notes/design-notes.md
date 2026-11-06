# Design notes — New City, Wah Cantt courtyard house

Running record of decisions, constraints and what we learned. Newest decisions win; superseded ideas are kept so the reasoning isn't lost.

## The plot

- 2 plots combined: 6 marla + 8 marla, about 3,487 sq ft total. Exact boundary lives in `shared/plot.py`.
- It's a **wedge**, not a rectangle: 83 ft back wall (against neighbours), 47 ft front, R2 side about 41 ft, R1 side about 54 ft, both road sides slanting inward. R2 side is shallow, R1 side is deeper.
- Neighbours only at the back. Roads on R1, R2 and the front.
- **Setbacks:** 5 ft front, 5 ft back, none on R1/R2 (because it's 2 small plots). About 2,777 sq ft buildable on the ground floor.
- **To confirm with New City in writing:** that the 6/8 marla rules still apply after merging (merged 14 marla plots sometimes get side setbacks), and whether a gate/shutter can sit at the plot line or only at the setback line.

## The idea: an introverted house (modern haveli)

- Closed to the roads: blank walls, high roshandans only, front fully blocked.
- Courtyard is **inside**, never at the front. **Decision: courtyard in the centre, rooms on all 4 sides** (replaced the earlier R1-side courtyard).
- Glass only where it faces inward; solid walls everywhere else.
- Garage looks like a plain workshop with a roller shutter, no open car porch.

## Rooms

**Ground floor:** great room (living + drawing + dining in one), kitchen, staff room, laundry/store, hall, stairs, parents' room with bath, entry + guest WC, office, garage, courtyard.
**First floor:** all private bedrooms (Ehsan's suite, brother's room), kids' room, family lounge, guest room, baths.

Rules set by Ehsan:
- No separate drawing room. One **great room** used daily by the family and by guests. Dining table is a must, shared, in the open.
- Great room separable with **folding glass doors on both sides** (house side and courtyard side). Both open = one continuous space.
- Public spaces get no solid doors: wooden doors with full clear glass, kitchen included.
- **Must face the courtyard:** parents' room, great room, kitchen. **Don't need it:** staff room, office, garage.
- Kitchen and service rooms grouped together, reachable by non-live-in staff from outside without passing through living spaces.
- Staff access: **front service gate + 3.5 ft passage along the inside of the R1 wall to the back lane** (chosen over a side door on R1). All gates stay at the front.
- Sizes on plans in feet.

Current layout: `layouts/13-ground-floor-centre-courtyard.html` and `layouts/14-first-floor-centre-courtyard.html`.

Known weak spots in the current layout:
- Garage 18×18: one car comfortably, second only if small.
- Kitchen 18×10: galley, no island.
- Kids' room on the R2 side, about 12 ft wide and tapering, no courtyard view. Option: swap with the guest room over the garage.
- Upstairs common bath only 12×5.

## Two-storey wall on the road side

Possible, but not as a freestanding boundary wall (unsafe; societies cap those around 7 ft). Build it as part of the house: RCC frame, columns every 10–12 ft, beams at first floor and roof, 9" brick infill. Best as the outer wall of an upstairs gallery. Keep the courtyard's short side at least about 15 ft or it becomes a dark well.

## How the airflow works (stack effect + courtyard effect)

1. **Down:** at night roofs and the courtyard floor lose heat to the sky (radiative cooling). Cool, heavy air sinks and pools in the enclosed courtyard.
2. **Across, low:** rooms pull that cool air in through openings on the courtyard side.
3. **Up and out, high:** air warms in the room, rises, and leaves through openings near the ceiling.

Physics: warm air is less dense (40°C air is about 6% lighter than 20°C air), so cool air sinks under it and pushes it up (buoyancy → convection). The pull grows with the height gap between inlet and outlet; that's why stairwells and chimneys work so well.

Outlet position:
- **Near the ceiling — best.** Works even with no wind.
- **Middle — weaker.** A hot layer stays trapped above the window.
- **Bottom — no stack effect at all.** Only works when wind blows; also brings dust, noise, eyes.

## Roshandan (clerestory window / "ventilator")

- Open area at least equal to the opening part of the courtyard window. 2 small ones per room or 1 strip 1–1.5 ft tall.
- Sill about 7 ft or higher, top close to the ceiling.
- Closable (hinged glass shutter with chain or rod), insect mesh, small chajja above.
- Use the stairwell as a chimney: openable vents at the top of the mumty.
- Light floor, plants or a small water trough in the courtyard, not dark tiles.

## Courtyard glass wall — 3 parts

1. **Top band (2.5–3 ft under the ceiling):** hopper vents tilting inward. Hot air out. Fixed mesh.
2. **Main zone (floor to 7.5 ft):** folding doors on part of the width (open about 90%, sliding only 50%), fixed glass on the rest. Pleated mesh.
3. **Gallery roof outside (4 ft):** overhang blocks steep summer sun, lets low winter sun in. Best on glass facing south to south-east.

Plus: curtain track at the 7.5 ft transom bar so curtains never block the vents; double glazing (uPVC or thermally broken aluminium) for Wah winters.

## Daily window routine

- **Evening to early morning:** open everything; courtyard air flushes the house.
- **About 11 am:** close up; thick walls hold the coolness.
- **Street side hot or dusty:** roshandan shut, use the courtyard wall's low and high panes.
- **Winter / summer midday:** everything shut.
- AC bedrooms: roshandans for spring, autumn and nights; must seal well when AC runs.

## Kitchen

- Strong hood vented outside, plus a roshandan. Desi cooking spreads smell and grease.
- Idea: small "dirty"/wet kitchen toward the service lane, main kitchen kept clean.
- Reeded or frosted glass on the kitchen door if counters shouldn't be visible to guests.

## Garage

- Single 16–18 ft motorised, insulated roller shutter in the wall colour.
- 5 ft front strip as a ramp up to the shutter (keeps rain out).
- Door straight into the hall, not the great room.
- High vents or an exhaust fan; back wall for shelves, tools, UPS.

## Glass and doors — costs (rough, Nov 2026, get 2–3 quotes)

- **Tempered (toughened) glass only**, never plain. Can't be cut or drilled after tempering — measure first.
- Wood frame + clear glass internal door (3×7): about PKR 75,000–120,000 vs premium solid door PKR 68,000–108,000. Extra for 5–6 public doors: about PKR 50,000–120,000 total.
- Fixed framed glass partition: about PKR 1,050–1,890 per sq ft.
- Folding glass doors: about PKR 2,500–4,500 per sq ft.
  - Office opening (10 ft wide, 9 ft high): PKR 225,000–400,000
  - Kitchen (12 ft): PKR 270,000–490,000
  - Great room, 2 sides of 18 ft: PKR 800,000–1,450,000
  - All 3: about PKR 1,300,000–2,300,000. Double glazing roughly doubles the glass part.
- Advice: folding doors on the great room (the one that actually opens fully); fixed glass + one door for the office (quieter, half the price); think twice about a glass wall for the kitchen (loses cabinets, oil coats it).
- Pick one frame colour for the whole house (black or dark wood).

## Courtyard cover

If covered, lift the cover about 2 ft above the roof (timber louvers over glass) so hot air escapes — otherwise it becomes a greenhouse.
