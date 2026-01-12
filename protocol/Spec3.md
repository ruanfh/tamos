
# TAMOS Protocol Specification

## 1 Scope and Status

### 1.1 What TAMOS IS

TAMOS is a minimal protocol for structuring information in a form that can be explored.

### 1.2 What TAMOS IS NOT

TAMOS is **NOT**:
- A general‑purpose modeling system.
- A transport or networking protocol.
- A storage or database system.

TAMOS does **NOT**:
- Define how exploration is performed.
- Guarantee human readability.

### 1.3 Status

This specification describes the TAMOS protocol in its current form.
It is experimental and subject to change without notice.
Implementations should expect breaking changes and must not assume long‑term stability or backward compatibility unless explicitly guaranteed in a future revision.

---

## 2 Schema and Examples

### 2.1 Schema

The file [gem.submit.schema.json](gem.submit.schema.json) is the only normative schema defined by TAMOS.

### 2.2 Examples

Examples are not normative and are provided solely for illustration:

- [examples/gem.example.json](examples/gem.example.json)
- [examples/gem.minimal.example.json](examples/gem.minimal.example.json)
- [examples/constellation.example.json](examples/constellation.example.json)

---

## 3 Terminology

Terms are symbolic identifiers, not conceptual metaphors.  
No semantic meaning should be inferred beyond what is explicitly specified.

This specification uses the following terms in a precise, technical way.

### 3.1 Required entity terms

#### 3.1.1 Gem
A Gem is any object that complies with the schema defined in [section 2.1](#21-schema).
#### 3.1.2 Star
A Star is a Gem suitable for exploration.
#### 3.1.3 Sky
The Sky is the place where Stars are made available for exploration.
#### 3.1.4 East-Horizon
An East‑Horizon receives a Gem and produces a Star within a Sky.
#### 3.1.5 West-Horizon
A West‑Horizon permanently removes a Star from a Sky.

### 3.2 Required profile terms

A Profile constrains how the implementation uses the East‑Horizon and West‑Horizon.

#### 3.2.1 TAMOS-Archive
A TAMOS‑Archive supports append‑only.
#### 3.2.2 TAMOS-Field
A TAMOS‑Field supports creation and removal, but does not support editing.
#### 3.2.3 TAMOS-Garden
A TAMOS‑Garden supports editable Stars.

### 3.3 Extended vocabulary

#### 3.3.1 Constellation
A constellation is a group of stars.

---

## 4 The TAMOS protocol

### 4.1 Core Protocol

- The East‑Horizon **MUST** reject any Gem that does not conform to the normative schema.
- The Star produced by the East‑Horizon **MUST** contain the submitted Gem intact and unmodified.

- The West‑Horizon **MUST** permanently remove the Star from the Sky.
- After removal, the Star **MUST NOT** be served for exploration by that Sky.

### 4.2 Optional Behaviors

- A Star **MAY** include additional fields added by the implementation, provided the submitted Gem remains intact and unaltered.
- An implementation **MAY** provide an edit operation, defined as an atomic composition of West‑Horizon followed by East‑Horizon.
- An implementation **MAY** assign identifiers to Stars for its own purposes. TAMOS does not define or constrain identifier format, stability, or semantics.
- A Sky **MAY** define an ordering for the Stars it serves. TAMOS does not define or constrain ordering semantics.
- Stars **MAY** be explored by any means, including programmatic access, file access, human inspection, automated scripts, or AI agents. TAMOS does not define or constrain exploration mechanisms.


### 4.3 Profile Behaviors

A TAMOS implementation **MUST** operate under exactly one Profile. The active Profile **MUST** be declared and enforced.

Profiles define the only permitted uses of the East‑Horizon and West‑Horizon. Any operation not explicitly permitted by the active Profile **MUST NOT** be performed.

#### 4.3.1 TAMOS‑Archive Profile

An implementation operating under the **TAMOS‑Archive** Profile:

- **MUST** permit use of the East-Horizon.
- **MUST NOT** permit use of the West‑Horizon.
- **MUST NOT** permit replacement or editing in any form.

This Profile is append‑only and immutable.

#### 4.3.2 TAMOS‑Field Profile

An implementation operating under the **TAMOS‑Field** Profile:

- **MUST** permit use of the East-Horizon.
- **MUST** permit use of the West‑Horizon.
- **MUST NOT** permit replacement or editing.
- **MUST** assign a stable identifier to each Star.
- **MUST NOT** reuse or reassign the Star’s identifier after removal.

Deletion removes a Star entirely. Any subsequent cast produces a new Star.

#### 4.3.3 TAMOS‑Garden Profile

An implementation operating under the **TAMOS‑Garden** Profile:

- **MUST** permit use of the East-Horizon.
- **MUST** permit use of the West‑Horizon.
- **MUST** permit replacement.
- **MUST** assign a stable identifier to each Star.

Replacement **MUST** be implemented as a single atomic operation that preserves the Star’s identifier.
The operation consists conceptually of:

1. Removing the existing Star.
2. Casting a new Star in its place.

No intermediate state may be externally observable.

---

## 5 Conformance

A TAMOS implementation is conformant only as one of the following:

- **TAMOS‑Archive**
- **TAMOS‑Field**
- **TAMOS‑Garden**

All conformant implementations **MUST** implement the Core Protocol defined in [Section 4.1](#41-core-protocol) and **MUST** operate under exactly one Profile defined in [Section 3.2](#32-required-profile-terms).

### 5.1 TAMOS‑Archive Conformance

An implementation claiming TAMOS‑Archive conformance **MUST** follow the Archive Profile Behaviors defined in [Section 4.3](#43-profile-behaviors).

### 5.2 TAMOS‑Field Conformance

An implementation claiming TAMOS‑Field conformance **MUST** follow the Field Profile Behaviors defined in [Section 4.3](#43-profile-behaviors).

### 5.3 TAMOS‑Garden Conformance

An implementation claiming TAMOS‑Garden conformance **MUST** follow the Garden Profile Behaviors defined in [Section 4.3](#43-profile-behaviors).

### 5.4 Optional Behaviors

Optional Behaviors defined in [Section 4.2](#42-optional-behaviors) **MAY** be implemented by any conformant implementation.

---

## 6 Security Considerations

TAMOS provides **no security guarantees** of any kind.

All security concerns **MUST** be defined by the implementation.

---

## 7 Error Handling

TAMOS does **not** define any error conditions or error‑handling semantics.

Any behavior resulting from invalid input, malformed Stars, unavailable Horizons, or implementation‑specific failures is **entirely outside the scope** of this specification and **MUST** be defined by the implementation.

---

## 8 Interoperability Considerations

TAMOS does **not** define any interoperability requirements between independent implementations.

Any behavior involving federation, replication, migration, synchronization, or cross‑Sky interaction is **outside the scope** of this specification and **MUST** be defined by the participating implementations.

---

## 9 Versioning

TAMOS does **not** define how different versions of TAMOS should interact.

If an implementation needs rules for compatibility or version negotiation, it **MUST** define them itself.
