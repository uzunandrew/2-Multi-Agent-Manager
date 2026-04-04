# Instructions for vision model: structured description of plumbing drawings

You receive a PNG image from the project documentation of section ВК (water supply and sewerage). Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from the description without viewing the image.

## Scope and limitations

**6 types of plumbing drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|-----------|
| Floor plans with piping | 35% | B1/T3/T4/K1/K2 routing on floor plans |
| Axonometric schematics | 25% | System risers and branches |
| Equipment/pump room layouts | 12% | Pump stations, water meter rooms |
| Details and nodes | 10% | Pipe connections, penetrations, supports |
| Tables and specifications | 10% | Pipe schedules, fixture counts |
| Sections | 8% | Building cross-sections with risers |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, cipher, organization)
- Revision tables
- Sheet numbers and their titles
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.

## Principle of reading

Water supply systems are read from inlet to fixture: city main → water meter → main pipe → riser → branch → fixture. Sewerage systems are read from fixture to outlet: fixture → branch → riser → building drain → city sewer. For each riser, trace the full path and describe every element in sequence: pipe diameter, material, fittings, valves, transitions.

## Description format: AXONOMETRIC WATER SUPPLY DIAGRAM

If the image is an axonometric view of a water supply system (B1, Т3, Т4, Т4ц):

```
AXONOMETRIC DIAGRAM: [title, e.g. "Аксонометрическая схема системы Т3"]
SYSTEM: B1 / Т3 / Т4 / Т4ц / В1+Т3
SCALE: no scale (typical for axonometric views)

INLET / SOURCE:
- Inlet point: at axes [X-Y], elevation [+X.XXX]
- Inlet diameter: Ду[mm]
- Material: [PPR/steel/polyethylene]
- Water meter node: [description, if visible]

MAINS:
- Horizontal main: Ду[mm], elevation [+X.XXX], material [PPR/steel]
- Section from axis [X] to axis [Y]: Ду[mm], length [m] (if indicated)
- Main slope: i=[value] (if indicated)

RISERS:
- Ст.Т3-1: Ду[mm], from elev. [+X.XXX] to elev. [+X.XXX], at axes [X-Y]
- Ст.Т3-2: Ду[mm], from elev. [+X.XXX] to elev. [+X.XXX], at axes [X-Y]
[list ALL risers with labeling, diameters, location]

FLOOR BRANCHES:
- Floor 1 (elev. +X.XXX): from Ст.Т3-1 → Ду[mm] → [fixtures: sink, bathtub, ...]
- Floor 2 (elev. +X.XXX): from Ст.Т3-1 → Ду[mm] → [fixtures]
[for each floor: riser, branch, diameter, fixtures]

VALVES:
- Ball valve Ду[mm] — [location, quantity]
- Check valve Ду[mm] — [location]
- Pressure regulator Ду[mm] — [location]
- Filter Ду[mm] — [location]
- Towel warmer — [riser, floor]
[list all visible valves]

INSULATION:
- Insulated pipelines: [which sections, thickness if indicated]
- Without insulation: [which sections]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: PIPELINE PLAN

If the image is a floor plan with pipe layout:

```
PIPELINE PLAN: [title, e.g. "План 1-го этажа. Водоснабжение и канализация"]
SCALE: М1:100 (if indicated)
SYSTEMS ON PLAN: B1 / Т3 / Т4 / К1 / К2 (which systems are shown)

AXES:
- Longitudinal: А, Б, В, Г (spacing [mm])
- Transverse: 1, 2, 3, 4, 5 (spacing [mm])

RISERS ON PLAN:
- Ст.В1-1: at axes [X-Y], Ду[mm]
- Ст.К1-1: at axes [X-Y], Ду[mm]
[list all risers with axis references]

HORIZONTAL PIPELINES:
- B1: from Ст.В1-1 to [fixture/room], Ду[mm], length ~[m]
- Т3: from Ст.Т3-1 to [fixture/room], Ду[mm]
- К1: from [fixture] to Ст.К1-1, Ду[mm], slope i=[value]
[for each system: routing, diameters]

SANITARY FIXTURES:
- Room [number] ([purpose]): [list of fixtures — bathtub, wash basin, toilet, kitchen sink, ...]
[for each room]

WATER DRAW-OFF POINTS:
- Watering tap: at axes [X-Y]
- Fire hydrant: at axes [X-Y], Ду[mm]
[if any]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: SEWERAGE / RISER DIAGRAM

If the image is an axonometric or development view of sewerage risers:

```
SEWERAGE DIAGRAM: [title, e.g. "Схема стояка К1-1"]
SYSTEM: К1 / К2
TYPE: riser development / axonometric / outlet diagram

RISERS:
- К1-1: Ду[mm], from elev. [+X.XXX] to elev. [+X.XXX], at axes [X-Y]
  - Vent stack: Ду[mm], extends [mm] above roof
  - Connections:
    - Floor 1 (elev. +X.XXX): [fixtures], Ду[mm], tee/cross [angle°]
    - Floor 2 (elev. +X.XXX): [fixtures], Ду[mm], tee/cross [angle°]
  - Inspection openings: on floors [N, N, ...]
  - Cleanouts: on floors [N, N, ...]

OUTLETS:
- Outlet #1: from Ст.К1-1, Ду[mm], slope i=[value], length [m]
- Outlet #2: from Ст.К1-2, Ду[mm], slope i=[value], length [m]
[list all outlets]

HORIZONTAL SECTIONS:
- Basement/technical subfloor: from [riser] to [outlet/manhole], Ду[mm], slope i=[value]
[routing in basement/technical subfloor]

FITTINGS:
- Tees: [type, angle, quantity]
- Elbows: [angle, quantity]
- Crosses: [type, quantity]
[list visible fittings]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: PUMP STATION PLAN

If the image is a pump room layout:

```
PUMP STATION PLAN: [title, e.g. "План насосной станции хоз-питьевого водоснабжения"]
SCALE: М1:50 / М1:100

