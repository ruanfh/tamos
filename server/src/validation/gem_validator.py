

import json
from jsonschema import validate, ValidationError
from pathlib import Path

# Reference the protocol/gem.schema.json from the project root
SCHEMA_PATH = Path(__file__).resolve().parents[3] / "protocol" / "gem.schema.json"

with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
	GEM_SCHEMA = json.load(f)

def validate_gem(gem: dict) -> (bool, dict):
	"""
	Validates a gem dict against the gem.schema.json.
	Returns (True, None) if valid, (False, error_details) if invalid.
	"""
	try:
		validate(instance=gem, schema=GEM_SCHEMA)
		return True, None
	except ValidationError as e:
		return False, {"error": str(e), "details": e.schema_path}
