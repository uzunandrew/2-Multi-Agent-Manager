# Instructions for Vision Model: Structured Description of POS Drawings

You receive a PNG image from the POS (construction management plan) section of design documentation. Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from the description without viewing the image.

## Scope and Limitations

**6 types of POS drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|------------|
| Site construction plans (SGP) | 35% | Construction site plan showing crane positions, temporary roads, storage, fencing, temporary buildings |
| Calendar schedules | 15% | Gantt chart or network diagram with construction stages, durations, resource allocation |
| Transport movement diagrams | 15% | Vehicle movement paths on and around the construction site, entry/exit points, traffic signs |
| Utility composite plans | 15% | Engineering networks layout (water, sewer, gas, heat, power, telecom) with separations |
| Demolition/protection plans | 10% | Technology card for demolition of existing structures, stages, equipment |
| Tables/specifications | 10% | Work volumes, material requirements, temporary building lists, equipment lists |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, project code, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.

## Description Format: SITE LAYOUT PLAN (SGP)

```
SGP: [name, e.g. "Construction site layout plan for the main period, stage 3 — superstructure"]
SCALE: M1:500 (if indicated)
STAGE: preparatory / main period stage N / finishing / landscaping

BUILDING OUTLINE:
- Building footprint: axes A-E / 1-12 (or dimensions LxW)
- Number of floors: ___
- Building height: ___ m (if indicated)
- Zero elevation mark: +___ m

CRANES:
- Crane 1: type ___ (tower/self-propelled), model ___
  - Location: at axis __ / coordinates ___
  - Boom reach: ___ m
  - Load capacity at max reach: ___ t
  - Hook height: ___ m
  - Rail track length: ___ m (for tower cranes)
  - Hazard zone radius: ___ m
  - Hazard zone boundary shown: yes/no
- Crane 2: [similarly]
[all cranes on the plan]

TEMPORARY ROADS:
- Road 1: from entry gate to unloading area
  - Width: ___ m (single-lane / double-lane)
  - Surface: reinforced concrete slabs / crushed stone / asphalt
  - Turning radius: ___ m (at curves)
  - Length: ~___ m
- Road 2: ring road around building
  - [similarly]
- Entry gates: ___ pcs, locations ___
- Exit gates: ___ pcs, locations ___
- Wash station: yes/no, location ___

FENCING:
- Perimeter length: ~___ m
- Height: ___ m (if indicated)
- Type: panel / mesh / solid
- Gates: ___ pcs, width ___ m
- Pedestrian passages: ___ pcs, with canopy: yes/no

TEMPORARY BUILDINGS:
- Office / dispatch: ___ pcs, location ___
- Worker shelters: ___ pcs, ___ persons capacity
- Canteen: ___ pcs, ___ seats
- Toilet: ___ pcs, type ___
- Dressing room: ___ pcs
- Security booth: ___ pcs, at entrance ___
- Storage (heated): ___ pcs, area ___ m2
- Storage (open): ___ pcs, area ___ m2
[all temporary structures with location reference]

STORAGE AREAS:
- Reinforcement storage: area ___ m2, location ___
- Formwork storage: area ___ m2, location ___
- Prefabricated elements: area ___ m2, location ___
- Aggregates (sand, gravel): area ___ m2, location ___
[all marked storage areas]

TEMPORARY UTILITIES:
- Power supply: transformer ___ kVA, location ___
- Distribution boards: ___ pcs, locations ___
- Water supply: connection point ___, temporary pipe route ___
- Fire water supply: hydrants ___ pcs, locations ___
- Temporary sewage: type ___, location ___
- Temporary lighting: poles ___ pcs

HAZARD ZONES:
- Crane hazard zone: radius ___ m from crane axis
- Building drop zone: ___ m from building facade
- Exclusion areas: locations, dimensions
- Overlap between crane zone and public area: yes/no
[all hazard zones with dimensions]

EXISTING STRUCTURES:
- Adjacent buildings: ___ pcs, distance from construction ___
- Existing roads: ___
- Existing utilities crossing site: ___
- Trees/green areas to preserve: ___
```

## Description Format: CALENDAR PLAN / SCHEDULE

