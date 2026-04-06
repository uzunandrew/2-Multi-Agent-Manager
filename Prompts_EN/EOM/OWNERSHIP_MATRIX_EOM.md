# Check Ownership Matrix — EOM

## Core Principle

Each check has **ONE** owner. Other agents **DO NOT** duplicate that check. If an agent discovers an issue outside its zone, it records it **only** in `checklist.notes` but **does not** create a finding.

## Check Types

| Check Type | Sole Owner | Description |
|---|---|---|
| **Consistency** — literal mismatch of the same parameter between sources | `consistency` | The same parameter differs across text, schematic, plan, specification, or layout |
| **Arithmetic** — formula, sum, coefficient recalculation within a table | `tables` | Error is discovered through mathematical recalculation |
| **Engineering correctness** — adequacy of a solution in its domain | domain R1 agent | Solution is technically incorrect per codes or engineering practice |
| **Norm status** — document currency, clause reference correctness | `norms` | Norm is cancelled/replaced, clause number is wrong |

**Resolution rule:** when ownership is unclear, determine the **type** from the table above.

---

## Ownership by Agent

### `consistency` (documentation consistency)

| Check | Owner |
|-------|-------|
| Literal mismatch text ↔ schematic (names, brands, parameters) | consistency |
| Literal mismatch schematic ↔ plan (presence, location) | consistency |
| Literal mismatch schematic ↔ specification (brand, type, rating, quantity) | consistency |
| Literal mismatch plan ↔ specification (presence, quantity) | consistency |
| Literal mismatch layout ↔ schematic (panel count, arrangement) | consistency |
| Sheet inventory (table of contents vs actual sheets) | consistency |
| Coverage gaps (sheet not covered by any agent) | consistency |

**Does NOT own:**
- title blocks, ciphers, sheet names, revision marks
- formatting cosmetics, legend symbols
- arithmetic (formula recalculation) → `tables`
- engineering evaluation of solution correctness → domain agent
- normative reference status → `norms`

---

### `tables` (arithmetic and internal mathematics)

| Check | Owner |
|-------|-------|
| Load table arithmetic (Pу, Pр, Qр, Sр, Iр) | tables |
| Summary totals by ВРУ / sections / ГРЩ | tables |
| Internal coefficient consistency (Kс, cosφ, Ко, Kн.макс) | tables |
| CT table arithmetic (formula recalculation by operating modes) | tables |

**Does NOT own:**
- full specification check (quantity vs schematic/plan) → `consistency`
- position numbering and ordering in specification
- engineering evaluation of coefficient selection → notes
- "spare breakers ≥10%" as universal requirement → notes

---

### `cables` (engineering correctness of cable lines)

| Check | Owner |
|-------|-------|
| Cable cross-sections by permissible current (Idesign ≤ Iallow) | cables |
| Breaker ↔ cable coordination (Irated ≤ Iallow, Irated ≥ Idesign) | cables |
| B/C/D characteristics for group breakers | cables |
| Breaking capacity (Ics ≥ Ishort-circuit) | cables |
| Voltage drop (total ≤ 5%) | cables |

**Does NOT own:**
- cable brand mismatch between sources (text ↔ schematic ↔ specification) → `consistency`
- economic current density as a finding → notes
- load table arithmetic → `tables`

---

### `fire_safety` (electrical fire safety)

| Check | Owner |
|-------|-------|
| FR/FRLS/FRHF — cable fire resistance for fire protection system lines | fire_safety |
| EI45/EI60/EI150 — required fire resistance rating for cable routes | fire_safety |
| Separation of mutually redundant lines | fire_safety |
| Cable penetrations through fire barriers | fire_safety |
| Fire protection system power supply / "Fire" mode on schematic | fire_safety |
| Emergency / evacuation lighting (EXIT signs, autonomy ≥3h) | fire_safety |
| Smoke extraction, air pressurization, activation from fire alarm | fire_safety |
| Working/emergency lighting on separate cable trays | fire_safety |

