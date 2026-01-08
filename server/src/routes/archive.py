
from fastapi import APIRouter
import os
import json

router = APIRouter()

ARCHIVE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'archive')

@router.get("/archive/")
def list_archive():
	gems = []
	if os.path.exists(ARCHIVE_DIR):
		for fname in os.listdir(ARCHIVE_DIR):
			if fname.endswith('.json') and fname[:-5].isdigit():
				gem_id = int(fname[:-5])
				gems.append({"id": gem_id, "path": f"/archive/{gem_id}.json"})
	gems.sort(key=lambda x: x["id"])
	return {"gems": gems}


from fastapi import HTTPException

@router.get("/archive/{gem_id}")
def get_gem(gem_id: int):
	gem_path = os.path.abspath(os.path.join(ARCHIVE_DIR, f"{gem_id}.json"))
	if not os.path.exists(gem_path):
		raise HTTPException(status_code=404, detail="Gem not found")
	with open(gem_path, 'r', encoding='utf-8') as f:
		return json.load(f)
