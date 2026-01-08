# TAMOS Server Architecture

The TAMOS Server is a minimal reference implementation of a TAMOS‑compatible node.  
Its purpose is to demonstrate how a platform can accept gem submissions, validate them, store them, and expose a public archive that follows the TAMOS protocol.  
This server is intentionally simple. It is not a framework, not a platform, and not a federation layer. It is a teaching tool and a reference implementation.

---

## Goals

- Provide a clean example of how to implement a TAMOS node.
- Accept gem submissions via a simple HTTP API.
- Validate gems against the official schema.
- Store gems in a predictable, append‑only archive.
- Expose the archive as static JSON files.
- Remain minimal, transparent, and easy to fork.

The server does **not** implement sync, federation, user accounts, ranking, or moderation logic.  
Those are platform‑level concerns, not protocol concerns.

---

## High‑Level Overview

`Client → POST /submit → Validation → Storage → /archive/{id}.json → AI Crawlers`

---

## Responsibilities

The server has three responsibilities:

1. **Accept gems**  
     Receive a JSON payload from a client (CLI, script, UI, etc.).
2. **Validate gems**  
     Ensure the payload matches the TAMOS gem schema.
3. **Store gems**  
     Assign the next numeric ID and write the gem to disk as `archive/{id}.json`.

Everything else — discovery, indexing, ranking, linking; is handled by AI crawlers following the protocol.

---

## Directory Structure

```text
server/
└── src/
    ├── main.py (or index.js, depending on stack)
    ├── routes/
    │   ├── submit.py
    │   ├── archive.py
    │   └── health.py
    ├── storage/
    │   ├── writer.py
    │   ├── reader.py
    │   └── id_allocator.py
    ├── validation/
    │   └── gem_validator.py
    └── docs/
        └── architecture.md   ← this file
```

This structure keeps concerns separated and the codebase easy to navigate.

---

## Components

### 1. Routes

- `/submit`  
    Accepts a gem via POST.  
    **Flow:**
    - Parse JSON
    - Validate
    - Allocate next ID
    - Write file
    - Return `{ "id": n }`
- `/archive/{id}`  
    Serves a single gem file.
- `/archive/`  
    Lists all gem files (directory listing or JSON index).
- `/health`  
    Simple health check endpoint.

### 2. Validation Layer

Located in `validation/gem_validator.py`.

**Responsibilities:**
- Load the official `gem.submit.schema.json`
- Validate incoming gems
- Return structured errors if invalid

This ensures all gems stored by the server are protocol‑compliant.

### 3. Storage Layer

Located in `storage/`.

- `id_allocator.py`: Reads the archive directory, finds the highest numeric filename, and returns the next integer.
- `writer.py`: Writes a gem to:
    - `archive/{id}.json`
    - Ensures atomic writes to avoid corruption.
- `reader.py`: Reads gems or lists the archive directory.

---

## Archive Format

The server stores gems exactly as the protocol defines:

```text
archive/
├── 1.json
├── 2.json
└── 3.json
```

No padding.  
No metadata files.  
No indexes required.  
AI crawlers enumerate the directory, sort numerically, and process each gem.

---

## Why This Architecture Works

- **Minimal:** No unnecessary abstractions.
- **Predictable:** File‑based storage is transparent and durable.
- **Portable:** Runs on any environment (Windows, Linux, macOS).
- **AI‑Native:** Exposes a clean, crawlable archive.
- **Extensible:** Platforms can add auth, moderation, dashboards, etc.

The server is **not** meant to be “the official TAMOS platform.”  
It is a reference implementation that demonstrates the protocol in its purest form.

---

## Non‑Goals

The server intentionally does **not** implement:

- Sync between nodes
- Federation
- Ranking or scoring
- User accounts
- Moderation
- Deletion or editing of gems
- Complex metadata
- Search

These are platform‑level features, not protocol features.

---

## Philosophy

The TAMOS Server exists to show one thing clearly:

> **A TAMOS node is just a folder of JSON files.**

Everything else is optional.

---

## Duplicates

A TAMOS node allows duplicate gems and does not attempt to detect or prevent them. This is intentional. The server is an append‑only, non‑editorial reference implementation whose sole responsibilities are validation, ID allocation, and storage. Determining whether two gems are “duplicates” is a platform‑level concern, not a protocol concern: similarity can depend on URL normalization, content semantics, author intent, or temporal context, none of which belong in the server layer. Allowing duplicates keeps the archive predictable, immutable, and easy for AI crawlers to process. Platforms built on top of TAMOS may choose to merge, collapse, rank, or annotate duplicates, but the reference server must remain neutral and accept all valid gems as submitted.

---

This architecture keeps the protocol small, the implementation simple, and the ecosystem open.
