# Instructions for vision model: structured description of technological drawings

You receive a PNG image from the TX (technological solutions) section of design documentation. Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from the description without viewing the image.

## Scope and limitations

**5 types of technological drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|-----------|
| Parking garage plan / Fragment | 25% | Underground parking plans: markings, signs, parking spaces, driveways, ramps, TX equipment, slopes |
| Elevator shaft plan / Section | 20% | Vertical sections: shaft, cabin, counterweight, machine room, pit |
| Waste removal plan | 20% | Waste collection room plans, hoist location, containers, removal route, shaft section |
| Common area plan | 15% | Pavilion plans, security rooms, parking service rooms, utility rooms |
| Specification in drawing | 20% | Tables on sheets: elevator equipment specifications, parking specifications, waste removal specifications, load tables, room schedules |

**What NOT to describe (this data already exists in document.md):**
- Title blocks, main inscriptions (sheet number, project code, organization)
- Revision tables
- Sheet numbers and their titles
- Drawing registers

**For each image type,** identify the type and apply the corresponding description format below.

## Description format: PARKING GARAGE PLAN

If the image is an underground parking garage plan, plan fragment, or layout:

```
PARKING GARAGE PLAN: [title, e.g. "Parking garage plan at elev. -3.600"]
SCALE: 1:200 (if indicated)
TYPE: underground / above-ground / mechanized

GRID AXES:
- Longitudinal: А, Б, В, Г (spacing [mm])
- Transverse: 1, 2, 3, ... (spacing [mm])

PARKING SPACES:
- Total quantity: [N]
- Standard: [N] pcs., size [W x L] mm (e.g. 2500 x 5300)
- For persons with disabilities (МГН): [N] pcs., size [W x L] mm (e.g. 3500 x 5300)
- For electric vehicles (ЭМ): [N] pcs., size [W x L] mm (if present)
- Enlarged: [N] pcs., size [W x L] mm (if present)
[parking space numbering: from No.... to No....]

DRIVEWAYS:
- Main driveway: width [mm], direction
- Side driveways: width [mm]
- Turning radii: [mm] (inner / outer)

RAMP:
- Width: [mm]
- Slope: [%]
- Length: [mm]
- Type: straight / curved / two-lane
- Surface: [type]
- Counter-slope: [mm] (if present)

SIGNS AND MARKINGS:
- Road signs: [list with ГОСТ numbers and locations]
- Horizontal markings: [type — arrows, pedestrian crossings, lines]
- Traffic direction: one-way / two-way
- Convex mirrors: [quantity, location]
- Wheel stops: [presence, material, location]

HEIGHTS:
- Clear height to protruding structures: [mm]
- Height to bottom of beams/girders: [mm]
- Height to bottom of utility networks: [mm]

VENTILATION:
- Supply openings: [location]
- Exhaust openings: [location]
- CO sensors: [quantity, location]
- Smoke exhaust: [presence, location]

FIRE SAFETY:
- Fire barriers/gates: [quantity, size, EI]
- Sprinklers: [presence]
- Fire hydrants/hose reels: [location]
- Emergency exits: [quantity, width, location]

UTILITY SYSTEMS:
- Drainage: floor drains, channels, floor slopes
- Lighting: [type, location]

ELEVATIONS:
- Floor level: [+/-X.XXX]
- Floor slopes: [%], direction toward drains

NOTES ON DRAWING:
[list all text notes]
```

## Description format: ELEVATOR SHAFT PLAN / SECTION

If the image is an elevator shaft section, shaft plan, pit, or machine room:

```
ELEVATOR SHAFT PLAN / SECTION: [title, e.g. "Section 1-1. Elevator Л-1, capacity 630 kg" or "Shaft plan at elev. +49.950"]
SCALE: 1:50 / 1:100 (if indicated)

ELEVATOR:
- Brand/manufacturer: [if indicated]
- Load capacity: [kg]
- Speed: [m/s]
- Number of stops: [N]
- Purpose: passenger / freight-passenger / firefighter / for persons with disabilities

CABIN:
- Width: [mm]
- Depth: [mm]
- Height: [mm]
- Cabin door: [W x H] mm, type (telescopic / center-opening)

SHAFT:
- Width: [mm]
- Depth: [mm]
- Walls: [material, thickness]
- Fire resistance: REI [value]

PIT:
- Depth: [mm]
- Buffers: [type]
- Drainage: [presence]

MACHINE ROOM:
- Location: top / bottom / machine-room-less
- Dimensions: [L x W x H] mm
- Ventilation: [presence, type]
- Lifting device: monorail [capacity kg] (if present)

COUNTERWEIGHT:
- Location: side / rear
- Clearances to walls: [mm]

LANDING DOORS:
- Size: [W x H] mm
- Fire resistance: EI [value]
- Type: automatic sliding

FLOOR STOPS:
- Elevations: [list all, e.g. -3.600, ±0.000, +3.300, ...]
- Leveling accuracy: [mm]

OVERHEAD CLEARANCE:
- Above cabin (top floor to ceiling): [mm]
- Below cabin (pit): [mm]

DISPATCHING:
- Communication type: [intercom, talk-back device]
- Connection to dispatch center: [presence]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: WASTE REMOVAL PLAN

If the image is a waste collection room plan or waste removal layout:

```
WASTE REMOVAL PLAN: [title, e.g. "Waste collection room plan at elev. -3.600"]
SCALE: 1:50 / 1:100 (if indicated)