```
CALENDAR PLAN: [name, e.g. "Calendar plan for construction of residential building"]
FORMAT: Gantt chart / network diagram / table

OVERALL DURATION: ___ months (from ___ to ___)
START DATE: ___ (if indicated)
END DATE: ___ (if indicated)

STAGES AND WORKS:
Stage 1 — Preparatory period:
  - Duration: ___ months (month __ to month __)
  - Works:
    1. Site clearing and grading: ___ days/months
    2. Temporary fencing installation: ___ days
    3. Temporary roads: ___ days
    4. Temporary utilities: ___ days
    5. Demolition of existing structures: ___ days (if applicable)
  - Workers: ___ persons (peak)
  - Machines: ___

Stage 2 — Underground works:
  - Duration: ___ months (month __ to month __)
  - Works:
    1. Excavation (pit): ___ days, volume ___ m3
    2. Pile driving / drilling: ___ days, ___ piles
    3. Foundation slab / strip foundation: ___ days, concrete ___ m3
    4. Basement walls: ___ days
    5. Waterproofing: ___ days
    6. Backfill: ___ days
  - Workers: ___ persons
  - Cranes: ___
  - Concrete pumps: ___

Stage 3 — Superstructure:
  - Duration: ___ months
  - Works:
    1. Monolithic frame floor-by-floor: ___ floors, ___ days per floor
    2. Masonry / enclosing walls: ___ days
    3. Internal partitions: ___ days
  - Workers: ___ persons
  - Tower crane: ___

Stage 4 — Roof:
  - Duration: ___ months
  - Works: [list]

Stage 5 — Finishing:
  - Duration: ___ months
  - Works: [list]

Stage 6 — MEP systems:
  - Duration: ___ months (concurrent with finishing)
  - Works: [list]

Stage 7 — Landscaping:
  - Duration: ___ months
  - Works: [list]

CRITICAL PATH: [if identifiable — list of works on the critical path]

RESOURCE GRAPH (if present):
- Maximum workers: ___ persons in month ___
- Average workers: ___ persons
- Graph shape: flat / peak / bell curve
```

## Description Format: TRANSPORT ROUTE SCHEME

```
TRANSPORT SCHEME: [name, e.g. "Vehicle movement scheme during main construction period"]
SCALE: M1:___ (if indicated)

ENTRY/EXIT POINTS:
- Entry 1: from street ___, direction ___, gate width ___ m
- Entry 2: [if multiple]
- Exit 1: to street ___, direction ___

ON-SITE ROUTES:
- Route 1: entry → unloading zone (crane 1) → exit
  - Direction: one-way / two-way
  - Width: ___ m
  - Speed limit: ___ km/h (if indicated)
  - Surface: ___
- Route 2: entry → concrete pump area → exit
  - [similarly]

UNLOADING ZONES:
- Zone 1: near crane 1, area ___ x ___ m
- Zone 2: concrete pump location
[all zones]

TRAFFIC SIGNS:
- Speed limit signs: ___ pcs, value ___ km/h
- Direction signs: ___ pcs
- Stop signs: ___ pcs
[all signs if visible]

PUBLIC ROAD INTERACTION:
- Temporary traffic restrictions: ___
- Flagmen positions: ___ pcs
- Pedestrian diversions: ___
- Public sidewalk closure: yes/no, alternative route ___
```

## Description Format: CONSOLIDATED UTILITY PLAN

```
UTILITY PLAN: [name, e.g. "Consolidated plan of engineering networks M1:500"]
SCALE: M1:___ (if indicated)

EXISTING UTILITIES:
- Water supply: Ду___, material ___, depth ___ m, from ___ to ___
- Sewage (gravity): Ду___, material ___, slope ___%, depth ___
- Sewage (pressure): Ду___, material ___
- Gas supply: Ду___, pressure ___ (low/medium/high), material ___
- Heat supply: 2xДу___, insulation type ___, depth ___
- Power cable: voltage ___ kV, cable type ___, depth ___
- Telecom: cable/fiber, duct bank ___ channels
- Storm drain: Ду___, material ___
[for each utility: designation, diameter, material, depth, route description]

DESIGNED UTILITIES:
[same format as existing, clearly separate]

CROSSINGS:
- Crossing 1: water Ду150 x sewer Ду200
  - Angle: ___°
  - Vertical clearance: ___ m (water above/below sewer)
  - Horizontal separation: ___ m
  - Casing pipe: yes/no, type ___
- Crossing 2: gas Ду100 x heat 2xДу100
  - [similarly]
[all crossings between utilities]

PARALLEL RUNS (minimum separations):
- Water ↔ sewer: ___ m (measured / shown)
- Gas ↔ water: ___ m
- Power cable ↔ heat pipe: ___ m
- Gas ↔ building: ___ m
[all parallel separations visible on plan]

MANHOLES AND CHAMBERS:
- Water manholes: ___ pcs, designations ___
- Sewer manholes: ___ pcs, designations ___
- Heat chambers: ___ pcs, designations ___
- Cable manholes: ___ pcs
[all manholes with designations]

PROTECTIVE ZONES:
- Gas pipeline zone: ___ m on each side
- Heat pipeline zone: ___ m on each side
- Power cable zone: ___ m on each side
[all marked zones]

CONNECTION POINTS:
- Water: connection to existing main at manhole ___
- Sewer: connection at manhole ___
- Gas: connection at ___
- Heat: connection at ___
- Power: connection at ___
[all connection points to existing infrastructure]
```

## Description Format: DEMOLITION / DISMANTLING PLAN

