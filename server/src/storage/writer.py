
import json
import os
import tempfile

ARCHIVE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'archive')

def write_gem(gem: dict, gem_id: int) -> None:
	"""
	Atomically write the gem dict to archive/{id}.json
	"""
	os.makedirs(ARCHIVE_DIR, exist_ok=True)
	target_path = os.path.abspath(os.path.join(ARCHIVE_DIR, f"{gem_id}.json"))
	# Write to a temp file first
	with tempfile.NamedTemporaryFile('w', dir=ARCHIVE_DIR, delete=False, encoding='utf-8') as tmp:
		json.dump(gem, tmp, ensure_ascii=False, indent=2)
		tmp.flush()
		os.fsync(tmp.fileno())
		temp_path = tmp.name
	# Atomically move temp file to target
	os.replace(temp_path, target_path)
