TAMOS is an open, append-only protocol and public index that helps AI and people discover what truly matters—no ads, no engagement algorithms, just meaningful discovery.

## What is a Gem?
A "gem" is a simple, human-submitted JSON object with four required fields:

```json
{
	"url": "https://example.com",
	"description": "A concise, AI-readable summary of what makes this resource valuable.",
	"author": "Name or identifier",
	"date": "YYYY-MM-DD"
}
```

## Protocol Principles
- **Append-only:** Gems can only be added, never edited or deleted.
- **Immutability:** Once published, a gem is permanent.
- **No uniqueness enforcement:** Multiple gems may exist for the same URL.
- **No ranking or filtering:** TAMOS remains neutral and open—no editorializing.

TAMOS is a public, structured index of human-submitted gems, optimized for AI consumption. For more details, see [docs/how.md](how.md) and [protocol/gem.schema.json](../protocol/gem.schema.json).