def test_root_redirect(client):
    response = client.get("/")
    assert response.status_code == 307 or response.status_code == 308  # Redirect
    # location header points to static index
    assert response.headers["location"].endswith("/static/index.html")
