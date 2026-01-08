def test_archive_empty(client):
    response = client.get("/archive")
    assert response.status_code == 200
    # Adjust according to your API's response structure
    assert isinstance(response.json(), list)

def test_archive_with_data(client):
    # TODO: Insert data first, then check archive
    pass
