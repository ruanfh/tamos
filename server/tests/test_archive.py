def test_archive_empty(client):
    response = client.get("/archive/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "gems" in data
    assert isinstance(data["gems"], list)
    assert data["gems"] == []

def test_archive_with_data(client):
    # Submit a valid gem
    valid_payload = {
        "url": "https://example.com",
        "description": "A test gem.",
        "author": "Test Author"
    }
    submit_response = client.post("/submit", json=valid_payload)
    assert submit_response.status_code in (200, 201)
    gem_id = submit_response.json().get("id")
    assert gem_id is not None

    # Check archive
    archive_response = client.get("/archive/")
    assert archive_response.status_code == 200
    data = archive_response.json()
    assert isinstance(data, dict)
    assert "gems" in data
    gems = data["gems"]
    assert isinstance(gems, list)
    # There should be at least one gem
    assert any(gem.get("id") == gem_id for gem in gems)
