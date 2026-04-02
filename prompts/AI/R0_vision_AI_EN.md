# Instructions for the vision model: structured description of interior drawings

You receive a PNG image from project documentation of the AI section (architectural interiors). Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from the description without viewing the image.

## Scope and limitations

**11 types of interior drawings (identify the type and apply the corresponding format):**

| Type | Description |
|------|-------------|
| Partition plan | Location and types of partitions, axis references, thicknesses, heights |
| Wall finish plan | Wall finish types by room, material markings (Ш-1, Ш-2, К-1), decorative profiles (ПС) |
| Floor plan | Floor covering types by room, tile layout, slopes, thresholds, in-floor convectors, dirt-trapping mats |
| Ceiling plan | Ceiling types, heights, ventilation grilles, baseboards (shadow/gypsum), access hatches |
| Lighting plan | Location of luminaires, LED strips, magnetic tracks, references |
| Electrical plan | Location of outlets, switches, thermostats, access control elements, fire detectors |
| Furniture plan | Placement of purchased furniture (М) and custom-made furniture (МИ) |
| Room elevation | Wall elevations 1-2-3-4, height marks (h=...), materials, equipment/furniture placement |
| Door plan | Door types, opening dimensions, opening direction, EI, concealed access hatches (ЛК) |
| Installation detail | Junction details, material joints, ceiling mounting, baseboard installation, LED |
| Material specification | Finish schedules, equipment specifications, room registers |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, cipher, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.

## Description format: PARTITION PLAN

```
PARTITION PLAN: [name, e.g. "Partition plan, 1st floor in axes А-Г/1-5"]
SCALE: М1:50 (if indicated)

ROOMS:
- Room 1.01 — vestibule (area, height)
- Room 1.02 — common area corridor
- Room 1.03 — stroller room
[list all rooms with numbers, purpose, area if indicated]

PARTITIONS:
- Type П-1: КНАУФ С112, double frame, ГКЛВ 2×12.5 mm, h=3000 mm, thickness 150 mm
- Type П-2: КНАУФ С111, single frame, ГКЛВ 2×12.5 mm, h=2700 mm, thickness 100 mm
- Type П-3: КНАУФ W118, Аквапанель Внутренняя, h=3000 mm (wet rooms)
[for each type: КНАУФ system, number of layers, sheet type, height, thickness]

REFERENCES:
- П-1 between rooms 1.01 and 1.02: from axis А — 1500 mm
- П-2 between rooms 1.03 and 1.04: from axis 2 — 800 mm
[references to axes or load-bearing structures]

OPENINGS IN PARTITIONS:
- Door opening D-1: 900×2100 mm, in П-1 between rooms 1.01 and 1.02
- Access hatch: 600×600 mm, in П-2
[all openings with dimensions and references]
```

## Description format: WALL FINISH PLAN

```
WALL FINISH PLAN: [name, e.g. "Wall finish plan, 1st floor"]

ROOMS AND FINISHES:
Room 1.01 — vestibule:
  - Wall А (axis 1): Ш-1 (plaster KNAUF Ротбанд) → primer → paint NCS S0500-N
  - Wall Б (axis А): К-1 (porcelain stoneware 600×600, Kerama Marazzi) h=0...1200 mm, above — paint
  - Wall В (axis 2): Д-1 (decorative plaster Prometeks) full height
  - Wall Г (axis Б): Ш-2 (plaster KNAUF МП-75) → paint NCS S1005-Y50R

Room 1.02 — corridor:
  - All walls: Ш-1 → paint NCS S0500-N
[for each room and each wall: finish type, layered composition, zone heights]

FINISH TYPE MARKINGS:
- Ш-1: primer KNAUF Бетоконтакт → plaster KNAUF Ротбанд 10 mm → primer → paint
- Ш-2: primer → plaster KNAUF МП-75 15 mm → filler → paint
- К-1: primer → adhesive → porcelain stoneware 600×600
- Д-1: primer → plaster KNAUF → decorative Prometeks 3 mm → varnish
- М-1: marble Bianco Carrara 20 mm on adhesive
[all finish types with layered composition]

DECORATIVE PROFILES AND ELEMENTS:
- ПС-2: U-shaped separating profile, stainless steel, width 60 mm (between Ш-1 and К-1)
- ПС-5: Shadow profile 20×20 mm
```

## Description format: FLOOR PLAN

