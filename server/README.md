# Folder structure
```text
server/
├── pyproject.toml
├── .venv/                # created automatically by uv
├── src/
│   ├── main.py
│   ├── routes/
│   │   ├── submit.py
│   │   ├── archive.py
│   │   └── health.py
│   ├── storage/
│   │   ├── writer.py
│   │   ├── reader.py
│   │   └── id_allocator.py
│   ├── validation/
│   │   └── gem_validator.py
│   └── docs/
│       ├── architecture.md
│       └── api.md
└── archive/
    └── (generated gem files: 1.json, 2.json, 3.json…)
```

# Setup in windows with uv
```bash
cd server/
uv init
```

# Installation in windows with uv
```bash
cd server/
uv pip install .
```

# Installation in windows for dev
```bash
cd server/
uv pip install -e .[dev]
```

# Run server (recommended)
```bash
uv run tamos-server
```

# Also run server
```bash
uv run uvicorn src.main:app --reload
```

# Run tests
```bash
uv run pytest tests
```
