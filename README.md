# TAMOS

TAMOS stand for: This Ain't Marketing Or Sales.
Or TAMOS Ain't Marketing Or Sales, if you will.
What it actually is about:
- Exposing hidden gems to the rightful owners.

TAMOS is a minimal, open protocol for publishing and discovering resources (“gems”) without marketing, manipulation, or algorithmic gate-keeping.

TAMOS is append‑only: once a gem is published, it is never modified or removed; only superseded.

## Repository structure
This repository contains both the specification for the TAMOS protocol and a reference implementation for demonstration purposes.
Folder structure:
- protocol/ -> the specification
- src/ -> the reference implementation
- examples/ -> sample manifests
- docs/ -> conceptual docs (what/why/how/who)

## What is TAMOS?
See [docs/what.md](docs/what.md)

## Why does TAMOS exist?
See [docs/why.md](docs/why.md)

## How does TAMOS work?
See [docs/how.md](docs/how.md)

## Who is TAMOS for?
See [docs/who.md](docs/who.md)

## Quick Start: Add a Gem
Submit a new gem as a JSON object with:
- url
- description
- author
- date

See [protocol/README.md](protocol/README.md) for details.

## Running the reference implementation
See [src/README.md](src/README.md) for details.

That implementation is TAMOS layer only, and does not specify delete or edit methods, which are strongly recommended to be implemented at the platform level.

## License
This repository, both the protocol and the reference implementation are licensed under MIT, see [LICENSE](LICENSE) for details.

## Contributions
Contributions are welcome, but the protocol is still stabilizing. Feel free to open issues for discussion.

## Status
Early draft (v0.x). Expect changes.
