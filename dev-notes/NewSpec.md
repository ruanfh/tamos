
# TAMOS Protocol Specification

## 0. Status

This specification is experimental and may change without notice.

## 1. Vocabulary

Terms are symbolic identifiers, not conceptual metaphors.  
No semantic meaning should be inferred beyond what is explicitly specified.

This specification uses the following terms in a precise, technical way.

### 1.1 Agents

- **Scout:**
	- An agent that offers a Gem to the Horizon through the East-Horizon.
	- Scouts do not retrieve Stars.

- **Navigator:**
	- An agent that explores Skies by retrieving Stars and Constellations.
	- Navigators do not offer Gems.

### 1.2 Protocol Role

- **Horizon:**
	- The protocol role that receives Gems from Scouts and casts Stars.
	- The Horizon is the only active protocol role defined by TAMOS.
	- The Horizon has two conceptual faces:
		- **East Horizon** — the normative entry point where Gems are offered and Stars are cast.
		- **West Horizon** — an intentionally undefined interface for removal or modification behaviors outside the scope of TAMOS.
	- TAMOS defines only the East Horizon. The West Horizon is optional and may be implemented in any manner without affecting protocol compliance.

### 1.3 Objects

- **Gem:**
	- The unit of content offered by a Scout to the Horizon. A Gem exists before casting.
	- A Gem **MUST** conform to the canonical Gem Submission Schema: [gem.submit.schema.json](gem.submit.schema.json).

- **Star:**
	- The published representation created by the Horizon from a Gem. A Star exists after casting.
    - A Star **MUST** preserve the Gem’s structure exactly.
	> For the purposes of this specification, “structure” refers to the schema-defined fields and their hierarchical organization, not the specific values they contain.
    - A Star **MAY** modify the values inside that structure.
    - A Star **MAY** add additional fields outside that structure.
    - TAMOS does **not** define or constrain how these modifications occur

- **Constellation:**
	- A logical collection of Stars.
	- TAMOS requires that Stars are grouped into Constellations but does not define how this grouping is determined.
	- A Horizon **MUST** expose at least one Constellation containing each Star.
	- When casting a Star, the Horizon MUST assign it to at least one Constellation.
	- TAMOS does **not** define how Constellations are represented or exposed within a Sky.

### 1.4 Environment

- **Sky:**
	- The environment in which Stars and Constellations are kept and exposed for Navigators to explore.
	- The Sky is not a role or an object; it is the medium through which Navigators access Stars.
	- Skies **MAY** be accessible to any Navigators or only to specific Navigators, as determined by the implementation.
	> TAMOS does not define authentication, authorization, or identity semantics for Sky access.

---

## 2. Scope

TAMOS defines the minimal contract for transforming a submitted Gem into a published Star, placing Stars into Constellations, and exposing those Constellations through one or more Skies for Navigators to explore.

TAMOS specifies the roles of Scout, Horizon, and Navigator, the objects Gem, Star, and Constellation, and the environment known as the Sky.

TAMOS defines only the East‑Horizon, where Gems are offered and Stars are cast.

All behaviors beyond casting (including removal, modification, ordering, ranking, storage, transport, and API structure) are explicitly outside the scope of this specification.

TAMOS guarantees no persistence, no addressing, and no interpretation of content; it defines only the minimal lifecycle required for exposing Gems (url + description) to Navigators.

---

## 3. Normative Behaviors (DRY Version)

TAMOS defines only the following required behaviors:

### 3.1 Casting (East Horizon)
- Structure **MUST** be preserved
- Values **MUST NOT** be modified
- Additional fields **MAY** be added

### 3.2 Constellations
- Every Star **MUST** belong to at least one Constellation.
- TAMOS does not define how Constellations are formed.

### 3.3 Skies
- Skies **MUST** expose the Stars and Constellations that the Horizon places within them.
- TAMOS does not define storage, transport, addressing, or persistence.

### 3.4 Horizon Boundaries
- TAMOS defines only the East‑Horizon.
- The West‑Horizon is outside the scope of this specification.

