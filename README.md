# TAMOS

TAMOS stands for: This Ain’t Marketing Or Sales.
Or, if you prefer recursion: TAMOS Ain’t Marketing Or Sales.

What it is about is simple:
- Exposing hidden gems to the people who actually need them; with AI doing the heavy lifting.

TAMOS is a minimal, open protocol for publishing and discovering resources (“gems”) without marketing, manipulation, or algorithmic gate‑keeping.
It’s designed for humans to publish and for AI to explore, connect, and surface what matters.

Spoiler: Nodes discover each other simply by being added as gems; no sync, no federation, no extra protocol. AI follows the links and builds the network.


## Repository structure
This repository contains both the specification for the TAMOS protocol and a reference implementation for demonstration purposes.

### Folder structure
- protocol/ -> the specification
- reference/ -> the reference implementation (TAMOS can be as simple as a folder with JSON files maintained manually)
- server/ -> an API implementation
- client/ -> a simple cli for any TAMOS API
- docs/ -> conceptual docs (what/why/how/who)

## Terminology
See [protocol/glossary.md](protocol/glossary.md)

## What is TAMOS?
See [docs/what.md](docs/what.md)

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
- author (optional, can be an email)
The node must fill the date
- date

Make it public. That's it.

People can start referencing the archive in their AI chats and AI will do the rest.

See [protocol/README.md](protocol/README.md) for details.

## Running the reference implementation
See [server/README.md](server/README.md) for details.

That implementation is TAMOS layer only, and does not specify delete or edit methods, which are strongly recommended to be implemented at the platform level.

## License
This repository, both the protocol and the reference implementation are licensed under MIT, see [LICENSE](LICENSE) for details.

Note: The MIT license applies to the protocol specification and reference
implementation. It does not apply to user-generated archives or data
produced by implementations of the protocol.

## Contributions
Contributions are welcome, but the protocol is still stabilizing. Feel free to open issues for discussion.

## Status
Early draft (v0.x). Expect changes.