WASTE COLLECTION ROOM:
- Location: [floor, elevation, grid axis reference]
- Plan dimensions: [L x W] mm
- Height: [mm]
- Walls: [material, thickness]
- Floor: [finish, slope to drain]
- Door: size [W x H], type, EI (if indicated)
- External access: [presence, opening size for removal]
- Premises category: [by fire load]

WASTE HOIST / HOIST:
- Load capacity: [kg]
- Lifting height: [m]
- Platform size: [L x W] mm
- Drive: [electric / hydraulic]
- Shaft: dimensions [L x W] mm

CONTAINERS:
- Type: [euro container / bin / compactor container]
- Volume: [liters / m3]
- Quantity: [N] (solid waste - ТБО), [N] (bulky waste - КГМ), [N] (separate collection)
- Location: [grid axis reference]
- Accumulation zone: [area m2]

VENTILATION:
- Supply: [presence, capacity]
- Exhaust: [presence, capacity, air change rate]

WATER SUPPLY AND DRAINAGE:
- Wash-down tap: [presence, DN]
- Floor drain: [presence, DN]
- Sewer connection: [presence]

REMOVAL ROUTE:
- Container route: [from room to garbage truck loading point]
- Driveway width: [mm]
- Garbage truck turning area: [dimensions]
- Ramp: [slope %, width mm]

DISINFECTION:
- Method: [washing, treatment]
- Frequency: [if indicated]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: COMMON AREA PLAN

If the image is a plan of pavilions, security rooms, or parking service rooms:

```
PREMISES PLAN: [title, e.g. "1st floor premises plan. Pavilion No. 1"]
SCALE: 1:100 (if indicated)

GRID AXES:
- Longitudinal: [list, spacing]
- Transverse: [list, spacing]

PREMISES (room schedule):
- Room [number] — [purpose], S=[area] m2, h=[height] m
[list ALL premises]

FUNCTIONAL PURPOSE:
- Security pavilion: [room number, area]
- Parking service: [room number, area]
- Utility rooms: [list]
- Restrooms: [list]
- Storage rooms: [list]

EQUIPMENT:
- Security post: [location, equipment — monitor, control panel, barrier]
- Parking meter: [quantity, location]
- Barrier: [quantity, location]
- Video surveillance: [cameras — quantity, location]
- Intercom/talk-back devices: [quantity]
- Utility connection points: [presence of water supply, 220V outlets, RJ-45 ports at specific equipment positions]

ENTRANCES:
- Doors: [type, size W x H, EI if indicated]
- Vestibules: [presence, dimensions]
- Accessibility for persons with disabilities (МГН): [presence, ramp/lift]

ELEVATIONS:
- Floor level: [+/-X.XXX]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: SPECIFICATION IN DRAWING

If the image is any table on a drawing sheet (equipment specification, load table, room schedule).
IMPORTANT: Do not try to squeeze data into the template below! Always strictly preserve the original number and names of columns from the drawing.

```
TABLE / SPECIFICATION: [title, e.g. "Elevator equipment specification" or "Pit floor loads"]

CONTENTS:
CONTENTS:
[reproduce the table in Markdown text format, strictly preserving the original structure, number of columns, and their names]

| [Original column 1] | [Original column 2] | [And so on...] |
|---------------------|---------------------|----------------|
| [Data]              | [Data]              | [Data]         |
[all table rows]

NOTES:
[text notes below the table or callouts to it]
```

## Rules

1. **Main rule:** for each element, specify CONCRETE numerical parameters — load capacity, size, quantity, slope. Do not limit yourself to "passenger elevator" — write "passenger elevator 630 kg, 1.0 m/s, cabin 1100x1400x2100 mm".

2. **Multiple plans/fragments:** If one sheet contains several different plan fragments or zones with different solutions (e.g., "Fragment plan 1", "Fragment plan 2") — describe each fragment under a separate subheading, duplicating the structure of axes, equipment, and dimensions for each.

3. **STRICTLY PROHIBITED TO GUESS:** If a parameter, marking, ГОСТ number, or dimension is unreadable due to image quality or is cropped — strictly write "[unreadable]". Do not fabricate data.

4. **Description order:** for plans — by axes left to right, top to bottom. For sections — top to bottom.

5. **Two scales:** if one sheet has a main drawing and enlarged detail nodes — describe both.

6. **Element markings:** if the drawing has markings (Л-1, М.М. №15, ПМ-1) — always include them, as they are the key for linking with other drawings.

7. **Format flexibility (important):** The formats proposed above are a basic framework. If the drawing contains important elements, sections, local mounting details, or non-standard callouts not described in the template, independently add new logical blocks (e.g., `SECTION 1-1:`, `DETAIL A:`, or `MIRROR MOUNTING SCHEME:`), maintaining the general style of structured text.

8. **Tables without headers:** If a table is a continuation from another sheet and has no header, reconstruct the column logic from the content, but be sure to indicate this in a note below the table.

## Typical description errors (what to avoid)

- "The plan shows an underground parking garage with parking spaces" — Generic description, no specifics
- "The elevator is installed in a shaft" — No shaft dimensions, cabin size, or load capacity specified
- "The waste collection room is located on the -1 floor" — No dimensions, equipment, or ventilation specified

- "Spaces No. 1-40 standard 2500x5300 mm, No. 41-42 for persons with disabilities 3500x5300. Driveway 6000 mm. Ramp i=15%, w. 3500 mm. Signs: 5.15.1, 3.24 '5 km/h'. Clear height 2200 mm" — All elements are specific, verifiable
