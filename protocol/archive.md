# TAMOS Archive Specification
The TAMOS Archive defines how a node exposes its collection of gems so that clients, crawlers, and other nodes can read it.
This specification describes the public interface only.
It does not define how nodes store data internally or how platforms manage user‑level features.

---

## 1. Archive Location

A node **MUST** expose its archive at a stable, publicly accessible URL.

**Examples:**

```
/archive/
/gems/
/tamos/
```

The exact path is implementation‑specific.

---

## 2. Archive Format

A node **MAY** expose its archive in any of the following formats:

**A. Directory of JSON files (recommended):**

```
/archive/
  000001.json
  000002.json
  000003.json
```

Each file represents a single gem entry.

**B. JSON Lines (JSONL) log:**

```
/archive.jsonl
```

Each line is a gem entry.

**C. Paginated JSON feed:**

```
/archive?page=1
/archive?page=2
```

Nodes are free to choose any format.  
Clients **MUST** be prepared to handle any of the above.

---

## 3. Entry Format

Each exposed entry **MUST**:

- be valid JSON
- conform to `gem.schema.json`
- contain the four required gem fields
- be immutable once published

Nodes **MAY** add metadata fields (e.g., `id`, `timestamp`), but:

- **MUST NOT** override gem fields
- **MUST NOT** introduce new required fields

**Example:**

```json
{
  "url": "...",
  "description": "...",
  "author": "...",
  "date": "2026-01-07",
  "id": "000001",
  "timestamp": "2026-01-07"
}
```

---

## 4. Immutability (Protocol-Level)

The gem itself is **immutable**:

- Once a gem is published, its content **MUST NOT** change.

This is the only immutability guarantee enforced by the TAMOS protocol.

---

## 5. Node Freedom (Implementation-Level)

Nodes and platforms **MAY**:

- delete entries
- hide entries
- reorder entries
- apply moderation
- allow user-level deletion
- maintain internal databases
- store gems in any format

These actions are **outside the scope** of the TAMOS protocol.  
TAMOS defines the structure of gems and how they are exposed — **not** how nodes manage them internally.

---

## 6. Ordering

A node **MAY** expose entries in chronological order, but this is **NOT** required.

- If ordering is provided, clients **MAY** use it for incremental crawling.
- If ordering is not provided, clients **MUST NOT** assume any ordering.

This keeps the protocol flexible and static‑hosting‑friendly.

---

## 7. Discovery Requirements

A node **MUST** expose a way for clients to:

- fetch the entire archive
- fetch all entries currently visible in the archive

This can be done via:

- directory listing
- JSONL log
- pagination
- any other stable mechanism

The protocol does **not** mandate a specific discovery method.

---

## 8. Content Responsibility

TAMOS is **neutral**.

Nodes and platforms are responsible for:

- moderation
- policy
- user deletion
- legal compliance

The protocol does **not** enforce or define any of these.
