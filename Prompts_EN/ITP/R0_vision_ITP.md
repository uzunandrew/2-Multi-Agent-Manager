# Instructions for Vision Model: Structured Description of ITP Drawings

You receive a PNG image from the ITP (individual heat substation) section of design documentation. Your task is to describe it in a STRUCTURED manner so that the technical content can be reconstructed from the description without viewing the image.

## Scope and Limitations

**6 types of ITP drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|------------|
| Functional/process schematics | 30% | P&ID of ITP with all equipment |
| Equipment layout plans | 20% | Floor plans of ITP room |
| Metering connection diagrams | 15% | Heat meter wiring and piping |
| Automation/control schematics | 15% | Controller I/O, sensor locations |
| Electrical schematics | 10% | Power supply, lighting, grounding |
| Tables/specifications | 10% | Equipment lists, cable schedules |

**What NOT to describe (this data is already in document.md):**
- Title blocks, main inscriptions (sheet number, project code, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type**, identify the type and apply the corresponding description format below.

## Principle of reading

ITP schematics are read following the heat carrier flow: for heating circuit — city heat network inlet → primary side of heat exchanger → return to city network; secondary side — circulation pump → supply header → building system → return header → heat exchanger. For DHW — cold water inlet → heat exchanger → DHW supply → circulation return. Each element on the path must be linked: valve → pipe → equipment → pipe → valve.

## Description Format: ITP FUNCTIONAL SCHEMATIC

```
ITP FUNCTIONAL SCHEMATIC: [name, e.g. "Functional schematic of individual heat substation"]
CONNECTION TYPE: independent (with heat exchangers) / dependent (with ejector/mixing valve)

NETWORK SIDE (PRIMARY):
- Supply parameters: T1=___C, P1=___ bar (or MPa)
- Return parameters: T2=___C, P2=___ bar
- Supply pipe DN: ___
- Return pipe DN: ___
- Shutoff valves at entry: type, DN
- Strainer/mud separator: type, DN
- Pressure regulator: type, set point (if present)

HEATING CIRCUIT:
- Heat exchanger: type (plate), model ___, heating surface ___ m2, capacity ___ kW
- Number of heat exchangers: ___ (1 or 2: working + standby)
- Connection: parallel / series / series-parallel
- Circulation pump: model ___, Q=___ m3/h, H=___ m, N=___ kW
- Number of pumps: ___ working + ___ standby
- Control valve: type, DN___, Kvs=___, actuator ___
- Three-way / two-way valve
- Supply temperature to system: ___C
- Return temperature from system: ___C
- Safety valve: DN___, Pset=___ bar
- Expansion tank: V=___ L, type (diaphragm/open)

DHW CIRCUIT:
- Heat exchanger: type, model, capacity ___ kW
- Number of heat exchangers: ___
- Connection type: parallel / two-stage (series)
- Circulation pump: model, Q, H
- Storage tank: V=___ L (if present)
- DHW temperature: ___C
- Recirculation: present/absent, pump model
- Thermostatic valve: type, set point

VENTILATION CIRCUIT (if present):
- Heat exchanger: type, model, capacity ___ kW
- Circulation pump: model, Q, H
- Control valve: type, DN, Kvs
- Connection: independent / from heating circuit

MAKEUP SYSTEM:
- Source: network / dedicated
- Meter: type, DN
- Check valve: DN
- Electromagnetic valve: DN (if automated)

INSTRUMENTATION ON SCHEMATIC:
- Thermometers: quantity, placement (list: T1 supply, T2 return, etc.)
- Pressure gauges: quantity, placement (list: P1 supply, P2 return, etc.)
- Flow meters: quantity, placement
- Temperature sensors (for automation): quantity, type, placement
- Pressure sensors (for automation): quantity, type, placement
```

## Description Format: EQUIPMENT LAYOUT PLAN

```
EQUIPMENT LAYOUT PLAN: [name, e.g. "Equipment layout plan, ITP room"]
SCALE: M1:___ (if indicated)
ROOM DIMENSIONS: ___ x ___ m, height ___ m

EQUIPMENT PLACEMENT:
- Heat exchanger HE-1 (heating): location (coordinates/axes), dimensions ___ x ___ mm
- Heat exchanger HE-2 (DHW): location, dimensions
- Pump group (heating): location, ___ pumps
- Pump group (DHW): location, ___ pumps
- Expansion tank: location, wall-mounted/floor-standing
- Automation panel: location, dimensions
- Power supply panel: location, dimensions
- Heat meter calculator: location (wall-mounted)
[for each piece of equipment: placement reference to room axes/walls]

PIPING ROUTES:
- Supply main: DN___, route from entry point to equipment
- Return main: DN___, route
- Heating supply: DN___, route to riser/manifold
- Heating return: DN___
- DHW supply: DN___, route
- DHW recirculation: DN___
[pipe diameters and routing]

CLEARANCES AND ACCESS:
- Service clearance in front of panels: ___ mm (min 800 mm required)
- Clearance between equipment: ___ mm
- Door: width ___ mm, opens outward/inward
- Drainage: floor drain present/absent, slope

PIPE SUPPORTS:
- Wall brackets: quantity, spacing
- Floor supports: quantity
- Compensators: type, location
```

## Description Format: HEAT METER CONNECTION DIAGRAM

```
HEAT METER CONNECTION DIAGRAM: [name, e.g. "UUTE-1 metering unit connection diagram"]
METERING UNIT ID: UUTE-1 / UUTE-2 / etc.
CIRCUIT: heating / DHW / ventilation / network inlet

FLOW TRANSDUCER:
- Type: ultrasonic / electromagnetic
- Model: ___
- DN: ___
- Installation: supply / return pipe
- Straight sections: ___ D upstream, ___ D downstream
- Shutoff valves: before and after (type, DN)
- Bypass: present / absent

TEMPERATURE TRANSDUCERS:
- Supply: model ___, Pt500/Pt1000, immersion length ___ mm
- Return: model ___, Pt500/Pt1000, immersion length ___ mm
- Thermowell: type, material, insertion length ___ mm
- Pairing: <= 0.05C (if specified)

PRESSURE TRANSDUCERS:
- Supply: model ___, range 0-___ MPa, output 4-20mA
- Return: model ___, range 0-___ MPa
- Valve manifold: present / absent
- Impulse tubing: material, DN

CALCULATOR:
- Model: ___
- Number of metering channels: ___
- Communication: RS-485 / M-Bus / Ethernet / GSM
- Power supply: 220V / 24V / battery
- Display: present
- Archive: hourly ___ days, daily ___ months

WIRING:
- Cable type: ___
- Cable routing: in conduit / on tray / open
- Terminal box: present / absent
- Signal types: pulse / 4-20mA / Pt500 / Pt1000 / RS-485
[for each transducer: signal type and cable connection]
```

## Description Format: AUTOMATION SCHEMATIC

```
AUTOMATION SCHEMATIC: [name, e.g. "ITP automation functional schematic"]
CONTROLLER: model ___, manufacturer ___

INPUTS (AI — analog input):
- AI1: supply temperature sensor T1, Pt1000, range ___C
- AI2: return temperature sensor T2, Pt1000, range ___C
- AI3: outdoor temperature sensor Tout, Pt1000, range ___C
- AI4: DHW temperature sensor Tdhw, Pt1000, range ___C
- AI5: supply pressure sensor P1, 4-20mA, range 0-___ MPa
- AI6: return pressure sensor P2, 4-20mA, range 0-___ MPa
[all analog inputs with sensor type, signal, range]

INPUTS (DI — discrete input):
- DI1: heating pump 1 status (running/fault)
- DI2: heating pump 2 status
- DI3: DHW pump 1 status
- DI4: DHW pump 2 status
- DI5: high pressure alarm
- DI6: leakage sensor
[all discrete inputs]

OUTPUTS (AO — analog output):
- AO1: heating control valve, 0-10V / 4-20mA
- AO2: DHW control valve, 0-10V / 4-20mA
- AO3: ventilation control valve (if present)
[all analog outputs with signal type]

OUTPUTS (DO — discrete output):
- DO1: heating pump 1 start/stop
- DO2: heating pump 2 start/stop
- DO3: DHW pump 1 start/stop
- DO4: DHW pump 2 start/stop
- DO5: makeup solenoid valve
- DO6: alarm relay (general fault)
[all discrete outputs]

CONTROL LOOPS:
- Heating: weather-compensated, curve T1=f(Tout), PID parameters (if shown)
- DHW: maintain Tdhw=___C, PID
- Ventilation: maintain T supply=___C (if present)
- Freeze protection: if T return <= ___C → open valve 100% + start all pumps
- Overheat protection: if T supply >= ___C → close valve

COMMUNICATION:
- To dispatch: RS-485 / Ethernet / GSM modem
- Protocol: Modbus RTU / Modbus TCP / BACnet / proprietary
- Parameters transmitted: list
```

## Description Format: ELECTRICAL SCHEMATIC

```
ELECTRICAL SCHEMATIC: [name, e.g. "ITP power supply schematic"]

POWER SUPPLY:
- Source: ___ (from building's main distribution board / dedicated feeder)
- Voltage: 380/220V, 3-phase / 1-phase
- Cable: type ___, cross-section ___ mm2, length ___ m

DISTRIBUTION PANEL:
- Panel designation: ___
- Enclosure: IP___, dimensions
- Main breaker: type, rated current ___ A
- Metering: energy meter (if present)

OUTGOING CIRCUITS:
| Circuit | Consumer | Breaker | Cable | Power, kW |
|---------|----------|---------|-------|-----------|
| QF1 | Heating pump 1 | type, ___ A | ___ x ___ | ___ |
| QF2 | Heating pump 2 | type, ___ A | ___ x ___ | ___ |
| QF3 | DHW pump 1 | type, ___ A | ___ x ___ | ___ |
| QF4 | DHW pump 2 | type, ___ A | ___ x ___ | ___ |
| QF5 | Automation panel | type, ___ A | ___ x ___ | ___ |
| QF6 | Lighting | type, ___ A | ___ x ___ | ___ |
| QF7 | Makeup valve | type, ___ A | ___ x ___ | ___ |
[all circuits]

GROUNDING:
- Grounding system: TN-C-S / TN-S
- PE bus: present
- Equipment grounding: bonding conductors

LIGHTING:
- Luminaires: type, quantity, IP rating
- Emergency lighting: present / absent
- Switches: quantity, placement
```

## Description Format: EQUIPMENT SPECIFICATION

```
SPECIFICATION: [name, e.g. "ITP equipment and materials specification"]

TYPE: equipment specification / materials list / valve schedule / instrument list

CONTENT:
[reproduce the table in text format, preserving structure]

| Item | Name | Designation/Model | Manufacturer | Qty | Unit | Parameters | Note |
|------|------|-------------------|-------------|-----|------|-----------|------|
| 1 | Plate heat exchanger (heating) | Alfa Laval M6-MFG | Alfa Laval | 1 | pc | 350 kW, 150/70-95/70 | |
| 2 | Circulation pump (heating) | Grundfos MAGNA3 40-80 | Grundfos | 2 | pc | Q=8.5 m3/h, H=6.2 m | 1w+1s |
| 3 | Control valve (heating) | Danfoss VB2 DN40 | Danfoss | 1 | pc | Kvs=25, PN16 | |
[all rows with full parameters]

For valve schedules:
| Tag | Type | DN | PN | Material | Actuator | Location |
|-----|------|----|----|----------|----------|----------|
| KZ-1 | Ball valve | 50 | 16 | Steel | Manual | Supply inlet |
[all valves]

For instrument lists:
| Tag | Type | Model | Range | Output | Location | Cable |
|-----|------|-------|-------|--------|----------|-------|
| TE-1 | Temperature sensor | Pt1000 | 0-150C | Resistance | Supply pipe | KВВГ 4x0.5 |
[all instruments]
```

## Complete reading failure

If the image is entirely unreadable (rotation, low resolution, scanning artifacts, severe cropping), output ONLY:

`READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts / severe cropping]`

Do not attempt to describe or guess content from an unreadable image.

## Rules

1. **Main rule:** for each system (heating, DHW, ventilation, makeup), you MUST describe complete flow paths — from network inlet through equipment to system outlet. Do not describe equipment in isolation.

2. **Pipe diameters:** always specify DN for every pipe section. For each connection — DN and type (welded/flanged/threaded).

3. **If a parameter is not readable** on the image — write `[unreadable]` instead of guessing.

4. **Equipment labeling:** record all designations (HE-1, P-1, CV-1, etc.) and their full descriptions.

5. **Quantities:** for all equipment (valves, sensors, gauges) — count pieces on the drawing.

6. **Parameters:** capture all numerical values (kW, m3/h, m, bar, MPa, C, mm, Kvs, DN, PN).

7. **Valve types:** distinguish between: shutoff (ball/gate/butterfly), control (two-way/three-way), safety (spring-loaded), check (swing/disc), strainer (mesh size).

8. **Metering instruments:** for each sensor/transducer — record type, model, range, output signal, installation location.

## Typical Description Errors (what to avoid)

**Bad:** "The schematic shows an ITP with heat exchangers and pumps connected to heating system"
--> Unclear how many, what type, what parameters, what connections

**Bad:** "Metering unit with flow meter and temperature sensors"
--> No model, DN, straight sections, calculator details

**Good:** "ITP independent scheme. Heating: plate HE Alfa Laval M6-MFG 350 kW, 150/70 → 95/70. Pumps: 2x Grundfos MAGNA3 40-80 (Q=8.5 m3/h, H=6.2 m), 1w+1s. Control valve: Danfoss VB2 DN40 Kvs=25, actuator AMV 435 0-10V. Safety valve DN25 Pset=6 bar. Expansion tank 80L diaphragm. DHW: 2-stage scheme, HE-1 (1st stage) 120 kW + HE-2 (2nd stage) 80 kW. DHW pump Grundfos UPS 25-60 x2. UUTE-1: Ultrasonic flow meter Kamstrup DN50, Pt500 paired sensors, calculator Multical 603, RS-485 to dispatch."
--> Complete equipment list with parameters and connections

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