ROOM:
- Dimensions: [LxWxH] mm
- Floor elevation: +[X.XXX]
- Location: at axes [X-Y]

PUMPS:
- Pump 1 (duty): [make/type], Q=[l/s], H=[m], N=[kW]
- Pump 2 (standby): [make/type], Q=[l/s], H=[m], N=[kW]
- Pump 3 (fire): [make/type], Q=[l/s], H=[m], N=[kW]
[list all pumps with characteristics]

STORAGE TANK / MEMBRANE TANK:
- Type: [hydropneumatic / membrane / open]
- Volume: [m3]
- Pressure: [MPa]
- Quantity: [pcs]

PIPING:
- Suction manifold: Ду[mm], material
- Discharge manifold: Ду[mm], material
- Shut-off valves: [types, diameters, quantities]
- Check valves: [location, Ду]
- Pressure gauges / pressure sensors: [location]

DRAINAGE:
- Floor drain: Ду[mm]
- Drainage sump: [dimensions]
- Drainage pump: [if present, characteristics]

AUTOMATION:
- Control panel: [location]
- Sensors: [pressure, level, flow]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: CONNECTION NODE

If the image is a water meter node, inlet node, or connection to networks:

```
NODE: [title, e.g. "Водомерный узел В1"]
NODE TYPE: water meter node / inlet node / manhole / external network connection

NODE COMPOSITION:
- Pipeline: Ду[mm], material
- Water meter: [type, make], Ду[mm], Qnom=[m3/h]
- Filter: [type — mesh, magnetic], Ду[mm]
- Gate valve / ball valve: [type], Ду[mm], quantity [pcs]
- Check valve: Ду[mm]
- Bypass line: [present/absent], Ду[mm]
- Pressure gauges: [quantity, location]
- Drain cock: Ду[mm]

DIAGRAM (element order in flow direction):
Inlet → gate valve → filter → water meter → check valve → gate valve → main

DIMENSIONS:
- Node length: [mm]
- Pipeline axis height: [mm] from floor
- Sleeve diameter (if through wall): Ду[mm]
- Penetration seal: [type]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: SPECIFICATION ON DRAWING

If the image is a specification table on a drawing sheet:

```
SPECIFICATION: [title, e.g. "Спецификация оборудования и материалов системы В1"]
SYSTEM: B1 / Т3 / Т4 / К1 / К2 / general

CONTENT:
[reproduce the table in text format, preserving structure]

| Item | Description | Make/Type | Ду/Size | Unit | Qty | Note |
|------|-------------|-----------|---------|------|-----|------|
| 1    | Труба PPR PN20 | PPRC | Ду25 | l.m. | 120 | B1 |
| 2    | Труба PPR PN20 | PPRC | Ду32 | l.m. | 45  | B1 |
| 3    | Кран шаровый | ... | Ду25 | pcs | 24  | ... |
[all table rows]

TOTALS (if present):
- Total pipe length by systems: [values]
- Total valve quantity: [values]

NOTES:
[text notes to specification]
```

## Rules

1. **Main rule:** for each element, specify SPECIFIC numerical parameters — diameter, length, slope, make, flow rate. Do not limit yourself to "pipeline" — write "трубопровод PPR PN20 Ду32, length ~3.5 m".

2. **If multiple systems are on the drawing** (B1+К1 on one plan) — describe each system separately.

3. **If a parameter is not legible** on the image — write "не читается" instead of guessing.

4. **Description order:** for axonometric views — bottom to top (from inlet to upper floors). For plans — along axes left to right. For risers — top to bottom.

5. **Two scales:** if there is a main drawing and enlarged detail views on the same sheet — describe both.

6. **Element labeling:** if the drawing has riser labels (Ст.В1-1, Ст.К1-3), pipe labels (B1, Т3, К1), valve labels — always include them, as they are the key for linking to other drawings.

7. **Flow direction:** for water supply — from inlet to fixtures. For sewerage — from fixtures to outlet. Indicate arrows if visible on the drawing.

## Typical description errors (what to avoid)

- "The plan shows pipe routing with connections to fixtures" — General description, no specifics
- "Sewerage is made of plastic pipes" — Type not specified (ПП/ПВХ), no diameter, no slope
- "Pump station with two pumps" — Characteristics Q, H, N not specified, no type

+ "Ст.В1-1: Ду32 PPR PN20, from elev. -1.200 to +9.600, at axes А-3. Branch on floor 2: Ду25 → wash basin + bathtub. Ball valve Ду32 on each floor" — All elements are specific, can be verified
