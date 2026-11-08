# Design rules — New City, Wah Cantt house

Fixed rules every layout, sketch and 3D model must follow. They override any earlier drawing. When a new rule is set, add it here with the date.

## Rule 1: Noise stays at the front (fundamental) — set 2026-11-09

The living room is the noisiest space in the house: TV, children playing, people talking. Its noise must never spread to rooms where someone wants to rest, sleep, work or hold a meeting.

- **Never put the living room in the centre of the house.** A central living room spreads noise equally to every room around it.
- Plan the house in 3 bands, front to back:
  - **Loud band, along the front road:** living room, dining, kitchen, car porch, foyer, upstairs play/lounge, gym.
  - **Buffer band, in the middle:** courtyard, stairs, halls, baths, stores, pantry, utility, laundry.
  - **Quiet band, along the back (neighbours' side):** parents' room, office, bedrooms, back terrace.
- A quiet room must never share a wall with a loud room. If it can't be avoided, put a bath, wardrobe or store between them as a buffer wall.
- Upstairs follows the same rule: loud rooms over loud rooms, quiet over quiet.
- Check every new layout against this rule before anything else. The 3D model's **Noise zones** view colours each room loud, buffer or quiet.

## Rule 2: Only the front has openings — set 2026-11-09

- The society does not allow any opening or garage on R1 or R2.
- R1 and R2 walls are **solid**: no gate, door, garage, shutter or window.
- **One main gate only, at F1 on the front.** Cars and people both enter there.
- Supersedes: the R1 car with its own R1 stair door (8 Nov), and the staff passage along the inside of R1 to a back lane (6 Nov).

## Rule 3: Inside courtyard with a long wall — set 2026-11-09

- The courtyard is enclosed. Nothing can see into it from outside.
- Where it touches a road, its wall runs full height (about 13 ft) with no openings.

## Rule 4: Terrace only at the back — set 2026-11-09

- No terrace on the R2 side or the front.
- If there is a terrace, it sits at the back (centre or toward R2), walled on the neighbours' side with a long wall.
- Rooms around it look onto it through glass windows.

## Rule 5: Draw on the real plot — set 2026-11-07

Every drawing uses the true plot shape and size (`shared/plot.py`), with roads, north and the 5 ft front and back setbacks. Never a generic rectangle.

## Room list (as of 2026-11-09)

- **Must have:** living room, dining, kitchen with service area (cook, laundry, ironing, store), live-in maid's room, gym, office, parents' room with bath, bedrooms upstairs, parking for 2 cars, inside courtyard with lawn.
- **Not needed:** prayer room, separate drawing room.
