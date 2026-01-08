

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from src.validation.gem_validator import validate_gem
from src.storage.id_allocator import get_next_id
from src.storage.writer import write_gem
from datetime import date

router = APIRouter()

@router.post("/submit", status_code=201)
async def submit_gem(request: Request):
	try:
		gem = await request.json()
	except Exception:
		return JSONResponse(status_code=400, content={"error": "Invalid JSON"})

	# Validate only url, description, author (author optional)
	valid, error = validate_gem(gem)
	if not valid:
		return JSONResponse(status_code=400, content={"error": "Validation failed", "details": error})

	# Add date field (current date, ISO format)
	gem_with_date = dict(gem)
	gem_with_date["date"] = date.today().isoformat()

	gem_id = get_next_id()
	try:
		write_gem(gem_with_date, gem_id)
	except Exception as e:
		return JSONResponse(status_code=500, content={"error": "Failed to store gem", "details": str(e)})

	return {"id": gem_id}
