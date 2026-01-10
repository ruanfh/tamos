# TAMOS

## What is TAMOS
TAMOS is an acronym meaning: This Ain’t Marketing Or Sales.  
Or, if you prefer recursion: TAMOS Ain’t Marketing Or Sales.

TAMOS is a minimal, open protocol for publishing and discovering small, meaningful resources (“gems”).  
It exists to let people expose what they consider valuable; and to let external AI systems do the heavy lifting of exploration, connection, and discovery.

TAMOS can be as simple as a folder with JSON files maintained manually.  
Like the example Archive in [reference](reference).

Spoiler: Nodes discover each other simply by being added as gems.  
No sync. No federation. No extra protocol.  
AI follows the links and builds the network.

TAMOS is intentionally small.  

## What TAMOS is not

TAMOS is not a platform, a service, a network, or a product.  
It doesn’t sync, federate, or coordinate anything.  
It makes no guarantees about security, ranking, moderation, or trust.

TAMOS doesn’t try to do marketing or sales; but if someone wants to use gems that way, the protocol won’t get in their way.

## Repository structure

This repository contains both the specification for the TAMOS protocol and a reference implementation for demonstration purposes.

### Folder structure

- protocol/ -> the protocol specification
- reference/ -> the reference implementation
- server/ -> an API implementation (TAMOS-2x2)
- client/ -> a simple cli for the implemented TAMOS API (TAMOS-2x2)
- docs/ -> conceptual docs

## Terminology

See [docs/glossary.md](docs/glossary.md)

## Why does TAMOS exist?

See [docs/why.md](docs/why.md)

## How does TAMOS work?

See [docs/how.md](docs/how.md)

## Who is TAMOS for?

See [docs/who.md](docs/who.md)

## Quick Start

Submit a new gem as a JSON object with:
- url
- description
- author (optional)

Make it public. That's it.

People can start referencing the archive in their AI chats and AI will do the rest.

See [protocol/SPEC.md](protocol/SPEC.md) for details.

## Running the server implementation

See [server/README.md](server/README.md) for details.

That implementation is TAMOS layer only, and does not specify delete or edit methods, which are strongly recommended to be implemented at the platform level.

## Gates

TAMOS defines optional Input and Output Gates that describe how a Node accepts Gems (TIG) and exposes Archives (TOG).

See [docs/gates.md](docs/gates.md) for details.

## License

This repository, both the protocol and the reference implementation are licensed under MIT, see [LICENSE](LICENSE) for details.

Note: The MIT license applies to the protocol specification and reference
implementation. It does not apply to user-generated archives or data
produced by implementations of the protocol.

## Contribution Policy

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Status

Early draft (v0.x). Expect changes.
