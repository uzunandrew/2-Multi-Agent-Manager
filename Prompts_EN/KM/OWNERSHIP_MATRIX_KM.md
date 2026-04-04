# Check Ownership Matrix (KM Section)

Each check has ONE owner. Other agents DO NOT duplicate this check.

| Check | Sole Owner |
|-------|------------|
| Fachwerk column profiles (HEB/HEA/SHS), lengths, axis references | km_structural |
| Beam/girder profiles, spans, load capacity | km_structural |
| Member slenderness (lambda <= limits per SP 16.13330) | km_structural |
| Beam deflections (f/L <= 1/250 floors, <= 1/200 secondary) | km_structural |
| Steel grades (S245/S255/S345 per GOST 27772) vs structural group | km_structural |
| Corrosion protection (primer, coating thickness >= 80/120 um) | km_structural |
| Column attachment to RC structures (anchors, embedded items) | km_structural |
| Stability of compressed members (buckling check) | km_structural |
| | |
| Metal staircase geometry (flight width, step h/b, slope) | km_stairs_platforms |
| Staircase railings (height >= 1100 mm, infill gap <= 110 mm) | km_stairs_platforms |
| Service platforms (load >= 2.0 kPa, deck type, thickness >= 3 mm) | km_stairs_platforms |
| Platform railings and toeboards | km_stairs_platforms |
| Staircase stringers (profile, span, deflection) | km_stairs_platforms |
| Ladder types (vertical/inclined for maintenance) | km_stairs_platforms |
| Guardrails around openings and equipment | km_stairs_platforms |
| Platform attachment to main structure | km_stairs_platforms |
| | |
| Bolt grade (5.8/8.8/10.9), diameter, spacing, edge distance | km_connections |
| Weld type (butt/fillet/lap), throat size, length, electrode grade | km_connections |
| Column base plates (thickness, anchor bolts, grout) | km_connections |
| Anchors to concrete (type, embedment, pullout capacity) | km_connections |
| Hardware specification (bolts, nuts, washers -- class, quantity) | km_connections |
| Splice joints (flange/web splices, cover plates) | km_connections |
| Gusset plates (thickness, weld to main member) | km_connections |
| Moment vs shear connection designation | km_connections |
| | |
| Currency of SP 16.13330, SP 20.13330, SP 70.13330 | km_norms |
| Currency of GOST 27772, GOST 23118, GOST 14771 | km_norms |
| Norm clause content verification (per norms_paragraphs) | km_norms |
| Completeness of KM section regulatory base | km_norms |
| Regulatory reference hierarchy (FZ > SP > GOST) | km_norms |
| | |
| Drawing register vs actual sheets | km_drawings |
| Layout plans vs element drawings (profiles, references) | km_drawings |
| Steel specification arithmetic (mass = length x unit mass) | km_drawings |
| Steel grade consistency (drawings vs specification) | km_drawings |
| Title blocks, scales, symbols per GOST 21.502 | km_drawings |
| Element marking consistency across sheets | km_drawings |
| Totals by steel grade (S245/S255/S345 summation) | km_drawings |
