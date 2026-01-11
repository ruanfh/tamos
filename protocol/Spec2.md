
# TAMOS Protocol Specification

## 1. Status

This specification defines the TAMOS protocol in its current form.  
It is **experimental** and may change without notice.  
Implementations should expect breaking changes and should not assume long-term stability or backward compatibility unless explicitly stated in a future revision of this document.

## 2. Terminology

Terms are symbolic identifiers, not conceptual metaphors.  
No semantic meaning should be inferred beyond what is explicitly specified.

This specification uses the following terms in a precise, technical way.

### 2.1 Agents

- **Scout:**
	- An agent that offers a Gem to the Horizon through the East-Horizon.
	- Scouts do not retrieve Stars.

- **Navigator:**
	- An agent that explores Skies by retrieving Stars and Constellations.
	- Navigators do not offer Gems.

### 2.2 Protocol Role

- **Horizon:**
	- The protocol role that receives Gems from Scouts and casts Stars.
	- The Horizon is the only active protocol role defined by TAMOS.
	- The Horizon has two conceptual faces:
		- **East Horizon** — the normative entry point where Gems are offered and Stars are cast.
		- **West Horizon** — an interface for permanently deleting a Star.
    - No other modification or editing behaviors are permitted to the Horizon.
	- TAMOS defines only the East Horizon. The West Horizon is optional and may be implemented in any manner for permanent deletion of Stars, without affecting protocol compliance.
	- Implementations **SHOULD** call the role for deletion the Cleaner.

### 2.3 Objects

- **Gem:**
	- The unit of content offered by a Scout to the Horizon. A Gem exists before casting.
	- A Gem **MUST** conform to the canonical Gem Submission Schema: [gem.submit.schema.json](gem.submit.schema.json).

- **Star:**
	- The published representation created by the Horizon from a Gem. A Star exists after casting.
	- A Star **MUST** contain the original Gem, unchanged, and **MAY** also have extra fields added.
	- A Star **MUST NOT** be modified after casting.
	- A Star **MAY** be permanently deleted via the West Horizon.

- **Constellation:**
	- A logical collection of Stars.
	- A Horizon **MUST** expose at least one Constellation containing Stars.
	- When casting a Star, the Horizon **MUST** assign it to at least one Constellation.
	- TAMOS does **not** define how Constellations are represented or exposed within a Sky.

### 2.4 Environment

- **Sky:**
	- The environment in which Stars and Constellations are kept and exposed for Navigators to explore.
	- The Sky is not a role or an object; it is the medium through which Navigators access Stars.
	- Skies **MAY** be accessible to any Navigators or only to specific Navigators, as determined by the implementation.
	> TAMOS does not define authentication, authorization, or identity semantics for Sky access.

---

## 3. Protocol Scope

This specification defines the TAMOS protocol roles, objects, and invariants required for publishing and discovering resources. It governs the structure and relationships between Scouts, Horizons, Gems, Stars, Constellations, Skies, and Navigators.

Behavior not explicitly defined in this specification is outside the scope of TAMOS and left to individual implementations.

---

## 4. Design Goals and Non-Goals

TAMOS is designed to be minimal, composable, and implementation-agnostic. It aims to provide a small set of primitives for publishing and discovery **without** prescribing ranking, trust, identity, monetization, moderation, or governance models.

TAMOS does **not** attempt to enforce fairness, prevent spam, guarantee visibility, or define how discovery results are evaluated or presented.

---

## 5. Protocol Flow (Non-Normative)

In a typical TAMOS deployment:

1. A Scout offers a Gem to a Horizon through the East Horizon.
2. The Horizon processes the Gem and casts a corresponding Star, assigning it to one or more Constellations.
3. Stars and Constellations are kept within a Sky, where they become accessible to Navigators.
4. Navigators retrieve Stars and Constellations from Skies in order to explore, connect, and interpret published resources.

---

## 6. Normative Protocol Rules

- A Horizon **MUST** accept or reject offered Gems based on conformance with the Gem Submission Schema.
- When casting a Star, the Horizon **MUST** preserve the Gem’s schema-defined structure, **MUST NOT** modify values within that structure, and **MAY** add additional fields outside of it.
- A Horizon **MUST** assign each Star to at least one Constellation at the time of casting.
- Scouts **MUST NOT** retrieve Stars, and Navigators **MUST NOT** offer Gems.

---

## 7. Data Models and Schemas

TAMOS defines a canonical Gem Submission Schema that all offered Gems **MUST** conform to.

Additional schemas **MAY** be defined by implementations for Stars or Constellations, provided they do not violate the invariants defined in this specification.

Schema evolution, versioning, and validation behavior are implementation-defined unless explicitly constrained by this document.

---

## 8. Error Handling and Invalid States

If a Gem does not conform to the Gem Submission Schema, the Horizon **MUST** reject it without casting a Star.

TAMOS does **not** define error codes, retry behavior, or failure signaling. Error handling is entirely implementation-defined.

---

## 9. Conformance and Compliance

An implementation is considered TAMOS-compliant if it adheres to all **MUST** and **MUST NOT** requirements defined in this specification.

Compliance may apply to individual roles, such as Horizons, Scouts, or Navigators, independently. Implementations **MAY** support additional behaviors or extensions, provided they do not violate the normative requirements of TAMOS.

---

## 10. Extensibility and Forward Compatibility

TAMOS is designed to allow extensions and evolution without central coordination. Implementations **SHOULD** tolerate unknown fields and additional data when processing Gems and Stars.
   
Extensions **MUST NOT** alter the meaning of existing fields or violate normative protocol rules. Future versions of this specification may introduce additional roles, objects, or constraints.

---

## 11. Security and Privacy Considerations

TAMOS defines no security, authentication, authorization, or privacy guarantees. All security and privacy properties depend on how implementations are built, deployed, and operated.

Implementers and deployers are responsible for assessing risks, protecting their environments, and ensuring compliance with applicable security and privacy requirements. See the Security section for additional guidance.

---

## 12. Examples (Non-Normative)

Examples are for illustration only and do not define requirements or constraints.