**Does NOT own:**
- general equipment IP rating by environmental conditions → `lighting` (luminaires), `power_equipment` (power equipment)
- cable brand mismatch between sources → `consistency`
- room categories as a standalone finding (only as context for FR/EI)

---

### `cable_routes` (cable route construction)

| Check | Owner |
|-------|-------|
| Cable tray fill rate (≤ 40%) | cable_routes |
| Co-routing of power + low-voltage cables | cable_routes |
| Mounting assemblies (threaded rods, bottom elevations, brackets) | cable_routes |
| Fire-rated enclosure construction (internal dimensions, sheathing thickness, ventilation grilles) | cable_routes |

**Does NOT own:**
- tray size mismatch plan ↔ specification → `consistency`
- length mismatch plan ↔ specification → `consistency`
- required fire resistance rating EI as fire requirement → `fire_safety`

---

### `lighting` (general and architectural lighting)

| Check | Owner |
|-------|-------|
| Luminaire IP rating by operating conditions | lighting |
| Lighting power balance | lighting |
| DALI: controllers, power supplies, ≤64 per line | lighting |
| Illuminance standards (lux) — only when calculation/specification exists | lighting |

**Does NOT own:**
- emergency / evacuation lighting → `fire_safety`
- "luminaire on plan but missing from specification" mismatch → `consistency`
- specification position numbering gaps

---

### `metering` (energy metering system)

| Check | Owner |
|-------|-------|
| CT selection (Ktt, accuracy class, justification by working/emergency current) | metering |
| Meters (model, interface, АСКУЭ compatibility) | metering |
| ИКК (presence, connection diagram) | metering |
| Metering points (commercial / technical) | metering |

**Does NOT own:**
- CT table arithmetic (formula recalculation) → `tables`
- CT model/quantity mismatch between schematic and specification → `consistency`

---

### `automation` (control logic)

| Check | Owner |
|-------|-------|
| Control logic (scenarios, SA/K/KM) | automation |
| Interface with АСУД (XT1/XT2, terminal blocks, protocol) | automation |
| Astronomical relays, timers | automation |
| АВР for lighting panels | automation |

**Does NOT own:**
- "no assignment to adjacent section" as a finding → notes
- absence of backup astronomical relay as mandatory remark → notes

---

### `grounding` (grounding and lightning protection)

| Check | Owner |
|-------|-------|
| TN-C-S, PEN splitting point | grounding |
| ГЗШ and connections to it | grounding |
| Equipotential bonding (ОСУП, ДСУП, КУП) | grounding |
| Lightning protection (air terminals, down conductors) | grounding |
| PE conductors (cross-sections) | grounding |

**Does NOT own:**
- ДСУП in rooms not covered by this project section

---

### `power_equipment` (power electrical equipment)

| Check | Owner |
|-------|-------|
| Electric motors (starting type, protection) | power_equipment |
| Socket networks (RCD 30mA, dedicated lines) | power_equipment |
| Cable heating (power, thermostat, RCD) | power_equipment |
| Variable frequency drives | power_equipment |
| Interlocks with process equipment (pumps, general ventilation) | power_equipment |

**Does NOT own:**
- panel completeness per specification (schematic ↔ specification) → `consistency`
- "spare groups" as universal requirement → notes

---

### `outdoor_install` (outdoor installation and earthworks)

| Check | Owner |
|-------|-------|
| Cable burial depth in trenches | outdoor_install |
| Distances from utilities | outdoor_install |
| Conduits under roads | outdoor_install |
| Earthwork volumes (arithmetic) | outdoor_install |

**Does NOT own:**
- "distances not specified, only PUE reference" as finding → notes

---

### `norms` (normative references)

| Check | Owner |
|-------|-------|
| Norm status (active / cancelled / replaced) | norms |
| Clause number and citation correctness | norms |

**Does NOT own:**
- "СП 256 missing from normative list" as standalone finding → notes
- "PUE without parallel СП reference" as finding → notes
- general completeness of normative document list as finding → notes
