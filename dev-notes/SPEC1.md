
# TAMOS Protocol Specification

## 1. Purpose

TAMOS defines a minimal contract between three roles: Client, Node, and Consumer; for submitting, storing, and exposing structured information.

The protocol specifies the lifecycle of a Gem, the creation of Entries, and the exposure of Archives.
TAMOS does **not** prescribe storage formats, transport mechanisms, or API structures.

---

## 2. Roles

### 2.1 Client
A Client is any actor capable of submitting a Gem to a Node.

### 2.2 Node
A Node receives Gems, turns them into Entries, and exposes Archives to Consumers.

### 2.3 Consumer
A Consumer reads Archives exposed by a Node. Consumers do not submit Gems.

---

## 3. Objects

### 3.1 Gem
A Gem is a JSON object submitted by a Client.  
A Gem **MUST** conform to the TAMOS Gem Submission Schema.

### 3.2 Entry
An Entry is a JSON object created by the Node from a Gem.  
Nodes **MAY** add metadata, modify entries, or delete entries.  
TAMOS does **not** enforce immutability.

### 3.3 Archive
An Archive is a collection of Entries exposed by the Node.  
The structure and organization of an Archive are Node‑defined.

---

## 4. Required Behaviors

### 4.1 Client Requirements
- A Client **MUST** provide a way to submit a Gem to a Node.

### 4.2 Node Requirements
- A Node **MUST** provide an append mechanism that accepts Gems.
- A Node **MUST** transform each submitted Gem into an Entry.
- A Node **MUST** expose Entries through one or more Archives.
- A Node **MUST** preserve the Gem’s structure exactly as submitted.
- A Node **MAY** modify the values inside that structure.
- A Node **MAY** add metadata to Entries.
- A Node **MAY** edit or delete Entries, but such edits **MUST NOT** alter the Gem’s structure.
- A Node **MAY** organize Archives in any structure.

### 4.3 Consumer Requirements
- A Consumer **MUST** be able to read Archives in whatever structure the Node exposes.

---

## 5. Protocol Flow

1. **Submit** — The Client submits a Gem to the Node.
2. **Append** — The Node accepts the Gem and creates an Entry.
3. **Expose** — The Node makes Entries available inside one or more Archives.
4. **Consume** — Consumers read the Archives.

This is the complete TAMOS lifecycle.

---

## 6. Gem Schema

The TAMOS Gem Submission Schema is the only normative schema in the protocol.  
All Gems **MUST** validate against this schema.  
[gem.submit.schema.json](gem.submit.schema.json)

---

## 7. Non‑Normative Areas

The protocol does **not** define:

- storage formats
- directory structures
- API endpoints
- pagination
- authentication
- metadata formats
- indexing or search
- transport mechanisms

These are implementation details left to Nodes.
