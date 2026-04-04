# Instructions for vision model: structured description of fire suppression drawings

You receive a PNG image from the project documentation of section PT (fire suppression). Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from the description without viewing the image.

## Scope and limitations

**7 types of fire suppression drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|-----------|
| System schematic (axonometric) | 20% | Axonometric view of ВПВ (B2/B21), sprinkler/drencher system, gas suppression piping |
| Floor plan with fire suppression | 25% | Plans with hydrant locations, sprinkler heads, piping routes |
| Pump station layout | 10% | Fire pump room: pumps, tanks, piping, valves, control panels |
| Gas/powder suppression station | 10% | ГОТВ cylinder storage, manifolds, piping to protected rooms |
| Riser development / section | 10% | Vertical section of ВПВ risers, sprinkler risers, floor connections |
| Control / wiring diagram | 10% | Electrical control of suppression system: start/stop, interlocks, signaling |
| Specification on drawing | 15% | Tables: pipe specs, equipment specs, valve specs |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, cipher, organization)
- Revision tables
- Sheet numbers and their titles
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.

## Principle of reading

Fire suppression systems are read from water/gas source to discharge point: for VPV — pump → main pipe → riser → fire hydrant cabinet; for sprinkler — pump → feed main → cross main → branch → sprinkler head; for gas suppression — cylinder battery → collector → distribution pipe → nozzle. Each path must preserve: pipe diameter, material, length, valves at every segment.

## Description format: SYSTEM SCHEMATIC (AXONOMETRIC)

If the image is an axonometric view of a fire water supply or suppression system:

```
AXONOMETRIC DIAGRAM: [title, e.g. "Аксонометрическая схема системы В2"]
SYSTEM: B2 (ВПВ) / B21 (sprinkler) / B21 (drencher) / АУГПТ / АУПП
SCALE: no scale (typical for axonometric views)

SOURCE / INLET:
- Water source: [city network / fire tank / combined]
- Inlet diameter: Ду[mm]
- Inlet pressure: [MPa] (if indicated)
- Connection point: at axes [X-Y], elevation [+X.XXX]

PUMP STATION (if shown):
- Duty pump: [make/type], Q=[l/s], H=[m], N=[kW]
- Standby pump: [make/type], Q=[l/s], H=[m], N=[kW]
- Jockey pump: [if present], Q=[l/s], H=[m]
- Fire water tank: V=[m3]
- Membrane tank: V=[l], P=[MPa]

MAINS:
- Ring / dead-end main: Ду[mm], elevation [+X.XXX], material
- Section from axis [X] to axis [Y]: Ду[mm], length [m] (if indicated)

RISERS:
- Ст.В2-1: Ду[mm], from elev. [+X.XXX] to elev. [+X.XXX], at axes [X-Y]
- Ст.В2-2: Ду[mm], from elev. [+X.XXX] to elev. [+X.XXX], at axes [X-Y]
[list ALL risers with labeling, diameters, location]

FIRE HYDRANTS / SPRINKLER HEADS:
- Floor 1 (elev. +X.XXX): hydrant ПК-1 on Ст.В2-1, Ду[mm]
- Floor 2 (elev. +X.XXX): hydrant ПК-2 on Ст.В2-1, Ду[mm]
[for each floor: device type, riser, connection]

OR for sprinkler:
- Floor 1: [N] sprinkler heads, pipe Ду[mm], branch from Ст.B21-1
- Floor 2: [N] sprinkler heads, pipe Ду[mm], branch from Ст.B21-1

VALVES:
- Control valve (задвижка): Ду[mm], [location]
- Check valve: Ду[mm], [location]
- Test valve: Ду[mm], [location]
- Drain valve: Ду[mm], [location]
- Motorized valve: Ду[mm], [location, interlock signal]
[list all visible valves]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: FLOOR PLAN WITH FIRE SUPPRESSION

If the image is a floor plan showing hydrants, sprinklers, or piping:

```
FLOOR PLAN: [title, e.g. "План 1-го этажа. Противопожарный водопровод"]
SCALE: М1:100 (if indicated)
SYSTEMS ON PLAN: B2 / B21 / АУГПТ (which systems are shown)

AXES:
- Longitudinal: А, Б, В, Г (spacing [mm])
- Transverse: 1, 2, 3, 4, 5 (spacing [mm])

RISERS ON PLAN:
- Ст.В2-1: at axes [X-Y], Ду[mm]
- Ст.В2-2: at axes [X-Y], Ду[mm]
[list all risers with axis references]

