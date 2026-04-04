# Instructions for Vision Model: Structured Description of Steel Structure Drawings (KM)

You receive a PNG image from the KM (metal structures) section of project documentation. Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from your description without viewing the image.
Your task is to perform a deep technical analysis of the PNG image from the KM section and create its "digital twin" in text form.
Your description must be precise enough that another structural engineer could fully read the drawing without seeing the original.

## Scope and Limitations

**5 types of KM drawings (identify the type and apply the corresponding format):**

| Type | Share | Description |
|------|-------|-------------|
| Layout plan | 20% | Plans showing locations of steel members relative to axes, elevations |
| Element drawing | 30% | Fachwerk columns, staircases (LM-1..LM-5), beams, platforms -- profiles, dimensions, details |
| Connection detail | 20% | Bolted, welded, anchor connections -- bolt layout, weld symbols, plate dimensions |
| Steel specification | 15% | Tables: member marks, profiles, lengths, unit mass, total mass, steel grade |
| Development/elevation | 15% | Elevations of structures, facade bracket layouts, lightning mast supports |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, project code, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.
**If a sheet contains multiple types simultaneously -- describe each in its own block.**

## Description Format: LAYOUT PLAN

If the image is a plan showing locations of steel members:

```
LAYOUT PLAN: [name, e.g. "Layout of steel structures at elevation -3.600"]
SCALE: M1:100 (if indicated)
LEVEL: underground part (-2 floor) / underground part (-1 floor) / above-ground part / roof

AXES:
- Longitudinal: A, B, V, G, D (spacing [mm])
- Transverse: 1, 2, 3, 4, 5 (spacing [mm])

COLUMNS:
- KF-1: profile [HEB/HEA/SHS size], at axis intersection [X/Y], base elevation [+/-X.XXX], top elevation [+/-X.XXX]
- KF-2: profile [...], at axis [X/Y], base [+/-X.XXX], top [+/-X.XXX]
[list ALL columns with markings, profiles, axis locations]

BEAMS:
- B-1: profile [IPE/HEA/channel size], from axis [X/Y] to axis [X/Y], elevation [+/-X.XXX], span [mm]
- B-2: profile [...], from [X/Y] to [X/Y], elevation [+/-X.XXX], span [mm]
[list ALL beams with markings]

STAIRCASES:
- LM-1: location (axes [X-Y/N-M]), type (straight-flight / L-shaped / U-shaped), floors served
- LM-2: location, type, floors served
[list ALL metal staircases]

PLATFORMS:
- PL-1: location (axes [X-Y/N-M]), elevation [+/-X.XXX], dimensions [LxW mm]
[list ALL platforms]

BRACING:
- Connection type: [cross / portal / K-type]
- Location: between axes [X-Y], at levels [from ... to ...]
- Profile: [angle/channel/tube size]

DIMENSIONAL REFERENCES (in mm):
- Overall dimensions along extreme axes
- Member spacing
- Offsets from axes

NOTES ON DRAWING:
[list all text notes]
```

## Description Format: ELEMENT DRAWING

If the image is a detailed drawing of a steel member (column, beam, staircase, platform):

```
ELEMENT DRAWING: [mark and name, e.g. "KF-1 Fachwerk column"]
SCALE: M1:20 / M1:25 (if indicated)

MEMBER TYPE: column / beam / staircase / platform / bracket / mast support

MAIN PROFILE:
- Section: [HEB 200 / HEA 160 / SHS 120x120x5 / IPE 270 / channel 20P / I-beam 20B1]
- Steel grade: [S245 / S255 / S345]
- Length: [mm]
- Quantity: [N pcs]

COMPONENTS (for assembled members):
Component 1: [name], profile [size], length [mm], qty [N]
Component 2: [name], profile [size], length [mm], qty [N]
[list ALL components]

FOR STAIRCASES (LM-N):
- Stringers: profile [channel/IPE], length [mm], slope [degrees or 1:X]
- Steps: material [checker plate/expanded metal/grating], thickness [mm], width [mm], depth [mm]
- Step count: [N]
- Step height: [mm], tread depth: [mm]
- Flight width (clear): [mm]
- Landings: [quantity], dimensions [LxW mm], deck type [checker plate/grating], thickness [mm]
- Railings: height [mm], post profile [tube WxHxT], post spacing [mm]
- Infill: [vertical bars / mesh / horizontal bars], spacing [mm]

FOR PLATFORMS:
- Frame: profile [angle/channel size]
- Deck: [checker plate/expanded metal/grating], thickness [mm]
- Supports: profile [angle/tube size], spacing [mm]
- Railings: height [mm], post spacing [mm]
- Toeboard: height [mm], material

CONNECTIONS (visible on element drawing):
- To main structure: [bolted M__ class __ / welded fillet __mm / anchored]
- Between components: [bolted / welded], details

DIMENSIONS:
- Overall: [LxWxH mm]
- Key spacing dimensions
- Connection point locations

NOTES ON DRAWING:
[list all text notes, especially steel grade, coating requirements]
```

## Description Format: CONNECTION DETAIL

If the image is a connection detail (bolted, welded, or anchor):

