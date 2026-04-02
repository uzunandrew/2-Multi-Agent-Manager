# Check Ownership Matrix (AR Section)

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|------------|
| Aerated concrete wall thickness (D500/D600), grade compliance | walls_masonry |
| Masonry reinforcement (basalt mesh, spacing, rebar in grooves) | walls_masonry |
| Masonry attachment to frame (anchors, flexible ties, gaps) | walls_masonry |
| Masonry waterproofing in wet rooms (300 mm) | walls_masonry |
| Deformation joints in masonry | walls_masonry |
| U-shaped blocks and reinforcement belts (армопояс) | walls_masonry |
| Masonry bearing length on floor slab | walls_masonry |
| | |
| Door specification (type, size, EI) | openings_doors |
| Lintels (type, cross-section, bearing) | openings_doors |
| Correspondence of openings on plan vs. specification | openings_doors |
| Opening dimensions (width, height) | openings_doors |
| Fire-rated doors (EI 30/60) -- presence and marking | openings_doors |
| Lintel angles and plates (L100x100x8, 200x20, 300x20) | openings_doors |
| | |
| Roof assembly (layer composition, thicknesses) | roof_waterproof |
| Технониколь ЭПП waterproofing (number of layers, overlaps) | roof_waterproof |
| Roof insulation (material, lambda, thickness) | roof_waterproof |
| Roof junctions to parapet, walls, pipes | roof_waterproof |
| Drainage (funnels, slopes, emergency overflows) | roof_waterproof |
| Slope formation (method, min-max thicknesses) | roof_waterproof |
| Green roofs (drainage, root barrier, substrate) | roof_waterproof |
| Vapor barrier (presence, type) | roof_waterproof |
| | |
| Staircase railing height (1200 mm for >10 stories) | stairs_railings |
| Baluster spacing (max 100 mm) | stairs_railings |
| Stair flight width | stairs_railings |
| Railing mounting anchors (Hilti HST M10x100) | stairs_railings |
| Railing tube (30x15x2 and analogues) | stairs_railings |
| Flight slope, step height/width | stairs_railings |
| Gap between flights (min 75 mm) | stairs_railings |
| Handrails (height, continuity) | stairs_railings |
| | |
| Fire resistance ratings of walls and floor slabs (REI 150/60) | fire_barriers |
| Fire-rated doors (EI) -- compliance with ФЗ-123 | fire_barriers |
| Sealing of openings in fire barriers | fire_barriers |
| Fire-rated partitions (types, ratings) | fire_barriers |
| Fire protection of load-bearing structures | fire_barriers |
| Evacuation routes (width, length, doors on routes) | fire_barriers |
| | |
| Discrepancies: marking plan vs. masonry plan vs. details | ar_drawings |
| Sheet inventory (register vs. actual presence) | ar_drawings |
| Axis references (plan vs. section) | ar_drawings |
| Elevation levels (plan vs. section vs. detail) | ar_drawings |
| Element marking (Д, ПР, ОК) across different sheets | ar_drawings |
| | |
| Specification arithmetic (aerated concrete volumes, quantities) | ar_tables |
| Area calculation (room schedule vs. plan) | ar_tables |
| Lintel lengths, door quantities | ar_tables |
| Finish schedule (areas, materials) | ar_tables |
| Roof insulation volumes | ar_tables |
| | |
| Currency of СП 15.13330, СП 17.13330, СП 70.13330 | ar_norms |
| Currency of ГОСТ 31360, ГОСТ 25772 | ar_norms |
| Norm clause content (per norms_paragraphs) | ar_norms |
| Completeness of the AR section regulatory base | ar_norms |
| Regulatory reference hierarchy (ФЗ > СП > ГОСТ) | ar_norms |
