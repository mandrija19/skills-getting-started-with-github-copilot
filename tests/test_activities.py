def test_get_activities(client):
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    # basic structural checks
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
