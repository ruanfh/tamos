# TAMOS Gates

TAMOS Gates are non‑normative accessibility profiles that describe how a Node may accept Gems and expose Archives. They do not modify the TAMOS Protocol, but define common patterns for input and output behavior. A Node may implement one or more Gates on each side.

---

## 1. TAMOS Input Gates (TIG)

TIGs define how a Node accepts Gems from Clients.

### TIG‑1 -> Manual File Input
- Gems are written manually or by scripts
- No API
- Ideal for:
	- local workflows
	- Git repositories
	- offline or air‑gapped nodes
This is the simplest possible input mechanism.

### TIG‑2 -> Append‑Only API Input
- POST /submit
- Body MUST validate against the Gem Submission Schema
- Node creates an Entry from the Gem
- Node MAY perform garbage collection or metadata enrichment
- Ideal for:
	- LAN setups
	- public submission endpoints
	- hybrid nodes that also expose files

### TIG-3 -> Full API
A richer, more expressive write interface.
- Includes everything from TIG‑2
- MAY include:
- authenticated submission
- batch submission
- editing or deleting entries
- metadata endpoints
- validation endpoints
- rate‑limiting or quotas

---

## 2. TAMOS Output Gates (TOG)

TOGs define how a Node exposes its Archives to Consumers.

### TOG‑1 — Static Folder Output
- archive/ is a folder
- archive/{id} is a JSON file
- Zero server logic
- Ideal for:
	- static hosting
	- local AI
	- GitHub Pages
	- file‑based nodes
This is the most transparent and durable output mechanism.

### TOG‑2 — Read API Output
- GET /archive/ → list of archive IDs
- GET /archive/{id} → entries for that archive
- JSON responses
- Node MAY add pagination, metadata, or computed views
- Ideal for:
	- remote consumers
	- indexing services
	- advanced or dynamic nodes

---

## 3. Gate Matrix

A Node is defined by its combination of one TIG and one TOG.

| TIG / TOG       | TOG-1: Static Folder | TOG-2: Read API |
| --------------- | -------------------- | --------------- |
| TIG-1: Manual   | TAMOS-1x1            | TAMOS-1x2       |
| TIG-2: API      | TAMOS-2x1            | TAMOS-2x2       |
| TIG-3: Full API | TAMOS-3x1            | TAMOS-3x2       |

---

## 4. Normative Status

TIG and TOG are non‑normative recommendations. They are optional architectural patterns that help implementers build interoperable Nodes.

The TAMOS Protocol remains the only normative layer.