```
DEMOLITION PLAN: [name, e.g. "Demolition technology card for building at address ___"]

STRUCTURE TO DEMOLISH:
- Type: residential / industrial / auxiliary / retaining wall
- Dimensions: ___ x ___ m, height ___ m
- Floors: ___
- Structural system: brick / reinforced concrete / steel frame / mixed
- Foundation type: strip / slab / piles
- Estimated volume: ___ m3
- Estimated demolition waste: ___ t

DEMOLITION METHOD:
- Method: mechanical (excavator with hydraulic shears) / manual / explosive / combined
- Equipment: ___ (excavator model, attachment type)
- Direction of demolition: from top to bottom / section by section
- Sequence: [numbered steps]

DEMOLITION STAGES:
Stage 1: ___
  - Duration: ___ days
  - Equipment: ___
Stage 2: ___
  [all stages]

SAFETY ZONES:
- Exclusion zone: ___ m from structure
- Dust suppression: method ___
- Vibration monitoring: yes/no

WASTE MANAGEMENT:
- Sorting on site: yes/no
- Temporary storage: area ___ m2
- Disposal: ___ m3 to landfill ___, ___ m3 recyclable
- Truck trips: ___ per day
```

## Description Format: TABLE / SPECIFICATION

```
TABLE: [name, e.g. "Work volumes summary" / "Temporary buildings and structures list"]

TYPE: work volumes / material requirements / temporary buildings / equipment list / 
     earth balance / concrete volumes / pile schedule

CONTENT:
[reproduce the table in text format, preserving structure]

| Column 1 | Column 2 | Column 3 | Column 4 |
|----------|----------|----------|----------|
| value | value | value | value |
[all rows]

TOTALS (if present):
- Total earthwork: ___ m3
- Total concrete: ___ m3
- Total reinforcement: ___ t
[summary values]
```

## Complete reading failure

If the image is entirely unreadable (rotation, low resolution, scanning artifacts, severe cropping), output ONLY:

`READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts / severe cropping]`

Do not attempt to describe or guess content from an unreadable image.

## Rules

1. **Main rule:** for each element on the SGP, reference it to the building axes or plan coordinates. Do not describe elements without spatial reference.

2. **Dimensions are critical:** always capture dimensions in meters — road widths, crane reach, hazard zone radii, storage areas, separation distances.

3. **Stages matter:** always identify which construction stage the SGP corresponds to. Different stages have different layouts.

4. **If a parameter is not readable** on the image — write `[unreadable]` instead of guessing.

5. **Quantities:** count all temporary buildings, gates, hydrants, cranes on the drawing.

6. **Hazard zones:** specifically look for crane hazard zone boundaries, building drop zones, and any overlaps with public areas or adjacent properties.

7. **Utility separations:** on the consolidated plan, record horizontal separations between parallel utilities only if explicitly dimensioned. Do not measure distances from the image unless explicitly dimensioned. Scale-based estimation is low-confidence and must be marked as approximate.

## Typical Description Errors (what to avoid)

**Bad:** "The SGP shows the building, a crane, and temporary roads around the site."
--> No dimensions, no hazard zones, no specifics

**Bad:** "Calendar plan with several stages of work spanning 24 months."
--> No stage details, no durations, no resource data

**Good:** "SGP main period stage 3 (superstructure). Tower crane Liebherr 132EC-H8 at axis E/6, boom reach 55m, hazard zone 62m radius. Temporary road width 6m (double-lane), ж/б slabs ПДН, ring layout, turning radius 12m at NE corner. 4 worker shelters (120 persons), canteen 60 seats at SE corner, 30m from building. Fire hydrant at entry gate, 15m from road."
--> All key parameters with spatial reference

## Accuracy standards

1. **Describe only technically significant content.** Do not describe visual style, shadows, decorative graphics, line thickness, line/contour colors unless they carry engineering meaning. Exceptions: color coding per legend (e.g., red lines for fire systems, NCS/RAL codes).

2. **Do not guess.** If a parameter, mark, dimension, node number, designation, sheet reference, or fragment is read with uncertainty — write `[unreadable]`.

3. **Complete reading failure.** If the entire image is unreadable, output only: `READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts / severe cropping]`

4. **Preserve designations and units exactly as on the drawing.** Do not normalize or paraphrase marks, positions, DN/Ду, Ø, EI/REI, IP, kW, kVA, A, kA, cosφ, m², m³, l/s, Pa, °C and other designations.

5. **If one image contains multiple entities** (plan + detail + table + notes), describe them under separate subheadings, do not mix into one block.

6. **Do not measure dimensions from the image if they are not explicitly labeled.** Scale-based estimation is allowed only as low-confidence and must be explicitly marked as approximate.

7. **At the end of every description, add mandatory blocks:**

```
EXACT LABELS AND MARKINGS:
- [list all clearly readable labels, marks, positions, designations]

UNREADABLE / AMBIGUOUS FRAGMENTS:
- [list fragments where data is partially readable or uncertain]

CROSS-REFERENCES TO NODES / SHEETS / FRAGMENTS:
- [list all references like "See node 1", "See sheet 5", "Detail A" etc.]
```
