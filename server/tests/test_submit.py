def test_submit_invalid(client):
    # Missing required fields: should fail
    response = client.post("/submit", json={})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] in ("Invalid JSON", "Validation failed")
    # Optionally, check for details key
    # assert "details" in data

def test_submit_valid(client):
    # Valid payload according to gem.schema.json
    valid_payload = {
        "url": "https://example.com",
        "description": "A test gem.",
        "author": "Test Author"
    }
    response = client.post("/submit", json=valid_payload)
    assert response.status_code in (200, 201)
    # Optionally, check response content structure
    # assert "id" in response.json() or similar
