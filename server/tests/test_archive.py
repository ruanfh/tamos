def test_archive_empty(client):
    response = client.get("/archive/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "gems" in data
    assert isinstance(data["gems"], list)
    assert data["gems"] == []

def test_archive_with_data(client):
    # TODO: Insert data first, then check archive
    pass
