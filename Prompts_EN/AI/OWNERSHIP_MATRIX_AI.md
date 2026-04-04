# Check Ownership Matrix (AI section — architectural interiors)

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole owner |
|-------|------------|
| Layered wall finish composition (primer → plaster → decor → paint) | finishes |
| Finish layer compatibility (substrate ↔ primer ↔ plaster) | finishes |
| Room categories per СП 71.13330 (К3/К4) | finishes |
| Wall finish types (Ш-1, Ш-2, К-1, Д-1, М-1) — decoding and completeness | finishes |
| Floor types (ПЛ-1, ПЛ-2, ПЛ-3) — layered composition, waterproofing | finishes |
| Presence of finish type in specification (yes/no) | finishes |
| Fire-technical characteristics of finishes (КМ class) on common area evacuation routes | finishes |
| NCS color codes — presence and correctness of notation | finishes |
| Materials: porcelain stoneware, marble, limestone — thicknesses, format, layout | finishes |
| | |
| Door specification: size, type, quantity | doors_hardware |
| Door count: plan vs schedule/specification | doors_hardware |
| EI rating of doors (fire-rated doors on evacuation routes) | doors_hardware |
| Door hardware (handles, hinges, closers) | doors_hardware |
| Concealed access hatches (ЛСМ): quantity, dimensions, reference | doors_hardware |
| Sliding systems (Eclisse and analogues): type, pocket size | doors_hardware |
| Opening direction (evacuation, bathrooms) | doors_hardware |
| | |
| КНАУФ ceiling systems (series 1.045.9, 1.073.9, 1.031.9) | ceilings |
| Double-layer ceilings (ГКЛВ / Аквапанель) — where required | ceilings |
| Ceiling suspension heights (elevations from finished floor) | ceilings |
| Baseboards: shadow profile / gypsum cornice — type and dimensions | ceilings |
| LED strip in ceilings: power, profile, diffuser | ceilings |
| Ceiling attachment to slab (hanger spacing, profile type) | ceilings |
| Ceilings in wet rooms (Аквапанель, not ГКЛВ) | ceilings |
| | |
| Sanitary ware specification: toilets, sinks, faucets, installations | sanitary |
| Shower channels and drains (TECEdrainline and analogues) | sanitary |
| Custom-made bathroom furniture | sanitary |
| Sanitary fixture count: plan vs specification | sanitary |
| Reception desk and other custom-made furniture | sanitary |
| Serial furniture (La Palma, Kinnarps, Taschini) — quantity and type | sanitary |
| | |
| Discrepancies plan ↔ elevation (materials, dimensions, equipment) | ai_drawings |
| Discrepancies elevation ↔ specification (quantity, type) | ai_drawings |
| Discrepancies plan ↔ specification (equipment quantity) | ai_drawings |
| Sheet inventory (register vs actual presence) | ai_drawings |
| Title blocks and formatting (ГОСТ 21.507) | ai_drawings |
| Legend symbols (presence of decoding) | ai_drawings |
| | |
| Finish area arithmetic (m²) | ai_tables |
| Equipment quantity arithmetic (pcs) | ai_tables |
| Baseboard linear meters (l.m.) | ai_tables |
| LED strip linear meters (l.m.) | ai_tables |
| Luminaire count: plan ↔ specification | ai_tables |
| Specification completeness (all items from plan present in specification) | ai_tables |
| | |
| Regulatory reference currency (status per norms_db) | ai_norms |
| Norm clause content (per norms_paragraphs) | ai_norms |
| СП 71.13330 — finishing work requirements | ai_norms |
| СП 29.13330 — floor requirements | ai_norms |
| СП 163.1325800 — architectural solution requirements | ai_norms |
| СП 52.13330 — illumination standards (as related to interior solutions) | ai_norms |
| ГОСТ 21.507 — interior drawing formatting | ai_norms |
| Completeness of the AI section regulatory framework | ai_norms |
