# Check Ownership Matrix

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|------------|
| Coordinate grid, building axes, tie-in to red lines | gp_layout |
| Fire access roads (width >= 3.5 m, turning radii >= 12 m) | gp_layout |
| Distances between buildings (fire breaks per SP 4.13130) | gp_layout |
| MHN accessibility (ramps, slopes <= 8%, tactile indicators) | gp_layout |
| Site zoning (residential, utility, recreation areas) | gp_layout |
| Parking layout and count (per SP 42.13330 / regional norms) | gp_layout |
| | |
| Pavement structure layers (base, sub-base, surface course) | gp_pavements |
| Pavement types (asphalt, paving tiles, gravel) and assignment | gp_pavements |
| Longitudinal and transverse slopes for drainage | gp_pavements |
| Curb stones (type designations BR100.30.15 / BR100.20.8) | gp_pavements |
| Transition joints between different pavement types | gp_pavements |
| Pavement bearing capacity for fire truck loads | gp_pavements |
| Material quantities in pavement specification | gp_pavements |
| Road structure cross-sections (layer thicknesses) | gp_pavements |
| | |
| Plant species selection for climate zone | gp_landscaping |
| Planting distances from buildings (trees >= 5 m, shrubs >= 1.5 m) | gp_landscaping |
| Planting distances from underground utilities | gp_landscaping |
| Plant quantities: specification vs plan count | gp_landscaping |
| Automatic irrigation system (zones, flow rates, coverage) | gp_landscaping |
| Mulching and topsoil (layer thicknesses, volumes) | gp_landscaping |
| Lawn areas and seed mix specification | gp_landscaping |
| | |
| MAF specifications (manufacturer, model, quantity) | gp_maf |
| Playground equipment safety (GOST R 52169, safety zones) | gp_maf |
| MAF structural solutions (pergolas, benches, canopies) | gp_maf |
| Anti-corrosion treatment of metal MAF structures | gp_maf |
| Foundations under MAF (type, dimensions) | gp_maf |
| Wind and snow loads on canopies and pergolas | gp_maf |
| Fence/enclosure design and heights | gp_maf |
| Retaining walls (structural design, drainage, waterproofing) | gp_maf |
| | |
| Consolidated utility plan (clearances between networks) | gp_engineering |
| Storm drainage (trays, sand traps, manholes, pipe diameters) | gp_engineering |
| Vertical grading (elevations, slopes away from building >= 0.5%) | gp_engineering |
| Site drainage system (French drains, drainage pipes) | gp_engineering |
| Outdoor lighting pole placement and spacing | gp_engineering |
| Utility protection zones on site plan | gp_engineering |
| Utility crossings under roads (sleeves, depth) | gp_engineering |
| Earthwork volumes (cut/fill balance) | gp_engineering |
| | |
| Normative reference currency (status per norms_db) | gp_norms |
| Norm clause content (per norms_paragraphs) | gp_norms |
| Obsolete SNiP/GOST references | gp_norms |
| Completeness of the regulatory base for GP | gp_norms |
| | |
| Drawing register vs actual sheets | gp_drawings |
| Discrepancies between plans and specifications | gp_drawings |
| Title blocks, project codes, sheet numbering | gp_drawings |
| Scale consistency across drawings | gp_drawings |
| Legend symbols and conventions | gp_drawings |
| Coordinate consistency across different plan sheets | gp_drawings |