FIRE HYDRANTS:
- ПК-1: at axes [X-Y], in cabinet ШПК-[type], on Ст.В2-1
- ПК-2: at axes [X-Y], in cabinet ШПК-[type], on Ст.В2-2
[for each hydrant: label, location, cabinet type, riser]

SPRINKLER HEADS (if present):
- Room [number] ([purpose]): [N] heads, spacing [m] x [m]
- Room [number] ([purpose]): [N] heads, spacing [m] x [m]
[for each room: head count and arrangement]

HORIZONTAL PIPELINES:
- Ring main: Ду[mm], along axes [route description]
- Branch to ПК-1: Ду[mm], from [riser/main]
[for each section: diameter, routing]

FIRE COMPARTMENT BOUNDARIES:
- Fire wall at axis [X]: EI[value]
- Pipe penetration seal: [type]
[list fire barriers crossed by piping]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: PUMP STATION LAYOUT

If the image is a fire pump room layout:

```
PUMP STATION LAYOUT: [title, e.g. "План насосной станции пожаротушения"]
SCALE: М1:50 / М1:100

ROOM:
- Dimensions: [LxWxH] mm
- Floor elevation: +[X.XXX]
- Location: at axes [X-Y]
- Fire resistance rating: [if indicated]

PUMPS:
- Fire pump 1 (duty): [make/type], Q=[l/s], H=[m], N=[kW]
- Fire pump 2 (standby): [make/type], Q=[l/s], H=[m], N=[kW]
- Jockey pump: [make/type], Q=[l/s], H=[m], N=[kW]
[list all pumps with characteristics]

FIRE WATER TANK:
- Type: [steel / reinforced concrete / sectional]
- Volume: [m3]
- Dimensions: [LxWxH] mm
- Quantity: [pcs]

PIPING:
- Suction manifold: Ду[mm], material
- Discharge manifold: Ду[mm], material
- Gate/ball valves: [types, diameters, quantities]
- Check valves: [location, Ду]
- Pressure gauges / sensors: [location]
- Flexible joints: [location]

CONTROL PANEL:
- Location: [in pump room / adjacent room]
- Type: [ШУН / ШУП / custom]

DRAINAGE:
- Floor drain: Ду[mm]
- Drainage sump: [dimensions, pump if present]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: GAS/POWDER SUPPRESSION STATION

If the image is a ГОТВ cylinder storage or gas suppression station:

```
SUPPRESSION STATION: [title, e.g. "Станция газового пожаротушения"]
SUPPRESSION TYPE: gas (ГОТВ) / powder / aerosol

ROOM:
- Dimensions: [LxWxH] mm
- Location: at axes [X-Y]
- Temperature regime: [if indicated]

CYLINDERS:
- ГОТВ type: [Halon 125 / Halon 227ea / Inergen / CO2 / powder type]
- Cylinder volume: [l]
- Cylinder pressure: [MPa]
- Quantity per direction: [pcs]
- Total quantity: [pcs]
- Cylinder rack/frame: [type, dimensions]

MANIFOLD:
- Collector diameter: Ду[mm]
- Material: [steel]
- Distribution valves: [type, Ду, per direction]
- Check valves: [location]

PIPING TO PROTECTED ROOMS:
- Direction 1: to room [name/number], Ду[mm], length ~[m]
- Direction 2: to room [name/number], Ду[mm], length ~[m]
[for each direction: pipe size, destination]

CONTROL:
- Start button: [location]
- Stop button: [location]
- Mode selector: [auto/manual/local]
- Light indicators: [list]
- Sound alarm: [type]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: RISER DEVELOPMENT / SECTION

If the image is a vertical section showing fire suppression risers:

```
RISER SECTION: [title, e.g. "Разрез 1-1. Стояки В2"]
SYSTEM: B2 / B21

RISERS:
- Ст.В2-1: Ду[mm]
  - Basement (elev. -X.XXX): connection to main, valve Ду[mm]
  - Floor 1 (elev. +X.XXX): hydrant ПК, tee Ду[mm]
  - Floor 2 (elev. +X.XXX): hydrant ПК, tee Ду[mm]
  ...
  - Top floor (elev. +X.XXX): hydrant ПК, cap/plug
[for each riser: floor-by-floor connections]

PIPE PENETRATIONS:
- Through floor slab: sleeve Ду[mm], seal type
- Through fire wall: fire seal EI[value]

MOUNTING:
- Pipe clamps: spacing [mm]
- Support type: [wall bracket / ceiling hanger]
- Installation height of hydrant: [mm] from floor

DIMENSIONS:
- Floor heights: [m]
- Hydrant installation height: [mm]
- Distance from riser to hydrant cabinet: [mm]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: CONTROL / WIRING DIAGRAM

If the image is an electrical control diagram for the suppression system:

```
CONTROL DIAGRAM: [title, e.g. "Схема электроуправления АУГПТ"]
SYSTEM: ВПВ / АУГПТ / АУПП

