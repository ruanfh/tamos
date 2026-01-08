import json
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".tamos"
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config():
    """Load the config file if it exists. Returns a dict or {}."""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            # Corrupted config → treat as empty
            return {}
    return {}


def save_config(data: dict):
    """Write the config file, creating the directory if needed."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_server_url(cli_value: str | None = None) -> str:
    """
    Determine which server URL to use.
    Priority:
      1. CLI flag
      2. ~/.tamos/config.json
      3. Error (no default)
    """
    # 1. CLI flag wins
    if cli_value:
        return cli_value

    # 2. Config file
    config = load_config()
    if "server" in config:
        return config["server"]

    # 3. No server configured → instruct user
    raise RuntimeError(
        "No TAMOS server configured.\n"
        "Use --server or set a default with:\n"
        "  tamos config set-server https://your-node.com"
    )


def set_server_url(url: str):
    """Update the config file with a new default server URL."""
    config = load_config()
    config["server"] = url
    save_config(config)