```
CONNECTION DETAIL: [number and name, e.g. "Node 1: Column KF-1 base"]
SCALE: M1:10 / M1:5 (if indicated)

CONNECTION TYPE: column base / beam-to-column / beam splice / beam-to-beam /
                 anchor to concrete / brace connection / staircase attachment

CONNECTED MEMBERS:
- Member 1: [mark], profile [size]
- Member 2: [mark], profile [size] (or: RC structure [wall/column/slab])

BOLTED CONNECTION (if present):
- Bolt grade: [5.8 / 8.8 / 10.9]
- Bolt diameter: M[12/16/20/24]
- Bolt quantity: [N]
- Bolt layout: [rows x columns, e.g. 2x3]
- Hole diameter: [mm]
- Spacing between bolts: [mm] (center-to-center)
- Edge distance: [mm] (center to edge)
- End distance: [mm] (center to member end)
- Washer: [yes/no], type [flat/spring/HV set]
- Tightening: [snug-tight / pretensioned / slip-critical]

WELDED CONNECTION (if present):
- Weld type: [butt / fillet / combined]
- Fillet weld throat: [mm]
- Weld length: [mm] or [continuous]
- Electrode grade: [E42 / E50 / E60] per GOST 9467
- Weld symbol per GOST 2.312: [transcribe exactly as shown]
- Welding position: [flat / horizontal / vertical / overhead]

PLATES AND STIFFENERS:
- Base plate: [LxWxT mm], steel grade
- Stiffeners: [quantity], [LxWxT mm]
- Gusset plates: [LxWxT mm]
- End plates: [LxWxT mm]

ANCHOR CONNECTION (if present):
- Anchor type: [cast-in / post-installed expansion / chemical / through-bolt]
- Anchor diameter: M[12/16/20/24]
- Anchor length: [mm]
- Embedment depth: [mm]
- Anchor quantity: [N]
- Anchor layout: [spacing mm x edge distance mm]
- Base material: [RC class B__ / masonry / steel]
- Grout: [type, thickness mm]

DIMENSIONS:
- Plate dimensions
- Bolt/anchor positions (from edges and between each other)
- Weld locations and lengths
- Gap/clearance values

NOTES ON DRAWING:
[list all text notes, especially welding requirements, bolt tightening specs, surface prep]
```

## Description Format: STEEL SPECIFICATION

If the image is a steel specification table:

```
STEEL SPECIFICATION: [name, e.g. "Steel specification for KM-1 (underground part)"]

TABLE CONTENTS:
[reproduce the table in text format, preserving structure]

| Item | Member mark | Profile | Steel grade | Length, mm | Qty | Unit mass, kg | Total mass, kg |
|------|-------------|---------|-------------|------------|-----|---------------|----------------|
| 1    | KF-1        | HEB 200 | S245        | 3600       | 4   | 213.1         | 852.4          |
| 2    | B-1         | IPE 270 | S245        | 4500       | 8   | 162.5         | 1300.0         |
[list ALL rows without exception -- skipping rows is not allowed]

SUMMARY BY STEEL GRADE:
- S245: [total mass, kg]
- S255: [total mass, kg]
- S345: [total mass, kg]
- TOTAL: [total mass, kg]

ADDITIONAL MATERIALS (if present):
| Item | Name | Standard | Size | Qty | Mass, kg |
|------|------|----------|------|-----|----------|
| 1    | Bolt M20x60 cl.8.8 | GOST 7798 | M20 | 48 | ... |
| 2    | Nut M20 cl.8 | GOST 5915 | M20 | 48 | ... |
[list ALL hardware and additional materials]

NOTES:
[text notes to the specification]
```

## Description Format: DEVELOPMENT/ELEVATION

If the image is a development view or elevation of structures:

```
DEVELOPMENT: [name, e.g. "Development along axis A (facade brackets)"]
SCALE: M1:100 / M1:50 (if indicated)

VIEW TYPE: elevation along axis / facade bracket layout / lightning mast support / equipment enclosure

STRUCTURE:
- Main members: [profiles, spacing]
- Secondary members: [profiles, spacing]
- Connections to main building: [type, spacing]

BY LEVELS (bottom to top):
Level -3.600:
  - Members: [mark, profile, location]
  - Connections: [type]
Level -0.150:
  - Members: [mark, profile, location]
  - Connections: [type]
[continue for all levels]

DIMENSIONS:
- Overall height: [mm]
- Bay spacing: [mm]
- Member spacing: [mm]
- Cantilever lengths: [mm]

NOTES ON DRAWING:
[list all text notes]
```

## Rules

1. **Main rule:** for each element specify SPECIFIC numerical parameters -- profile size, steel grade, bolt class, weld throat, plate thickness. Do not just say "I-beam" -- write "IPE 270, S245, L=4500 mm".

2. **If the drawing has multiple members/nodes** -- describe each separately with its mark.

3. **If a parameter is unreadable** on the image -- write "unreadable" instead of guessing.
3a. **If the image is completely unreadable** (rotated, resolution <72 dpi, solid artifacts):
output only:
`READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts]`
and do not attempt to describe the content.

4. **Description order:** for plans -- by axes left to right, top to bottom. For elements -- main profile first, then components. For connections -- from main member outward.

5. **Two scales:** if a sheet has a main drawing and extracted details at larger scale -- describe both.

6. **Member marking:** if the drawing has markings (KF-1, B-1, LM-1, PL-1, Node 1) -- always include them, they are the key for linking to other drawings.

7. **Weld symbols:** transcribe exactly as shown on the drawing, including standard designation (GOST 14771, GOST 5264). If a weld table is present -- reproduce it fully.

8. **Bolt tables:** if a bolt/hardware table is present on the drawing -- reproduce it fully with all columns.

## Typical Description Errors (what to avoid)

- "The plan shows steel columns and beams" -- Generic, no profiles, no locations
- "The column is welded to the base plate" -- Weld type, throat, plate thickness not specified
- "Bolted connection" -- Bolt class, diameter, quantity, spacing not specified

+ "KF-1: HEB 200, S245, L=3600mm, at axes B/3, el. -3.600 to -0.150. Base plate 300x300x20, 4x M24 cl.8.8 anchors, embedment 300mm" -- All parameters are specific and verifiable
