# Check Ownership Matrix

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|------------|
| Separation of mutually redundant lines | fire_safety |
| FR/FRLS/FRHF — cable fire resistance for СПЗ | fire_safety |
| EI45/EI60/EI150 — required fire resistance rating | fire_safety |
| ПЭСПЗ / "Пожар" mode on the diagram | fire_safety |
| Emergency lighting, "ВЫХОД" signs, autonomy ≥3h | fire_safety |
| Smoke extraction, air pressurization, activation from ОПС | fire_safety |
| Working/emergency lighting on separate cable trays | fire_safety |
| Room categories, IP rating by category | fire_safety |
| Cable penetrations through fire barriers | fire_safety |
| | |
| Cable cross-sections by permissible current | cables |
| Breaker ↔ cable coordination (Iном ≤ Iдоп) | cables |
| B/C/D characteristics of residential breakers | cables |
| Breaking capacity (Ics ≥ Iкз) | cables |
| Voltage drop (total ≤ 5%) | cables |
| Cable mark consistency (text = diagram = specification) | cables |
| Economic current density | cables |
| | |
| Cable tray fill rate (≤ 40%) | cable_routes |
| Cable tray sizes (plan vs specification) | cable_routes |
| Mounting assemblies (threaded rods, bottom elevations) | cable_routes |
| Fire-rated enclosure design (dimensions, thickness, ventilation grilles) | cable_routes |
| Co-routing of power + low-voltage cables | cable_routes |
| | |
| Load table arithmetic (Pу, Pр, Sр, Iр) | tables |
| Summary totals, Ко, Кн.макс | tables |
| Coefficients (Кс, cosφ) — as reference values | tables |
| CT table arithmetic (formula recalculation) | tables |
| Specification: breakers, CTs, meters, cables, panels (quantity vs diagram) | tables |
| | |
| Discrepancies between text ↔ diagram ↔ plan (factual) | drawings |
| Sheet inventory (table of contents vs actual sheets) | drawings |
| Title blocks and formatting | drawings |
| Legend symbols | drawings |
| Layout (clearances, dimensions) | drawings |
| | |
| Regulatory reference currency (status per norms_db) | norms |
| Norm clause content (per norms_paragraphs) | norms |
| ПУЭ without parallel СП | norms |
| Completeness of the regulatory base | norms |
| | |
| CT selection (Ктт, accuracy class, justification) | metering |
| Meters (model, interface, АСКУЭ compatibility) | metering |
| ИКК (presence, connection diagram) | metering |
| Metering points (commercial / technical) | metering |
| | |
| Luminaire IP rating by operating conditions | lighting |
| Lighting power balance | lighting |
| DALI: controllers, power supplies, ≤64 per line | lighting |
| Illuminance standards (lux) | lighting |
| Luminaire specification | lighting |
| | |
| Control logic (scenarios, SA/K/KM) | automation |
| Interface with АСУД (XT1/XT2, terminal blocks) | automation |
| Astronomical relays, timers | automation |
| АВР for lighting panels | automation |
| | |
| TN-C-S, PEN splitting point | grounding |
| ГЗШ and connections to it | grounding |
| Equipotential bonding (ОСУП, ДСУП, КУП) | grounding |
| Lightning protection (air terminals, down conductors) | grounding |
| PE conductors (cross-sections) | grounding |
| | |
| Electric motors (starting, protection) | power_equipment |
| Power distribution panels (ЩР, ШР) | power_equipment |
| Socket networks (УЗО 30mA) | power_equipment |
| Cable heating (power, thermostat, УЗО) | power_equipment |
| Variable frequency drives | power_equipment |
| Interlocks with process equipment (pumps, general ventilation) | power_equipment |
| | |
| Cable burial depth in trenches | outdoor_install |
| Distances from utilities | outdoor_install |
| Conduits under roads | outdoor_install |
| Earthwork volumes (arithmetic) | outdoor_install |
