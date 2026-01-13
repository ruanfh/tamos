# TAMOS

TAMOS is defined by the specification in [protocol/SPEC.md](protocol/SPEC.md).

> Only [protocol/SPEC.md](protocol/SPEC.md) and [protocol/gem.submit.schema.json](protocol/gem.submit.schema.json) are authoritative.

This repository exists to host:
- The TAMOS protocol specification
- Non-normative reference material and implementations

## Problem

Let's say person A wants X, and Person B offers X.
How to connect person A with person B.
The channel already exist: the internet.
But here comes the real problem: how B stand out? And how A is directed precisely to B.
If X is already popular it's easy because search engines are optimized for that already.
But what if X is rare or new?
B won't stand out and A will only get noise.

## Solution

TAMOS exist not to directly solve it by it self, but to provide a standardized layer in that direction.
We already have AI chats that can do the heavy lifting of categorizing large sets of data.
And we already have countless active people in the internet.

TAMOS provide a standard language-agnostic way for people to contribute with Gems which consists of a url and a description.

That way large sets of unusual or unique data that may not fit anywhere else can be gathered in a environment, a Sky, think of it as a server, a site, or even a local file.

Now let's say person B put X's url and its description on a Sky.
Person A can search the whole Sky by pointing an automated agent to it. 

## Limitation

This is an experimental concept, to check would require large amounts of real data to be properly verified.

## Positive side effects

TAMOS can be used in private setups. Even though it's meant for the internet.

## Scope

TAMOS is a minimal protocol meant for revealing small, meaningful resources for machines to later explore.

It defines concepts and rules only.

It does not define platforms, services, networks, guarantees, or behavior beyond what is explicitly stated in the specification.

## Repository

```text
protocol/  -> TAMOS protocol specification
example/   -> Example JSON only implementation
server/    -> Example API implementation
client/    -> Example CLI
docs/      -> Conceptual notes
dev-notes/ -> Drafts and internal material
```

## Status

Early draft (v0.x).
Expect changes.

> Earlier commits reflect exploratory drafts and design evolution.

## Why

See [docs/why.md](docs/why.md) (non-normative).

## License

MIT. See [LICENSE](LICENSE).

User-generated data is not covered by this license.

## Contribution Policy

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security Policy

See [SECURITY.md](SECURITY.md).
