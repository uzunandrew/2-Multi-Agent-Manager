# Instructions for Vision Model: Structured Description of Architectural Drawings

You receive a PNG image from the AR (architectural solutions) section of project documentation. Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from your description without viewing the image.
Your task is to perform a deep technical analysis of the PNG image from the AR section and create its "digital twin" in text form.
Your description must be precise enough that another architect could fully read the drawing without seeing the original.

## Scope and Limitations

**7 types of architectural drawings (identify the type and apply the corresponding format):**

| Type | Share | Description |
|------|-------|-------------|
| Marking plan | 20% | Floor plans with room markings, zones, room schedules, axis references |
| Masonry plan | 20% | Wall layout in aerated concrete, brick; thicknesses, references, elevations |
| Wall/roof section | 15% | Vertical sections: layered wall, roof, floor slab compositions |
| Junction detail | 15% | Details: roof-to-parapet junction, wall-to-slab, window reveals |
| Roof plan | 10% | Slopes, drainage funnels, parapets, slope formation, roof access |
| Staircase detail | 10% | Stair flights, railings, anchors, balusters, handrails |
| Specification in drawing | 10% | Tables on sheets: door, lintel, masonry element specifications |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, project code, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.
**If a sheet contains multiple types simultaneously -- describe each in its own block.**

## Description Format: MARKING PLAN


If the image is a floor plan with room markings:

```
MARKING PLAN: [name, e.g. "Plan of 1st floor in axes А-Д/1-8"]
SCALE: М1:100 (if indicated)
TYPE: underground part / above-ground part / typical floor

AXES:
- Longitudinal: А, Б, В, Г, Д (spacing [mm])
- Transverse: 1, 2, 3, 4, 5, 6, 7, 8 (spacing [mm])

ROOMS (room schedule):
- Room 1.01 -- Vestibule, S=3.2 m², h=2.7 m
- Room 1.02 -- Corridor, S=12.5 m², h=2.7 m
- Room 1.03 -- Technical room, S=8.1 m², h=2.7 m
[list ALL rooms with numbers, purpose, area]

WALLS AND PARTITIONS:
- Exterior wall: thickness [mm], material (газобетон D500/D600, brick)
- Interior load-bearing: thickness [mm], material
- Partitions: thickness [mm], material
- Finish type: [code from finish schedule, e.g. "Т1"]
- Wall fire resistance: [REI -- if indicated]
[specify axis references]

ENGINEERING ELEMENTS AND EQUIPMENT:
- Ventilation shafts/Ducts: [marking, cross-section, wall material]
- Sanitary fixtures: [presence and location of toilets, sinks, floor drains]
- Vertical transport: [stairs, elevators, lifts]
- Fire hose cabinets (ШП): [quantity, location]

ADDITIONAL DESIGNATIONS:
- Floor slopes: [direction, % -- in wet zones]
- Level changes: [steps, ramps, thresholds]

OPENINGS:
- Door Д1 -- at axes А-Б/3, size [WxH], type (ДГ/ДП/ДО/ПП), EI if indicated
- Window ОК1 -- at axes Б-В/5, size [WxH]
[list all openings with markings]

ELEVATIONS:
- Finished floor level: +[X.XXX]
- Room height: [mm]
```

## Description Format: MASONRY PLAN

If the image is a plan with masonry layout:

```
MASONRY PLAN: [name, e.g. "Masonry plan of 2nd floor"]
SCALE: М1:100 (if indicated)

MASONRY MATERIALS:
- Exterior walls: газобетон D[500/600] B[2.5/3.5/5.0], thickness [mm]
- Interior walls: газобетон D[500/600], thickness [mm]
- Partitions: газобетон D[500/600], thickness [mm]
- Brick sections: [where, purpose -- opening frames, ventilation channels]

LAYOUT BY AXES:
- Axis А, from axis 1 to axis 4, elev. +3.300: wall 300mm, газобетон D600, length [mm], reference to axis [mm]
- Axis Б, from axis 2 to axis 3, elev. +3.300: wall 200mm, газобетон D500, length [mm], reference to axis [mm]
[for each wall: axis, from which axis to which, thickness, material, length, axis reference]

REINFORCEMENT:
- Basalt mesh: spacing every [N] courses (typically 2)
- Mesh type: [cell size, width]
- U-shaped blocks: [where, purpose -- армопояс, lintels]
- Rebar in grooves: [diameter, class, location]

LINTELS:
- ПР-1: angle L100x100x8 + plate 200x20, opening [WxH], bearing [mm] on each side
- ПР-2: U-shaped block with reinforcement, opening [WxH], bearing [mm]
[list all lintels with markings]

FRAME ATTACHMENT:
- Column connection: [method -- anchors, embedded items, flexible ties]
- Gap between masonry and frame: [mm]
- Deformation joints: [location, width]

WATERPROOFING:
- In wet rooms: coating waterproofing to height [mm] (typically 300 mm)
- Base course: roll/coating type, elev. [+X.XXX]

NOTES ON DRAWING:
[list all text notes]
```

