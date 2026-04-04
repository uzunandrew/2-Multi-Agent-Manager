# Instructions for vision model: structured description of low-voltage system drawings

You receive a PNG image from project documentation for low-voltage systems (SS section). Your task is to describe it in a STRUCTURED way so that the technical content can be reconstructed from the description without viewing the image.

## Scope and limitations

**7 types of low-voltage system drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|------------|
| Structural diagrams | 25% | APS loops, SKUD topology, CCTV tree, ASKUE collection |
| Floor plans with devices | 30% | Detector/camera/reader/speaker placement on floor plans |
| Electrical schematics | 10% | PPKP connection, controller wiring, power supply circuits |
| Connection diagrams | 10% | Terminal block wiring, device-to-controller connections |
| Cable route plans | 10% | Low-voltage tray routes, riser diagrams |
| Tables and legends | 10% | Specifications, cable journals, symbol legends |
| Functional automation diagrams | 5% | Sensor-controller-actuator logic, ASUD diagrams |

**What NOT to describe (this data is already in document.md):**
- Title blocks, title inscriptions (sheet number, cipher, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type** identify the type and apply the corresponding description format below.

## Principle of reading

Low-voltage systems are read from controller to field device: for fire alarm — PPKP → address loop → detector/module; for SKUD — controller → reader → lock; for CCTV — camera → switch → NVR/server. Each device chain must be described as one connected entry: controller → cable → field device, preserving address/channel assignment.

## Description format: STRUCTURAL DIAGRAM (APS / SOUE)

```
STRUCTURAL DIAGRAM: [name, e.g., "Structural diagram of fire alarm system"]

PPKP (FIRE ALARM CONTROL PANEL):
- Type: [model, e.g., "Bolid S2000-M"]
- Location: [room, floor]
- Address capacity: [number of addressable devices]
- Number of loops: [N]

LOOPS:
Loop 1 (AL1):
  - Controller: [e.g., "S2000-KDL" or "Rubezh R3-KAU"]
  - Devices on loop:
    - Smoke detectors: [type, quantity, e.g., "DIP-34A x 48"]
    - Heat detectors: [type, quantity]
    - Manual call points: [type, quantity, e.g., "IPR 513-3A x 6"]
    - Short-circuit isolators: [type, quantity, locations]
    - Input/output modules: [type, quantity, purpose]
  - Floors covered: [1-5, basement, etc.]

Loop 2 (AL2):
  ...

SOUE (NOTIFICATION SYSTEM):
- Type: [1-5]
- Control unit: [model]
- Sound notification:
  - Sirens: [type, quantity, location zones]
  - Sound pressure: [dBA at distance]
- Light notification:
  - "EXIT" signs: [type, quantity]
  - Direction indicators: [type, quantity]
  - Flashing beacons: [type, quantity]

INTEGRATION:
- Ventilation shutdown: [signal type, target system]
- Smoke extraction start: [signal type, target system]
- Elevator recall: [signal type, target system]
- SKUD unlock: [signal type, target system]
- Fire department retransmission: [method, device]

POWER SUPPLY:
- Main: [source, cable]
- Backup: [UPS/battery, capacity Ah, autonomy hours]
```

## Description format: STRUCTURAL DIAGRAM (SKUD / SOT / SDS)

```
STRUCTURAL DIAGRAM: [name, e.g., "Structural diagram of access control system"]

SERVER / HEAD-END:
- Server: [model, software]
- Network switch: [model, ports]
- Location: [room]

CONTROLLERS:
Controller 1:
  - Type: [model, e.g., "PERCo CT/L04"]
  - Location: [floor, room]
  - Doors controlled: [quantity, list]
  - Readers per door: [1 or 2, type]
  - Lock type: [electromagnetic/electromechanical, model, holding force N]
  - Exit button: [type]
  - Connection: [Ethernet/RS-485, to which switch/controller]

Controller 2:
  ...

CAMERAS (for SOT):
Camera group [zone name]:
  - Camera type: [model, e.g., "DS-2CD2143G2-IS"]
  - Resolution: [MP]
  - Lens: [mm, viewing angle]
  - IR range: [m]
  - Quantity: [N]
  - PoE switch: [model, ports]

STORAGE:
- NVR/Server: [model]
- HDD: [total TB]
- Retention period: [days]
- Recording mode: [continuous/motion/schedule]

INTERCOM (for SDS):
- Call panels: [type, quantity, locations]
- Apartment stations: [type, per apartment]
- Concierge monitor: [type, quantity]
- Connection: [IP/2-wire/4-wire]
```

## Description format: STRUCTURAL DIAGRAM (AUTOMATION / DISPATCHING)

```
STRUCTURAL DIAGRAM: [name, e.g., "Structural diagram of building automation"]

DISPATCHING CENTER:
- AWP (workstation): [quantity, location]
- Server: [model, software platform]
- Network: [topology, switches]

CONTROLLERS:
Controller [name/designation]:
  - Type: [model, e.g., "Schneider M340" or "Bolid S2000-PP"]
  - Location: [floor, room]
  - Protocol: [Modbus RTU/TCP, BACnet, LonWorks]
  - I/O modules:
    - DI (digital inputs): [quantity, purpose]
    - DO (digital outputs): [quantity, purpose]
    - AI (analog inputs): [quantity, purpose]
    - AO (analog outputs): [quantity, purpose]
  - Connected subsystems: [list]

FIELD DEVICES:
- Temperature sensors: [type, quantity, locations]
- Pressure sensors: [type, quantity, locations]
- Level sensors: [type, quantity, locations]
- Leak sensors: [type, quantity, locations]
- Valves/actuators: [type, quantity, purpose]
- Frequency drives: [controlled equipment]

COMMUNICATION:
- Backbone: [Ethernet/RS-485/fiber]
- Field bus: [Modbus/BACnet/proprietary]
- Redundancy: [ring/star/none]
```

## Description format: FLOOR PLAN WITH DEVICES

```
PLAN: [name, e.g., "Floor plan 1st floor - fire alarm"]
SCALE: [if specified]
SUBSYSTEM: [APS/SOT/SKUD/SOUE/etc.]

ROOMS:
- Room 101 - entrance hall
- Room 102 - corridor
- Room 103 - apartment 1
[list all rooms with numbers and designations]

DEVICES ON PLAN:
Room 101 (entrance hall):
  - Smoke detector DIP-34A: 2 pcs, ceiling mount
  - Manual call point IPR 513-3A: 1 pc, at exit, h=1.5m
  - Siren Sonat-K: 1 pc, h=2.3m
  - "EXIT" sign: 1 pc, above door

Room 102 (corridor):
  - Smoke detector DIP-34A: 3 pcs, spacing ~8m
  - Camera DS-2CD2143G2: 1 pc, at corridor end
  - SKUD reader: 1 pc, at door to stairwell
  ...

CABLE ROUTES ON PLAN:
- From shield ShPS (room 001) to corridor: tray 100x50 at +3.000
- Along corridor: tray 100x50 at +2.900, branching to rooms
- Fire-rated cable: KPSng(A)-FRLS 2x2x0.5 [routes marked]
- Low-voltage: UTP Cat.6 [routes marked]

RISER (if shown):
- Vertical shaft location: [axis reference]
- Cables in riser: [list]
- Floor taps: [at each floor / selective]
```

## Description format: CONNECTION / WIRING DIAGRAM

```
WIRING DIAGRAM: [name, e.g., "Connection diagram of PPKP panel"]

PANEL / DEVICE: [designation, model]

TERMINALS:
Terminal block XT1 (power):
  - 1: L (phase from UPS)
  - 2: N (neutral)
  - 3: PE (ground)

Terminal block XT2 (addressable loop 1):
  - 1: AL1+ (loop 1 positive)
  - 2: AL1- (loop 1 negative)

Terminal block XT3 (relay outputs):
  - 1-2: Relay 1 (ventilation shutdown, NO contact)
  - 3-4: Relay 2 (smoke extraction start, NO contact)
  - 5-6: Relay 3 (elevator recall, NO contact)
  - 7-8: Relay 4 (SKUD unlock, NO contact)

CABLES:
- To loop 1: KPSng(A)-FRLS 1x2x0.75, L=...
- To relay ventilation: KPSng(A)-FRHF 2x2x0.5, L=...
- Power: PPGng(A)-HF 3x2.5, L=...
[list ALL cables with types and destinations]

EXTERNAL CONNECTIONS:
- RS-485 to dispatcher: cable [type], to device [name]
- Ethernet to server: UTP Cat.6, to switch [name]
```

## Description format: CABLE ROUTE PLAN / RISER DIAGRAM

```
CABLE ROUTES: [name, e.g., "Low-voltage cable route plan, basement"]

TRAYS AND STRUCTURES:
- Tray 1: perforated 100x50mm, bottom elevation +2.900, route [from-to]
- Tray 2: mesh 200x50mm, bottom elevation +3.100, route [from-to]
- Fire-rated enclosure: [type, EI rating], route [from-to]
- Conduit: PVC d=20mm, [for specific cables]

SEPARATION FROM POWER:
- Distance to power trays: [mm]
- Partition: [if present, type]

RISER:
Floor connections (bottom to top):
  - Basement: ShPS, ShSS, server room
  - 1st floor: tap to corridor, [N] cables
  - 2nd floor: tap to corridor, [N] cables
  ...
  - Roof: antenna equipment, lightning protection

PENETRATIONS:
- Through floor [N]: sleeve package [size], fire sealing [type]
- Through wall [room-to-room]: sleeve [size], fire sealing [type]
```

## Description format: TABLE / LEGEND

```
TABLE: [name, e.g., "Cable journal" / "Equipment specification" / "Legend"]

CONTENT:
[reproduce the table in text format, preserving structure]

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| value    | value    | value    |
```

For symbol legends:
```
LEGEND:
- [symbol] - Smoke detector
- [symbol] - Heat detector
- [symbol] - Manual call point
- [symbol] - Siren
- [symbol] - "EXIT" sign
- [symbol] - CCTV camera
- [symbol] - SKUD reader
- [symbol] - Intercom call panel
[list all symbols]
```

## Description format: FUNCTIONAL AUTOMATION DIAGRAM

```
FUNCTIONAL DIAGRAM: [name, e.g., "Functional diagram of pump station automation"]

CONTROLLED OBJECT: [pump, valve, fan, etc.]

SENSORS (inputs):
- [designation] [type]: [parameter measured], range [min-max], output [4-20mA/discrete]
- TE1 (temperature sensor): water temperature, 0-100C, 4-20mA
- PT1 (pressure transmitter): discharge pressure, 0-16 bar, 4-20mA
- LS1 (level switch): dry-run protection, discrete NO

ACTUATORS (outputs):
- [designation] [type]: [controlled parameter]
- M1 (pump motor): via VFD, 0-50Hz
- KV1 (solenoid valve): on/off, 24VDC

CONTROLLER:
- Type: [model]
- Algorithm: [PID/on-off/cascade/sequence]
- Setpoints: [listed values]

INTERLOCKS:
- [condition] -> [action]
- LS1 = LOW -> M1 STOP (dry-run protection)
- PT1 > 12 bar -> M1 STOP (overpressure protection)
- Fire signal -> KV1 CLOSE
```

## Rules

1. **Main rule:** for each device/sensor on the diagram, capture: designation, type/model, location, connection (to which controller/loop/switch), cable type.

2. **If the diagram has multiple subsystems** (e.g., APS + SOUE on one sheet) — describe each subsystem separately with clear headers.

3. **If a parameter is unreadable** on the image — write "unreadable" instead of guessing.

4. **Device counts:** always count and state the total number of each device type. This is critical for cross-checking with specifications.

5. **Cable types matter:** for fire alarm, the cable type (FR/FRLS/FRHF) is a critical parameter. Always capture it.

6. **Address/zone allocation:** if devices have addresses or zone numbers visible — capture them. This is needed for loop capacity verification.

## Typical description errors (what to avoid)

X **Bad:** "The diagram shows a fire alarm system with smoke detectors and sirens."
-> No specifics, no quantities, no connections

X **Bad:** "PPKP has several loops connected to detectors on different floors."
-> "Several" and "different" are useless — state exact numbers

V **Good:** "Loop 1 (S2000-KDL): 47 smoke detectors DIP-34A + 6 manual call points IPR 513-3A + 4 short-circuit isolators B2R-KDL, floors 1-5. Loop 2: ..."
-> Exact counts, types, floor allocation
