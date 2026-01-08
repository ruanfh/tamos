import json
from jsonschema import Draft7Validator
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "protocol" / "gem.schema.json"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_gem(gem: dict):
    """
    Validate a gem against gem.schema.json.
    Returns a list of error messages (empty list = valid).
    """
    schema = load_schema()
    validator = Draft7Validator(schema)

    errors = []
    for error in validator.iter_errors(gem):
        errors.append(error.message)

    return errors