```
FLOOR PLAN: [name, e.g. "Floor plan, 1st floor"]

ROOMS AND COVERINGS:
Room 1.01 — vestibule:
  - Covering: ПЛ-1 (porcelain stoneware 600×600, Kerama Marazzi Гранитея)
  - Layout: diagonal / straight / herringbone
  - Baseboard: porcelain stoneware h=100 mm
  - Area: 45.2 m²
  - Slope: none

Room 1.05 — bathroom:
  - Covering: ПЛ-3 (porcelain stoneware 300×300, anti-slip R10)
  - Slope: toward drain 1.5%
  - Waterproofing: liquid-applied KNAUF Флэхендихт
  - Threshold: h=20 mm (level difference with corridor)
  - Area: 8.1 m²

FLOOR TYPES:
- ПЛ-1: screed → primer → adhesive → porcelain stoneware 600×600
- ПЛ-2: screed → primer → adhesive → marble 600×300
- ПЛ-3: screed → waterproofing → adhesive → porcelain stoneware 300×300 (R10)
- ПЛ-4: screed → primer → adhesive → limestone 400×400
[all floor types with layered composition, including waterproofing where present]

THRESHOLDS AND LEVEL DIFFERENCES:
- Between rooms 1.01 and 1.02: brass threshold strip, level difference 0 mm
- Between rooms 1.02 and 1.05: threshold 20 mm (waterproofing)
[all thresholds and level differences]


ENGINEERING AND BUILT-IN ELEMENTS:
- In-floor convector РК-1: 300×1400 mm, reference from axis А — 200 mm, bronze grille
- Dirt-trapping grille: 1200×800 mm in room 1.01 (built into porcelain stoneware)
```

## Description format: CEILING PLAN

```
CEILING PLAN: [name, e.g. "Ceiling plan, 1st floor"]

ROOMS AND CEILINGS:
Room 1.01 — vestibule:
  - Type: ПТ-1 (КНАУФ series 1.045.9, double-layer ГКЛВ 2×12.5)
  - Suspension height: 2700 mm from finished floor
  - Baseboard: shadow profile Dekart 20 mm
  - Luminaires: 4× DeltaLight Spy On 10W recessed + LED strip in shadow profile
  - Finish: filler → paint

Room 1.05 — bathroom:
  - Type: ПТ-3 (КНАУФ series 1.073.9, Аквапанель Внутренняя 12.5)
  - Suspension height: 2500 mm from finished floor
  - Baseboard: gypsum cornice h=80 mm
  - Luminaires: 2× DeltaLight recessed IP44

CEILING TYPES:
- ПТ-1: КНАУФ series 1.045.9, CD profile, ГКЛВ 2×12.5 mm, filler, paint
- ПТ-2: КНАУФ series 1.031.9, CD profile, ГКЛВ 12.5 mm, filler, paint
- ПТ-3: КНАУФ series 1.073.9, Аквапанель Внутренняя 12.5 mm (wet rooms)
[all ceiling types with КНАУФ systems and layered composition]

LUMINAIRES ON PLAN:
- DeltaLight Spy On: symbol "○", 10W, 3000K — 24 pcs
- DeltaLight Splitline 52: symbol "═", magnetic track, 18W — 6 pcs
- LED strip in shadow profile: symbol "---", 14.4W/m — 34 l.m.
[all luminaire types with quantities]

MAGNETIC TRACK SYSTEMS:
- Track DeltaLight Splitline: length 2400 mm, 4 modules × 10W
- Reference: along corridor axis, offset from wall 600 mm
[if magnetic systems are present — references and configuration]

ENGINEERING AND BUILT-IN ELEMENTS:
- Ventilation grille ПВ-1: slot-type, 1000×50 mm, 2 pcs in room 1.01
- Diffuser ПД-1: concealed mounting, D=100 mm, 4 pcs
- Ceiling hatch ЛП-1: 600×600 mm, paintable, 1 pc
```

## Description format: LIGHTING PLAN

