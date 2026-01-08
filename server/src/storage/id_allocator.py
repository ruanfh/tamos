
import os
import re

ARCHIVE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'archive')

def get_next_id() -> int:
	"""
	Scans the archive directory for numeric .json files and returns the next available integer ID.
	"""
	os.makedirs(ARCHIVE_DIR, exist_ok=True)
	max_id = 0
	for fname in os.listdir(ARCHIVE_DIR):
		match = re.fullmatch(r"(\d+)\.json", fname)
		if match:
			file_id = int(match.group(1))
			if file_id > max_id:
				max_id = file_id
	return max_id + 1
