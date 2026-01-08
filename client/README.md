
# Quick start

## Install dependencies (from client/)

```bash
cd client/
uv pip install -e .
```

## Run commands

### Submit a gem
```bash
uv run tamos submit --url "https://example.com" --description "A short description." --author "Your Name"
```

### Validate a gem (locally, no server)
```bash
uv run tamos validate --url "https://example.com" --description "A short description."
```

### Set default server
```bash
uv run tamos config set-server http://localhost:8000
```

### Show current config
```bash
uv run tamos config show
```

# For devs

## Install
```bash
cd client/
uv pip install -e .[dev]
```

## Running tests

To run all client tests:

```bash
cd client/
uv run pytest tests
```

# Folder structure
```text
client/
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── config.py
│   ├── validator.py
│   ├── submitter.py
│   └── docs/
│       ├── usage.md
│       └── architecture.md
```