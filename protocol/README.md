
# TAMOS Protocol

This folder contains the **formal, normative specification** of TAMOS — the minimal, open protocol for publishing “gems” (structured JSON objects describing valuable resources).

Everything here defines the contract that all TAMOS‑compatible nodes, clients, and crawlers must follow.  
TAMOS is intentionally small, neutral, and easy to implement.

---

## Contents

- **protocol.md**  
	The core specification.  
	Defines what a gem is, how gems are published, and what responsibilities nodes and platforms have.
- **archive.md**  
	The archive exposure specification.  
	Defines how a node exposes its collection of gems so clients and crawlers can read it.
- **glossary.md**  
	Canonical definitions of protocol terms such as gem, archive, entry, node, client, and platform.
- **gem.schema.json**  
	The machine‑readable schema for gems.  
	All gems **MUST** validate against this schema.

---

## What This Folder Represents

The files in this folder define:

- the gem format
- the immutability guarantee
- the rules for publishing gems
- the public interface of a node’s archive
- the shared vocabulary used across the protocol

These documents are **normative** — meaning they define what it means to be TAMOS‑compatible.  
Everything else in the repository (examples, docs, implementation) is **informative**.

---

## What TAMOS Does Not Define

TAMOS does **not** define:

- user accounts
- moderation or policy
- deletion or editing
- ranking, filtering, or search
- internal storage models
- platform behavior

These are left entirely to nodes and platforms.

---

## Implementing TAMOS

If you are building a TAMOS node or client:

1. **Start with** `protocol.md`
2. **Validate gems** using `gem.schema.json`
3. **Expose your archive** according to `archive.md`
4. **Use the vocabulary** in `glossary.md`

This is all you need to be compliant.