## Description Format: WALL/ROOF SECTION

If the image is a vertical section with layered composition:

```
SECTION: [number and name, e.g. "Section 1-1. Exterior wall cross-section"]
SCALE: М1:20 / М1:50 (if indicated)

LAYER COMPOSITION (outside to inside or top to bottom):
Layer 1: [material], thickness [mm], density/grade
Layer 2: [material], thickness [mm]
Layer 3: [material], thickness [mm]
...
[for each layer: material, thickness, properties]

WALL EXAMPLE:
1. Facing layer: [material: brick/porcelain stoneware/panels], thickness [mm], [color/grade]
2. Air gap: [mm] (if present)
3. Thermal insulation: [brand, e.g. Технониколь], thickness [mm], density [kg/m3], lambda [W/mK]
4. Structural layer: газобетон D[500/600], thickness [mm]
5. Interior finish: plaster [mm]
6. Wind-moisture barrier: [membrane brand, e.g. Tyvek, Изоспан], seam taping present
7. Vapor barrier: [brand] (mandatory for frame walls or interior insulation)
8. Substructure / Fixings: [type: rails, brackets, clips], material [aluminum/steel], spacing [mm]

ROOF EXAMPLE:
1. Waterproofing: Технониколь ЭПП [grade], [N] layers, thickness [mm]
2. Screed: cement-sand mortar, thickness [mm]
3. Slope formation: expanded clay / tapered insulation, thickness min-max [mm]
4. Insulation: mineral wool / XPS, lambda=[value], thickness [mm]
5. Vapor barrier: [brand], thickness [mm]
6. Base: reinforced concrete slab, thickness [mm]
7. Waterproofing membrane: [type: PVC membrane / bitumen-polymer (ЭПП, ТКП)], brand, number of layers, fixing method [torch-applied/mechanical/adhesive]
8. Structural base: [RC slab / profiled sheeting (grade, e.g. Н75)], thickness [mm]

KEY POINTS:
- Parapet: height [mm], capping (galvanized steel, cap)
- Base course: waterproofing elevation, blind area
- Floor slab: bearing, junction detail

DIMENSIONS:
- Total structure thickness: [mm]
- Elevations: wall top +[X.XXX], bottom +[X.XXX]
- Top of structure elevation (parapet/ridge): +[X.XXX]
- Top of base slab elevation: +[X.XXX]
- Finished floor level (УЧП): +[X.XXX]
```

## Description Format: JUNCTION DETAIL

The most detailed type. Includes: roof-to-parapet junction, wall-to-foundation, window in opening, deformation joints.

```
DETAIL: [number and name, e.g. "Detail 5: Roof-to-parapet junction"]

DETAIL TYPE: roof-to-parapet junction / wall-to-slab junction /
             window reveal / deformation joint / base course / pipe penetration

CONSTRUCTION:
- Main element: [what connects to what]
- Sealing: [type -- mastic, tape, sealant]
- Fixings: [dowels, anchors, screws -- type, spacing]
- Insulation at junction: [material, thickness]

WATERPROOFING AT JUNCTION:
- Material: [Технониколь ЭПП / coating / self-adhesive tape]
- Turn-up on vertical: [mm]
- Extension on horizontal: [mm]
- Number of layers: [N]
- Fixing method: torch-applied / mechanical / adhesive

LAYERS (outside to inside / top to bottom):
1. [material], [mm]
2. [material], [mm]
...

DIMENSIONS:
- Turn-up height: [mm]
- Overlap: [mm]
- Fillet/cove size: [mm]
- Fastener (dowel/anchor) spacing: [mm]
- Gaps (assembly/ventilation): [mm]

NOTES:
[text annotations on drawing]
```

## Description Format: ROOF PLAN

If the image is a roof plan:

