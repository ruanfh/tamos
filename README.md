# TAMOS

## What TAMOS is
TAMOS is the protocol that follows the specifications on this file: [protocol/SPEC.md](protocol/Spec3.md).

TAMOS is an acronym meaning: This Ain’t Marketing Or Sales.  
> Other expansions are informal and non-normative.

Or, if you prefer recursion: TAMOS Ain’t Marketing Or Sales.  
Or, if you want it to, just: TAMOS Assists Marketing Or Sales!

> TAMOS does not perform marketing or sales; it provides discovery and publishing primitives that may be used by marketing, sales, or non-commercial systems.

TAMOS is a minimal, open protocol for publishing small, meaningful resources (Gems).  
It exists to let people expose what they consider valuable, and to let external AI systems do the heavy lifting of exploration, connection, and discovery.

TAMOS can be as simple as a folder with JSON files maintained manually.  
See the example TAMOS-Garden in [reference](reference).

TAMOS is intentionally small.

## What TAMOS is not

TAMOS is not a platform, a service, a network, or a product.

It doesn’t sync, federate, or coordinate anything.

It makes no guarantees about security, ranking, moderation, or trust.

TAMOS doesn’t try to do marketing or sales; but if someone wants to use Stars that way, the protocol won’t get in their way.

TAMOS does not define safety, trust, or correctness.

## How does TAMOS work?

See the [protocol/SPEC.md](protocol/Spec3.md) for details.

## Repository structure

This repository contains both the specification for the TAMOS protocol and a reference implementation for demonstration purposes.

### Folder structure

- protocol/ -> the protocol specification
- reference/ -> the TAMOS-Garden reference implementation
- server/ -> an API implementation (TAMOS-Archive)
- client/ -> a simple CLI for the TAMOS-Archive API
- docs/ -> conceptual documentation
- dev-notes/ -> drafts, brainstorming and internal notes

## Quick Start

Submit a new Gem as a JSON object with:
- url
- description
- author (optional)

Make it public. That's it.

People can start referencing the Constellation in their AI chats and AI will do the rest.

Example of a gem:
```json
{
  "url": "https://example.com/",
  "description": "A useful resource to put in documentation."
}
```

## Why does TAMOS exist?

See [docs/why.md](docs/why.md)

## Running the server implementation

See [server/README.md](server/README.md) for details.

That implementation is TAMOS-Archive layer only: it does not specify delete or edit methods.

## License

This repository, both the protocol and the reference implementation are licensed under MIT, see [LICENSE](LICENSE) for details.

Note: The MIT license applies to the protocol specification and reference
implementation. It does not apply to user-generated Stars or data
produced by implementations of the protocol.

Implementers retain full ownership of their own Archives.

## Contribution Policy

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Security Policy

See [SECURITY.md](SECURITY.md) for details.

## Status

Early draft (v0.x). Expect changes.