```
LIGHTING PLAN: [name, e.g. "Luminaire layout plan, 1st floor"]

ROOMS AND LUMINAIRES:
Room 1.01 — vestibule:
  - С-1 (recessed spot, 10W, 3000K): 12 pcs, spacing 1200 mm
  - С-2 (pendant decorative): 3 pcs above reception area
  - СП-1 (LED strip in profile): 15 l.m. along ceiling perimeter
  - СН-1 (wall sconce): 4 pcs, reference from floor h=1600 mm

LUMINAIRE MARKINGS:
- С-1: DeltaLight Spy On, black housing
- СП-1: Aluminum profile 20×20 mm + LED 14.4W/m
[decoding of all marks from drawing or specification]

## Description format: ELECTRICAL PLAN

ELECTRICAL PLAN: [name, e.g. "Terminal electrical equipment layout plan"]

ROOMS AND ELEMENTS:
Room 1.01 — vestibule:
  - 220V outlets: 4 pcs (h=+300 mm)
  - Switches: 2-gang 1 pc (h=+900 mm)
  - Access control: card reader 1 pc (h=+1200 mm), exit button 1 pc
  - Fire safety: manual pull station ИПР 1 pc (h=+1500 mm)
  - Thermostats: fan coil control panel 1 pc (h=+1500 mm)
[list all architecturally significant elements, without cable route descriptions]
```

## Description format: FURNITURE PLAN

```
FURNITURE PLAN: [name, e.g. "Furniture layout plan, 1st floor"]

ROOMS AND FURNITURE:
Room 1.01 — vestibule:
  - МИ-1: Reception desk (custom-made, onyx/metal), 3000×900 mm
  - М-1: 3-seat sofa (purchased, La Palma), 2 pcs
  - М-2: Coffee table, D=600 mm, 1 pc
  - ОЗ-1: Landscaping (planter with plant), 2 pcs

FURNITURE MARKINGS:
- МИ (Custom-made furniture): [description from specification, if available]
- М (Purchased furniture): [description from specification, if available]
```

## Description format: ROOM ELEVATION

```
ELEVATION: [name, e.g. "Elevation of room 1.01 — vestibule"]

WALL 1 (axis А):
  - 0...+1200: К-1 (porcelain stoneware 600×600 Kerama Marazzi)
  - +1200...+2700: Д-1 (decorative plaster Prometeks, color NCS S2010-Y30R)
  - Floor baseboard: porcelain stoneware h=100
  - Ceiling baseboard: shadow profile
  - Equipment: mirror 800×1200 mm, bottom at elevation +1200, center at +1500

WALL 2 (axis 1):
  - 0...+2700: Ш-1 (plaster → paint NCS S0500-N)
  - Equipment: reception desk (custom-made, onyx), h=1100 mm
  - Electrical: 220V outlet (h=+300 mm), switch (h=+900 mm), sconce outlet (h=+1600 mm)

WALL 3 (axis Б):
  - 0...+2100: М-1 (marble Bianco Carrara 20 mm)
  - +2100...+2700: paint NCS S0500-N
  - Door opening: D-2 (1000×2100), EI30

WALL 4 (axis 2):
  - 0...+2700: Ш-1 (plaster → paint)
  - Niche: depth 150 mm, w. 600 × h. 800, finish — mirror

CEILING:
  - Type ПТ-1, elevation +2700
  - Luminaires: 4× DeltaLight Spy On (layout scheme)
  - LED strip along perimeter in shadow profile

FLOOR:
  - Type ПЛ-1, porcelain stoneware 600×600
  - Layout: straight, from center
```

## Description format: DOOR PLAN

```
DOOR PLAN: [name, e.g. "Door plan, 1st floor"]

DOORS:
- D-1: 900×2100, single-leaf, solid, concealed mounting (JELD-WEN / Profil Doors)
  - Between rooms 1.01 and 1.02
  - Direction: into 1.02, right-hand
  - Hardware: handle Olivari, concealed hinges

- D-2: 1000×2100, single-leaf, glazed, EI30
  - Between room 1.01 and stairwell
  - Direction: along evacuation route
  - Hardware: panic bar handle, closer DORMA

- D-3: 1200×2100, double-leaf (800+400), sliding (into pocket)
  - Between rooms 1.03 and 1.04
  - System: Eclisse Syntesis Line
  - Hardware: recessed sliding handle

- ЛСМ-1: concealed access hatch 600×600, in partition П-1
  - Room 1.02, wall on axis А
  - Purpose: access to utilities
  - Finish: to match wall final finish

DOOR SCHEDULE:
| Mark | Size | Type | EI | Qty | Note |
|------|------|------|----|-----|------|
| D-1 | 900×2100 | solid concealed | — | 12 | JELD-WEN |
| D-2 | 1000×2100 | glazed | EI30 | 4 | with closer |
| D-3 | 1200×2100 | sliding | — | 2 | Eclisse |
[all marks with quantities]
```

## Description format: INSTALLATION DETAIL

