# Check Ownership Matrix

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|------------|
| Calendar plan sequence and logic (stages, critical path) | pos_schedule |
| Normative construction duration (SNiP 1.04.03-85*, MDS 12-43.2008) | pos_schedule |
| Work volumes arithmetic (earthworks, concrete, installation) | pos_schedule |
| Winter construction measures (T < -15C) | pos_schedule |
| Work shifts and crew composition | pos_schedule |
| Stage interrelation (cannot start superstructure before foundations) | pos_schedule |
| | |
| Site layout plans (SGP) per construction stage | pos_site_plan |
| Crane coverage zones (boom reach, load capacity, hazard zones) | pos_site_plan |
| Temporary roads (width, turning radii, surface type) | pos_site_plan |
| Site fencing (height >= 2m, canopy over pedestrian passages) | pos_site_plan |
| Temporary buildings and facilities (shelters, canteen, sanitation) | pos_site_plan |
| Temporary power supply and water supply for the site | pos_site_plan |
| Material storage areas and open storage | pos_site_plan |
| Fire safety on the construction site (driveways, hydrants, PPR) | pos_site_plan |
| Crane installation and dismantling schemes | pos_site_plan |
| | |
| Utility crossing clearances (horizontal separation by SP 42.13330 table 16) | pos_utilities |
| Protective zones of existing utilities (gas, heat, power) | pos_utilities |
| Protection of existing utilities during construction (sheet piling, suspension) | pos_utilities |
| Utility burial depths | pos_utilities |
| Manholes at utility crossings | pos_utilities |
| Technical conditions (TU) from operating organizations | pos_utilities |
| Consolidated utility network plan completeness | pos_utilities |
| | |
| Normative reference currency (status per norms_db) | pos_norms |
| Norm clause content (per norms_paragraphs) | pos_norms |
| Completeness of the normative framework for POS | pos_norms |
| Obsolete norms (SNiP without replacement SP) | pos_norms |
| Hierarchy of normative documents | pos_norms |
| | |
| Drawing register vs actual sheets | pos_drawings |
| SGP vs text part consistency (stage descriptions match drawings) | pos_drawings |
| Calendar plan vs SGP stages alignment | pos_drawings |
| Consolidated utility plan vs text (utility list) | pos_drawings |
| Title blocks and formatting (GOST R 21.101-2020) | pos_drawings |
| Legend symbols and consistency | pos_drawings |
| Transport route schemes vs SGP consistency | pos_drawings |
