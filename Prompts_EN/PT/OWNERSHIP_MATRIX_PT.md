# Inspection Ownership Matrix (section PT)

Each inspection has ONE owner. Other agents DO NOT duplicate this inspection.

| Inspection | Sole Owner |
|-----------|------------|
| Fire hydrant riser diameters (B2/B21), locations, spacing ≤20 m | pt_water_supply |
| Fire hydrant cabinets (ШПК): type, hose length 20 m, nozzle РС-50/РСК-50 | pt_water_supply |
| Pressure at fire hydrant (≥0.4 MPa for compact jet ≥6 m) | pt_water_supply |
| Fire pumps for ВПВ: duty + standby, auto-start from АПС | pt_water_supply |
| Check valves, drain valves, test valves on ВПВ | pt_water_supply |
| Connection to domestic water supply via check valve | pt_water_supply |
| Sprinkler/drencher systems (B21): riser layout, control valves | pt_water_supply |
| Fire compartment isolation: separate risers per fire compartment | pt_water_supply |
| Pump station room: drainage, ventilation, access | pt_water_supply |
| Motorized valves on ВПВ risers (interlocking with АПС) | pt_water_supply |
| | |
| ГОТВ type selection (Halon 125/227ea, Inergen, CO2, powder) | pt_gas_powder |
| ГОТВ mass calculation (extinguishing concentration, room volume, leakage) | pt_gas_powder |
| Cylinder storage: quantity, pressure, station room | pt_gas_powder |
| Pipeline routing: diameters, pressure losses, delivery time ≤10 s (gas) / ≤30 s (powder) | pt_gas_powder |
| Nozzles/distributors: type, count, coverage area | pt_gas_powder |
| Electrical control: start/stop buttons, 30 s delay, warning signs | pt_gas_powder |
| Interlocks: ventilation shutdown, damper closure, door closure | pt_gas_powder |
| Warning signs and signals ("GAS — LEAVE", "GAS — DO NOT ENTER") | pt_gas_powder |
| Automatic / manual / local start modes | pt_gas_powder |
| Room tightness requirement (leakage ≤0.001 m2/m3 for gas) | pt_gas_powder |
| | |
| ВПВ hydraulic calculation (Darcy-Weisbach losses, Q, P at dictating hydrant) | pt_hydraulics |
| Sprinkler system calculation (irrigation intensity per СП 485) | pt_hydraulics |
| Pump selection verification (Q-H curve, operating point, NPSH) | pt_hydraulics |
| Fire water tank volume (10-minute reserve for ВПВ) | pt_hydraulics |
| Specification arithmetic (pipe lengths, fitting counts, equipment vs drawings) | pt_hydraulics |
| Pipe material verification (steel VGP / electrowelded, connections) | pt_hydraulics |
| ГОТВ mass recalculation (concentration × volume × correction factors) | pt_hydraulics |
| | |
| Currency of СП 10.13130, СП 485.1311500, СП 486.1311500 | pt_norms |
| Currency of ФЗ №123-ФЗ, ГОСТ Р 51052, ГОСТ 53325 | pt_norms |
| Content of norm clauses (per norms_paragraphs) | pt_norms |
| Completeness of the normative base for section PT | pt_norms |
| Hierarchy of normative references (ФЗ > ТР > СП > ГОСТ) | pt_norms |
| | |
| Sheet inventory (register vs actual presence) | pt_drawings |
| Discrepancies: system diagram vs floor plan (hydrant/sprinkler count, pipe diameters) | pt_drawings |
| Discrepancies: specification vs plans (quantities of equipment and materials) | pt_drawings |
| Title blocks and formatting | pt_drawings |
| Legend symbols and notation consistency | pt_drawings |
| Riser/pipeline labeling consistency across sheets | pt_drawings |
