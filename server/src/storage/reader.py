
import os
import json

ARCHIVE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'archive')

def list_gems():
	"""Return a sorted list of all gem IDs in the archive directory."""
	if not os.path.exists(ARCHIVE_DIR):
		return []
	ids = []
	for fname in os.listdir(ARCHIVE_DIR):
		if fname.endswith('.json') and fname[:-5].isdigit():
			ids.append(int(fname[:-5]))
	return sorted(ids)

def read_gem(gem_id: int):
	"""Read and return the gem dict for the given ID, or None if not found."""
	gem_path = os.path.abspath(os.path.join(ARCHIVE_DIR, f"{gem_id}.json"))
	if not os.path.exists(gem_path):
		return None
	with open(gem_path, 'r', encoding='utf-8') as f:
		return json.load(f)
