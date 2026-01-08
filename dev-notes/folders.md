tamos/
│
├── protocol/              # The normative specification (the contract)
│   ├── protocol.md
│   ├── archive.md
│   ├── glossary.md
│   └── gem.schema.json
│
├── reference/             # Implementation #1: static archive
│   ├── archive/
│   │   ├── 1.json
│   │   ├── 2.json
│   │   └── ...
│   └── README.md
│
├── server/                # Implementation #2: TAMOS server API
│   ├── src/
│   │   ├── index.js       # or main.py, main.rs, etc.
│   │   ├── storage/       # file-based, sqlite, KV, etc.
│   │   ├── routes/
│   │   │   ├── submit.js
│   │   │   ├── archive.js
│   │   │   └── health.js
│   │   └── validation/
│   │       └── gemValidator.js
│   ├── tests/
│   ├── package.json       # or pyproject.toml, Cargo.toml, etc.
│   └── README.md
│
├── client/                # Implementation #3: CLI / SDK
│   ├── src/
│   │   ├── cli.js         # or cli.py, cli.rs
│   │   ├── commands/
│   │   │   ├── submit.js
│   │   │   ├── validate.js
│   │   │   ├── fetch.js
│   │   │   └── crawl.js
│   │   └── utils/
│   ├── package.json
│   └── README.md
│
├── docs/                  # Human-friendly conceptual docs
│   ├── what.md
│   ├── why.md
│   ├── how.md
│   └── architecture.md
│
└── README.md              # High-level overview of the whole project