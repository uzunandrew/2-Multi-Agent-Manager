# Check Ownership Matrix (Section ITP — Individual Heat Substations)

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|-----------|
| Heat exchangers: type (plate/shell-and-tube), heating surface margin, parameters | itp_thermal |
| Circulation pumps: Q-H selection, operating point, redundancy (1+1) | itp_thermal |
| Control valves: Kvs, valve authority >=0.3, actuator type | itp_thermal |
| Shutoff valves: type (ball/gate/butterfly), PN/DN match to system parameters | itp_thermal |
| Strainers, mud separators, filters: DN, mesh size, placement | itp_thermal |
| Safety valves: set pressure Pset = 1.25 x Pwork | itp_thermal |
| Expansion tanks: type (diaphragm), volume = 0.04 x Vsystem | itp_thermal |
| Piping: material (steel/PPR/PE-Xa), diameters, velocity check | itp_thermal |
| Thermal insulation: thickness per SP 61.13330 | itp_thermal |
| Compensators: type, placement at fixed points | itp_thermal |
| Pressure regulators: type, set point, placement | itp_thermal |
| Makeup water system: connection, meter, check valve | itp_thermal |
| | |
| Heat meters: type (ultrasonic/electromagnetic), accuracy class, dynamic range | itp_metering |
| Flow transducers: straight sections (5D upstream / 3D downstream), DN selection by Vmax | itp_metering |
| Temperature transducers: Pt500/Pt1000, pairing <=0.05C, immersion length | itp_metering |
| Pressure transducers: accuracy class 0.5%, range | itp_metering |
| Heat calculator: channels, communication protocol (RS-485/M-Bus), archive depth | itp_metering |
| Metering unit mounting diagrams: thermowells, pockets, installation locations | itp_metering |
| Metering unit electrical wiring diagrams | itp_metering |
| Gmin/Gt/Gmax flow range verification | itp_metering |
| DN selection for heat meter by Vmax <= 3 m/s | itp_metering |
| | |
| Controllers: type, I/O count (AI/AO/DI/DO), communication protocol | itp_automation |
| Weather-compensated control: temperature curve T1/T2=f(Tout), PID | itp_automation |
| Freeze protection: return water <=5C, algorithm | itp_automation |
| Overheat protection: supply water limit, algorithm | itp_automation |
| Temperature sensors: Pt1000, 4-20mA, placement | itp_automation |
| Pressure sensors: range, output signal, placement | itp_automation |
| Actuators: control valves, stroke/full stroke time, spring return | itp_automation |
| Automation panels: layout, labeling, DIN-rail equipment | itp_automation |
| Dispatch system: communication (RS-485/Ethernet/GSM), monitored parameters | itp_automation |
| Alarm signals: list, priorities, transmission method | itp_automation |
| Interlock logic: pump-valve, pump-pump sequencing | itp_automation |
| | |
| Currency of regulatory references (status per norms_db) | itp_norms |
| Content of norm paragraphs (per norms_paragraphs) | itp_norms |
| SP 124.13330 — heat supply networks | itp_norms |
| SP 60.13330 — heating, ventilation, air conditioning | itp_norms |
| SP 61.13330 — thermal insulation of pipelines | itp_norms |
| FZ No.261-FZ — energy conservation | itp_norms |
| FZ No.102-FZ — ensuring measurement uniformity | itp_norms |
| PP RF No.1034 — commercial heat metering rules | itp_norms |
| GOST R 8.592 — heat meters | itp_norms |
| MDS 41-4.2000 — recommendations for ITP design | itp_norms |
| Completeness of regulatory framework for ITP section | itp_norms |
| | |
| Discrepancies between functional schematic ↔ equipment layout plan | itp_drawings |
| Discrepancies between functional schematic ↔ specification (types/quantities) | itp_drawings |
| Discrepancies between metering connection diagram ↔ functional schematic | itp_drawings |
| Discrepancies between automation schematic ↔ functional schematic | itp_drawings |
| Discrepancies between electrical schematic ↔ specification | itp_drawings |
| Sheet inventory (drawing register vs actual sheets) | itp_drawings |
| Title blocks and formatting (GOST R 21.101) | itp_drawings |
| Legend/symbols (presence of explanations) | itp_drawings |
| System and equipment labeling consistency across sheets | itp_drawings |
| DN of pipelines: schematic vs plan vs specification | itp_drawings |
| Instrument count: automation schematic vs specification | itp_drawings |
