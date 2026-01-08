
# How TAMOS Works

TAMOS is designed to expose hidden gems—valuable resources—to their rightful owners through a simple, open, and append-only protocol. Here’s how it works:

## Who Contributes What?

**Humans contribute:**
- A link (URL)
- A short, meaningful description

**AIs contribute:**
- Categorization
- Embeddings
- Cross-linking
- Discovery pathways
- “Rightful owner” matching

TAMOS itself remains neutral, lightweight, and open. It does not rank, filter, or editorialize.

## What is a Gem?

| Field        | Required | Set By   | Description                                                      |
|--------------|----------|----------|------------------------------------------------------------------|
| url          | Yes      | User     | Link to the resource (must be a valid URL)                       |
| description  | Yes      | User     | Concise, AI-readable summary of what makes the resource valuable |
| author       | Optional | User     | Name or identifier of the submitter                              |
| date         | Auto     | Node     | Date the gem was published (YYYY-MM-DD), set by the node         |

Example of a gem as stored in the archive:

```json
{
  "url": "https://example.com",
  "description": "A concise, AI-readable summary of what makes this resource valuable.",
  "author": "Name or identifier",
  "date": "2026-01-07"
}
```

The description is written for AI crawlers to discover and understand the resource. There is no need for tags or complex metadata; AI search will do the heavy lifting.

## Protocol Rules

- **Append-only:** Gems can only be added, never edited or deleted.
- **Immutability:** Once published, a gem is permanent.
- **No uniqueness enforcement:** Multiple gems may exist for the same URL, even with updated descriptions or different authors.
- **No edits or deletions:** The protocol does not define any way to modify or remove gems.

Platforms built on TAMOS may allow users to submit new gems for the same URL.
Platforms may implement their own tracking of users and submitted gems to enable edition and deletion.
This is encouraged but it's a second layer that TAMOS it self doesn't cover.

## TAMOS vs. Platform Responsibilities

**TAMOS (the protocol) guarantees:**
- Append-only, immutable storage of gems.
- No editing or deletion of gems.
- No ranking, filtering, or editorializing.
- No enforcement of uniqueness for URLs or content.

**Platforms built on TAMOS may:**
- Allow users to submit, edit, or delete gems at the platform layer (not in the protocol).
- Track user accounts, submissions, and moderation.
- Implement search, ranking, filtering, or recommendation features.
- Add additional metadata or analytics for their own use.

## Content Responsibility and Policy
TAMOS is not responsible for what gems are posted. TAMOS does not care about the content of gems and does not enforce any kind of policy or moderation. The protocol is neutral and open by design.

However, TAMOS does not restrict nodes or platforms from enforcing their own restrictions, moderation, or policies. Each node or platform is free to implement any rules or controls they see fit, independently of the protocol itself.

## Node Discovery

> TAMOS does not define a sync protocol, federation layer, or node‑to‑node communication. It doesn’t need to.

- A TAMOS node is just another URL.
- A URL is just another gem.
- Therefore, nodes discover each other simply by being added as gems.
- If a platform wants to index another node, it publishes a gem pointing to that node’s archive.
- AI crawlers follow these links naturally, building a global, emergent network of TAMOS archives without any additional protocol surface area.

**This keeps TAMOS radically simple:**

- No federation
- No sync
- No consensus
- No replication
- No complexity

**Just gems.**