POWER SUPPLY:
- Category: [I / II]
- Sources: [two independent feeds / UPS / diesel]
- Control panel: [type, make]

CONTROL ELEMENTS:
- Fire alarm panel (ППКП): [type, make]
- Control module: [type]
- Start button: [location, type]
- Stop button: [location, type]
- Mode selector: [auto/manual/off]

ACTUATORS:
- Fire pump start: [signal type, cable]
- Motorized valve open: [signal type, cable]
- Ventilation shutdown: [signal type, cable]
- Damper closure: [signal type, cable]
- Door holder release: [signal type, cable]
- ГОТВ release solenoid: [signal type, cable]

SIGNALING:
- Light indicators: [list with locations]
  - "ПОЖАР" / "FIRE"
  - "ГАЗ — УХОДИ" / "GAS — LEAVE"
  - "ГАЗ — НЕ ВХОДИ" / "GAS — DO NOT ENTER"
  - "АВТОМАТИКА ВКЛЮЧЕНА" / "AUTO ON"
  - "АВТОМАТИКА ОТКЛЮЧЕНА" / "AUTO OFF"
- Sound alarm: [type, location]
- Signal to fire alarm panel: [type]

INTERLOCKS (sequence):
1. Fire detector activation → signal to ППКП
2. ППКП → start delay timer (30 s)
3. During delay: sound + light alarm, ventilation shutdown, damper closure
4. After delay: ГОТВ release / pump start / valve open
5. Manual stop: cancels release during delay

CABLES:
- From ППКП to control panel: [type, cross-section]
- From control panel to actuators: [type, cross-section]
- Fire-rated cables: [FR rating, type]

NOTES ON DRAWING:
[list all text notes]
```

## Description format: SPECIFICATION ON DRAWING

If the image is a specification table:

```
SPECIFICATION: [title, e.g. "Спецификация оборудования системы В2"]
SYSTEM: B2 / B21 / АУГПТ / АУПП / general

CONTENT:
[reproduce the table in text format, preserving structure]

| Item | Description | Make/Type | Ду/Size | Unit | Qty | Note |
|------|-------------|-----------|---------|------|-----|------|
| 1    | Труба стальная ВГП | ГОСТ 3262-75 | Ду50 | m | 120 | B2 |
| 2    | Труба стальная ВГП | ГОСТ 3262-75 | Ду65 | m | 45  | B2 |
| 3    | Кран пожарный Ду50 | КПЧ-50 | Ду50 | pcs | 16  | ... |
[all table rows]

TOTALS (if present):
- Total pipe length by systems: [values]
- Total equipment quantity: [values]

NOTES:
[text notes to specification]
```

## Rules

1. **Main rule:** for each element, specify SPECIFIC numerical parameters -- diameter, length, pressure, flow rate, quantity. Do not write "fire suppression piping" -- write "трубопровод стальной ВГП Ду65, length ~12 m, from Ст.В2-1 to ПК-3".

2. **If multiple systems are on the drawing** (B2 + B21 on one plan) -- describe each system separately.

3. **If a parameter is not legible** on the image -- write "unreadable" instead of guessing.

4. **Description order:** for axonometric views -- bottom to top (from pump station to upper floors). For plans -- along axes left to right. For risers -- top to bottom.

5. **Two scales:** if there is a main drawing and enlarged detail views on the same sheet -- describe both.

6. **Element labeling:** if the drawing has riser labels (Ст.В2-1, Ст.B21-3), hydrant labels (ПК-1, ПК-2), sprinkler head labels -- always include them, as they are the key for linking to other drawings.

7. **Fire compartment boundaries:** always note fire walls/barriers shown on the drawing, as pipe penetrations through them require fire seals.

8. **Control sequences:** for control diagrams, describe the SEQUENCE of actions (detection -> delay -> alarm -> suppression), not just individual elements.

## Typical description errors (what to avoid)

- "The plan shows fire hydrants on each floor" -- No quantities, no labels, no riser references
- "Gas suppression system with cylinders" -- No ГОТВ type, no cylinder count, no pressure
- "Pump station with fire pumps" -- No characteristics Q, H, N, no make/type, no redundancy info

+ "Ст.В2-1: Ду65 steel VGP, from elev. -2.800 to +27.600, at axes А-3. Hydrant ПК-1 on floor 1 in ШПК-310 cabinet, hose 20 m, nozzle РС-50. Gate valve Ду65 at basement level with electric actuator." -- All elements are specific, can be verified
