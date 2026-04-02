# Check Ownership Matrix (Section OV — Heating, Ventilation, and Air Conditioning)

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|-----------|
| Radiators: type, model, capacity, number of sections/panels | heating |
| Convectors: type, capacity, placement | heating |
| Underfloor heating: pipe spacing, circuit lengths, pipe, manifolds | heating |
| ИТП (individual heat substation): schematic, pumps, heat exchangers, control | heating |
| Coolant temperature schedule | heating |
| Balancing valves: presetting, Kvs, size | heating |
| Room heat losses vs radiator capacity | heating |
| АОВ (air-heating units): capacity, airflow | heating |
| Towel warmers: type, connection | heating |
| | |
| Supply air handling units: airflow, pressure, capacity, sections | ventilation |
| Exhaust units and fans: airflow, pressure | ventilation |
| Ductwork: cross-section, material, air velocity ≤6 m/s | ventilation |
| Heat recovery: type, efficiency, bypass | ventilation |
| Sound attenuators: size, placement | ventilation |
| Air distribution devices: grilles, diffusers, type, airflow | ventilation |
| Control dampers: type, size | ventilation |
| Air heater piping: pump, three-way valve, controls | ventilation |
| Air balance: supply vs exhaust per room and building | ventilation |
| | |
| Smoke exhaust (ДУ): airflow, fan capacity | smoke_control |
| Stairwell pressurization (ПД): airflow, shaft/vestibule pressure | smoke_control |
| Smoke control system activation from fire alarm (ОПС) | smoke_control |
| Fire protection of ДУ ducts: type, fire resistance rating (EI 60/EI 150) | smoke_control |
| Dampers КПВ/КДМ/КПС: type, size, fire resistance rating | smoke_control |
| Fire dampers on general ventilation ducts at wall/floor penetrations | smoke_control |
| Smoke exhaust airflow calculation (room, floor, fire load) | smoke_control |
| Makeup air for smoke exhaust (supply air during ДУ operation) | smoke_control |
| Combined operation of ДУ + ПД + general ventilation shutdown | smoke_control |
| | |
| VRF system: outdoor units, capacity, refrigerant | conditioning |
| VRF system: refrigerant piping lengths and elevation differences | conditioning |
| VRF system: refnets, branch selectors, piping restrictions | conditioning |
| Split systems: model, capacity, connection | conditioning |
| Fan coil units: model, cooling/heating capacity, airflow | conditioning |
| Chiller: model, capacity, coolant, pump group | conditioning |
| Condensate drain: diameter, slope, discharge point | conditioning |
| Chilled water piping: diameter, thermal insulation, material | conditioning |
| | |
| Discrepancies between plan ↔ axonometric view ↔ specification (heating) | ov_drawings |
| Discrepancies between plan ↔ AHU schematic ↔ specification (ventilation) | ov_drawings |
| Discrepancies between plan ↔ specification (air conditioning) | ov_drawings |
| Sheet inventory (drawing register vs actual sheets) | ov_drawings |
| Title blocks and formatting (ГОСТ Р 21.101) | ov_drawings |
| Legend/symbols (presence of explanations, ГОСТ 21.205) | ov_drawings |
| System labeling: consistency of designations П/В/ДУ/ПД/ОТ/ТП/К | ov_drawings |
| | |
| Airflow arithmetic: sum per grilles vs AHU total | ov_tables |
| Heat loss arithmetic: calculation vs totals vs system capacity | ov_tables |
| Equipment specifications: quantities, units of measurement | ov_tables |
| Airflow balance: supply vs exhaust per table | ov_tables |
| Recalculation of duct areas, pipe lengths | ov_tables |
| Capacities: sum per devices vs source capacity | ov_tables |
| | |
| Currency of regulatory references (status per norms_db) | ov_norms |
| Content of norm paragraphs (per norms_paragraphs) | ov_norms |
| СП 60.13330 — heating, ventilation, air conditioning | ov_norms |
| СП 7.13130 — fire protection requirements for ventilation systems | ov_norms |
| СП 50.13330 — thermal protection of buildings | ov_norms |
| СП 54.13330 — residential apartment buildings (indoor climate) | ov_norms |
| СП 73.13330 — internal sanitary-technical systems | ov_norms |
| Completeness of regulatory framework for OV section | ov_norms |
