
# How TAMOS Works

TAMOS is designed to expose hidden gems—valuable resources—through a simple, open protocol. Here’s how it works:

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

| Field       | Required | Description                                                      |
| ----------- | -------- | ---------------------------------------------------------------- |
| url         | Yes      | Link to the resource (must be a valid URL)                       |
| description | Yes      | Concise, AI-readable summary of what makes the resource valuable |
| author      | Optional | Name or identifier of the submitter                              |

Example of a Gem as stored in the Archive:

```json
{
  "url": "https://example.com",
  "description": "A concise, AI-readable summary of what makes this resource valuable.",
  "author": "Name or identifier",
}
```

The description is written for AI Consumers to discover and understand the resource. There is no need for tags or complex metadata; AI search will do the heavy lifting.

## TAMOS vs. Platform Responsibilities

**TAMOS (the protocol) guarantees:**
- Gems can be submitted by the client and appended by the node.
- The Archive will be available for the intended Consumer.

That's it.

**Platforms built on TAMOS may:**
- Allow users to submit, edit, or delete gems.
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
- AI Consumers follow these links naturally, building network of TAMOS Archives without any additional protocol surface area.

**This keeps TAMOS radically simple:**

- No federation
- No sync
- No consensus
- No replication
- No complexity

**Just gems.**