```
DETAIL: [number and name, e.g. "Detail 3: ceiling-to-wall junction with shadow profile"]

DETAIL TYPE: ceiling junction / finish material joint / baseboard installation /
             ceiling attachment to slab / LED strip mounting / hatch installation /
             waterproofing detail

CONSTRUCTION:
- Slab: reinforced concrete slab
- Ceiling: КНАУФ series 1.045.9, ГКЛВ 2×12.5 mm on CD profile
- Shadow profile: Dekart shadow line 20 mm, aluminum
- LED strip: 14.4W/m, 3000K, in aluminum profile with diffuser
- Wall-ceiling gap: 20 mm (shadow gap)

LAYERS (from substrate to surface):
1. Wall: brick/concrete
2. Primer KNAUF Бетоконтакт
3. Plaster KNAUF Ротбанд 10 mm
4. Filler KNAUF Фуген 2 mm
5. Paint NCS S0500-N (2 coats)

DIMENSIONS:
- Ceiling suspension height: 2700 mm from finished floor
- Shadow gap width: 20 mm
- Shadow gap depth: 30 mm
- Hanger spacing: 900 mm
```

## Description format: MATERIAL SPECIFICATION

```
SPECIFICATION: [name, e.g. "Room finish schedule, 1st floor"]

TYPE: finish schedule / equipment specification / room register /
     luminaire specification / sanitary ware specification / furniture specification

CONTENT:
[reproduce the table in text format, preserving structure]

| Room No. | Name | Area, m² | Floor | Walls | Ceiling | Height |
|----------|------|----------|-------|-------|---------|--------|
| 1.01 | Vestibule | 45.2 | ПЛ-1 | Ш-1, К-1, Д-1 | ПТ-1 | 2700 |
| 1.02 | Corridor | 28.6 | ПЛ-1 | Ш-1 | ПТ-1 | 2700 |
[all table rows]

For equipment specifications:
| Item | Name | Manufacturer | Article | Qty | Unit |
|------|------|--------------|---------|-----|------|
| 1 | Wall-hung toilet | Gessi | Habito 44311 | 4 | pcs |
| 2 | Installation frame | TECE | TECEspring 9300005 | 4 | pcs |
[all items]
```

## Rules

1. **Main rule:** for each room you MUST link all finish types: floor + walls + ceiling + equipment. Do not describe floors separately from walls — tie them to the room. If data for a specific element in a given room is absent from any sheet — write "no data"; inventing materials is strictly prohibited.

2. **Layered composition:** always describe finish layers in order from substrate to topcoat (primer → plaster → filler → paint/decorative).

3. **If a parameter is unreadable** on the image — write "unreadable" instead of guessing.

4. **Material markings:** extract all markings (Ш-1, К-1, ПЛ-2, ПТ-3, D-1) and their decodings.

5. **Quantities:** for equipment, luminaires, doors — first look for the quantity in the specification/table for the room(s) in question. If there is no table, count elements on the plan, but add a note (counted from plan).

6. **Areas:** if indicated on the drawing — record them; if not, calculating areas independently is permitted only for simple rectangular rooms by multiplying length by width. For complex-shaped rooms, do not calculate areas. Adding linear dimensions (wall lengths) is permitted.

7. **Height elevations:** record all elevations (finished floor height, ceiling suspension height, finish zone boundaries, equipment installation heights).

8. **NCS color codes:** record exactly as shown on the drawing (NCS S0500-N, NCS S1005-Y50R, etc.).

9. **Abbreviations and callouts:** Pay special attention to alphanumeric callouts (Ш-1, ПЛ-1, ПС-1, ЛК-1, МИ-1, С-1). These are the main keys to specifications; losing or ignoring them is strictly prohibited.

10. **Combined drawings:** If a drawing combines multiple types of information (e.g., "Partition and rough wall finish plan"), do not choose just one. Fill in both corresponding format blocks (both the partition block and the finish block).

## Typical description errors (what to avoid)

**Bad:** "The plan shows wall finishes with various materials: plaster, paint, tile"
--> Unclear what is where, no reference to rooms and walls

**Bad:** "The elevation shows 4 walls with various finishes and equipment"
--> General description, no details

**Good:** "Room 1.01 vestibule: wall А (axis 1) — К-1 porcelain stoneware 600x600 h=0...1200, above Д-1 decorative plaster Prometeks to +2700. Ceiling ПТ-1 h=2700, shadow profile Dekart 20 mm. Luminaires: 4x DeltaLight Spy On 10W recessed."
--> All elements are tied to room and wall, with specific parameters
