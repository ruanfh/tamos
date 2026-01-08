
# TAMOS Protocol

> TAMOS is a minimal, open protocol for publishing “gems” — small, structured JSON objects that describe valuable resources.  
> The protocol defines what a gem is, how gems are published, and how nodes expose their archives.  
> It does **not** define platform features such as accounts, moderation, ranking, or deletion.  
> TAMOS is intentionally small, neutral, and easy to implement.

---

## 1. Gem Definition


A gem is the atomic unit of TAMOS.  
It is a JSON object with **two required fields** (the server will add the date, and author is optional):

```json
{
  "url": "https://example.com",
  "description": "A concise, AI-readable summary of what makes this resource valuable."
  // "author": "Name or identifier" (optional)
}
```

When a gem is submitted, the server will set the `date` field to the current date (YYYY-MM-DD) before storing and exposing it in the archive. The `author` field is optional and may be omitted or left blank.

The formal schema is defined in `gem.schema.json`.

**Immutability:**  
Once a gem is published, its content **MUST NOT** change.  
This is the only immutability guarantee enforced by the protocol.

---

## 2. Publishing a Gem

Publishing a gem means submitting a valid gem object to a TAMOS node.

A node **MUST**:

- validate the gem against `gem.schema.json`
- assign any node-specific metadata (optional)
- expose the gem in its public archive

A node **MAY**:

- reject invalid gems
- apply rate limits
- require authentication
- enforce platform-level policies

These behaviors are **outside the scope** of the protocol.

---

## 3. Archive Exposure

Each node exposes its collection of gems as an **archive**.  
The archive is the public interface that clients, crawlers, and other nodes read.

Nodes **MAY** expose their archive as:

- a directory of JSON files
- a JSONL log
- a paginated feed
- any other stable, documented format

See `archive.md` for the full archive specification.

---

## 4. Node Responsibilities

A TAMOS node **MUST**:

- expose its archive publicly
- expose gems in valid JSON form
- preserve gem immutability
- provide a stable way to fetch all visible entries

A TAMOS node **MAY**:

- delete or hide entries (moderation, user deletion, legal compliance)
- reorder entries
- store data in any internal format
- add metadata fields to entries
- implement platform features

These actions do **not** affect protocol compliance.

---

## 5. Platform Responsibilities

Platforms built on TAMOS **MAY** implement:

- user accounts
- editing and deletion at the platform layer
- moderation and policy enforcement
- ranking, filtering, or recommendation
- analytics or additional metadata

These features **MUST NOT** modify the gem format or introduce new required fields.

---

## 6. Interoperability

Clients and crawlers **MUST**:

- accept any archive format defined in `archive.md`
- validate gems using `gem.schema.json`
- treat gems as immutable
- not assume ordering unless explicitly provided

Nodes **SHOULD**:

- document their archive format
- provide stable URLs
- avoid breaking changes

---

## 7. Scope of the Protocol

TAMOS **defines**:

- the gem structure
- gem immutability
- how gems are published
- how archives are exposed

TAMOS **does not define**:

- moderation
- deletion
- ranking or search
- user identity
- platform behavior
- internal storage models

This separation keeps TAMOS minimal, durable, and easy to adopt.