```
ROOF PLAN: [name, e.g. "Roof plan in axes А-Д/1-8"]
SCALE: М1:200 (if indicated)

ROOF TYPE: flat / pitched / accessible / non-accessible / green

SLOPES:
- Direction: toward funnels / toward parapet / toward gutters
- Value: i=[%] or [deg]
- Method: slope formation with expanded clay / tapered insulation / screed

DRAINAGE:
- Type: internal / external
- Funnels: [quantity], coordinates of each (e.g.: axis А/3, offset 500mm from axis А and 300mm from axis 3), diameter [mm]
- Emergency funnels/overflows: [quantity], coordinates of each (e.g.: axis А/3, offset 500mm from axis А and 300mm from axis 3)
- Gutters: [cross-section], length, slope

PARAPET:
- Height: [mm]
- Capping: galvanized steel / parapet tile
- Waterproofing junction: turn-up to [mm]

ROOF ACCESS:
- Hatches: [quantity], size [WxH], location
- Staircase superstructures: [location]
- Vent outlets: [quantity], diameter [mm]

ZONES:
- Green roof: [area], type (extensive/intensive)
- Terraces: [area], covering
- Technical zone: [equipment -- VRF, ventilation]

DIMENSIONAL REFERENCES (in mm):
- Overall dimensions along extreme axes: [Length] x [Width] mm
- Roof reference to axes: [centered / by edge / offset N mm from axis]
- Dimension chains: [list main distances]
- Door/window opening widths (clear): [mm]
- Joint thickness: [mm]
```

## Description Format: STAIRCASE DETAIL

If the image is a stair flight, railing, or mounting details:

```
STAIRCASE DETAIL: [name, e.g. "Railing mounting detail for staircase Л-1"]

STAIRCASE:
- Type: precast RC / monolithic / steel
- Flight width: [mm]
- Step height: [mm]
- Tread width: [mm]
- Number of steps per flight: [N]
- Slope: 1:[X]

RAILING:
- Height: [mm] (from step surface)
- Post material: tube [WxHxT] mm (e.g. 30x15x2)
- Handrail material: tube / profile [size]
- Infill: vertical balusters / screen / horizontal bars
- Baluster spacing: [mm]

MOUNTING:
- Anchor type: [brand, e.g. Hilti HST M10x100]
- Post spacing: [mm]
- Fixing method: to step / to stringer / to landing
- Base plate: [size], [number of holes]
- Embedment depth: [mm]

DIMENSIONS:
- Gap between flights: [mm]
- Landing width: [mm]
- Story height: [mm]

FIRE SAFETY REQUIREMENTS:
- Railing continuous over full height: yes/no
- Material: non-combustible / combustible
```

## Description Format: SPECIFICATION IN DRAWING

If the image is a specification table on a drawing sheet:

```
SPECIFICATION: [name, e.g. "Door opening specification"]

CONTENTS:
[reproduce the table in text format, preserving structure]

| Item | Mark | Name | Size WxH | Qty | Notes |
|------|------|------|----------|-----|-------|
| 1    | Д1   | Solid door | 900x2100  | 12  | EI 30 |
| 2    | Д2   | Glazed door | 1200x2100 | 4   | EI 60 |
[list ALL rows without exception -- skipping rows is not allowed]

NOTES:
[text notes to the specification]
```

## Rules

1. **Main rule:** for each element specify SPECIFIC numerical parameters -- thickness, size, grade, spacing. Do not just say "aerated concrete" -- write "газобетон D500 B2.5, thickness 300 mm".

2. **If the drawing has multiple zones/areas** with different solutions -- describe each zone separately.

3. **If a parameter is unreadable** on the image -- write "unreadable" instead of guessing.
3a. **If the image is completely unreadable** (rotated, resolution <72 dpi, solid artifacts):
output only:
`READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts]`
and do not attempt to describe the content.

4. **Description order:** for plans -- by axes left to right, top to bottom. For sections -- top to bottom or outside to inside.

5. **Two scales:** if a sheet has a main drawing and extracted details at larger scale -- describe both.

6. **Element marking:** if the drawing has markings (Д1, ПР-1, ОК-1) -- always include them, they are the key for linking to other drawings.

## Typical Description Errors (what to avoid)

- "The plan shows first floor rooms with partitions" -- Generic description, no specifics
- "The roof is insulated" -- Insulation type, thickness, number of layers not specified
- "The staircase railing is metal" -- Height, baluster spacing, mounting type not specified

- "Room 1.01 -- Vestibule, S=3.2 m2. Wall: газобетон D500 300mm. Door Д1 900x2100 EI30. Lintel ПР-1: L100x100x8, bearing 200mm" -- All elements are specific and verifiable
