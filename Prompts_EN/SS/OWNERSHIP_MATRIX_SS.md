# Check Ownership Matrix

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|------------|
| Fire detector placement (distances, coverage areas) | ss_fire_alarm |
| Addressable loop capacity (devices per loop <=128/255) | ss_fire_alarm |
| SOUE type selection (1-5) and sound pressure >=75 dBA | ss_fire_alarm |
| Fire alarm cable fire resistance (FR, E30-E90) | ss_fire_alarm |
| PPKP capacity and address allocation | ss_fire_alarm |
| APS integration with engineering systems (ventilation shutdown, smoke extraction start) | ss_fire_alarm |
| Backup power for APS (battery >=24h standby + 1h alarm) | ss_fire_alarm |
| Manual call points placement (at exits, <=45m between) | ss_fire_alarm |
| Fire alarm notification to fire department (retransmission) | ss_fire_alarm |
| Short-circuit isolators on addressable loops | ss_fire_alarm |
| | |
| SKUD controllers and readers (type, protocol, capacity) | ss_access_security |
| Electric locks (type, power, fail-safe/fail-secure) | ss_access_security |
| SKUD unlock on fire alarm signal | ss_access_security |
| CCTV cameras (resolution, IR, viewing angles) | ss_access_security |
| Video archive storage (>=30 days, SHD capacity) | ss_access_security |
| IP intercom system (call panels, apartment stations, concierge) | ss_access_security |
| Intrusion alarm sensors and zones | ss_access_security |
| OZDS system (derat sensors, controllers) | ss_access_security |
| Integration SKUD + SOT + SDS | ss_access_security |
| | |
| Automation functional diagrams (sensor -> controller -> actuator) | ss_automation |
| Control algorithms (PID, protections, interlocks) | ss_automation |
| Communication protocols (Modbus RTU/TCP, BACnet, LonWorks) | ss_automation |
| Dispatching workstation (AWP, server, visualization) | ss_automation |
| Elevator fire mode (recall to ground floor, firefighter control) | ss_automation |
| Pump station automation (dry-run protection, alternation, cascade) | ss_automation |
| ASUD.I controller I/O capacity and module allocation | ss_automation |
| Leak protection system (sensors, valves, controller) | ss_automation |
| | |
| Metering points (commercial at input, per-apartment, technical) | ss_metering |
| Electricity meters (accuracy class 1.0/0.5S, interfaces) | ss_metering |
| Current transformers for ASKUE (Ktt, class 0.5S) | ss_metering |
| Concentrators (channel count, SPODES/DLMS protocol) | ss_metering |
| Water/heat meters (metrological class, straight sections) | ss_metering |
| Data collection server and EIS ZhKH integration | ss_metering |
| ASKUE communication channels (RS-485/RF/GPON) | ss_metering |
| | |
| Cable tray types and fill rate (<=40%) | ss_cabling |
| Separation of low-voltage and power cables (>=150mm or partition) | ss_cabling |
| Sleeve packages through walls/floors (fire-rated sealing) | ss_cabling |
| SCS cable category (Cat.6/Cat.6A, segment <=90m) | ss_cabling |
| GPON architecture (splitters, OLT/ONT, attenuation budget <=28dB) | ss_cabling |
| Server/communication rooms (placement, climate, UPS) | ss_cabling |
| Cable tray mounting (brackets, threaded rods, bottom elevations) | ss_cabling |
| Fire-rated enclosures for low-voltage cables | ss_cabling |
| | |
| SKTV head-end station (DVB-T2 reception, amplification) | ss_media |
| Distribution network (RG-6/RG-11 cable, signal levels 60-80 dBuV) | ss_media |
| Tap-offs and splitters (signal level calculation) | ss_media |
| Antennas (UHF, installation height) | ss_media |
| RSPI radio (3 programs, sound pressure level) | ss_media |
| SOUE integration with radio distribution | ss_media |
| SAKZ gas detection (sensors, valves, controller) | ss_media |
| | |
| Regulatory reference currency (status per norms_db) | ss_norms |
| Norm clause content (per norms_paragraphs) | ss_norms |
| Completeness of the regulatory base for SS | ss_norms |
| | |
| Discrepancies between text, structural diagrams, and floor plans | ss_drawings |
| Sheet inventory (table of contents vs actual sheets) | ss_drawings |
| Title blocks and formatting | ss_drawings |
| Legend symbols per GOST 21.210 | ss_drawings |
| Device counts on diagrams vs plans vs specifications | ss_drawings |
| Cable journal vs specification consistency | ss_drawings |
