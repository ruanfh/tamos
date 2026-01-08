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
uv add fastapi uvicorn
```

# Installation in windows with uv
```bash
cd server/
uv sync
```

# Run server
```bash
uv run dev
```