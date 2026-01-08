import json
from jsonschema import Draft7Validator
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "protocol" / "gem.submit.schema.json"


def load_submit_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_gem_submission(gem: dict):
    """
    Validate a gem submission against gem.submit.schema.json.
    Returns a list of error messages (empty list = valid).
    """
    schema = load_submit_schema()
    validator = Draft7Validator(schema)

    errors = []
    for error in validator.iter_errors(gem):
        errors.append(error.message)

    return errors