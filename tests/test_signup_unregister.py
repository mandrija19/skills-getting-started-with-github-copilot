import pytest


def test_signup_success(client):
    email = "test@mergington.edu"
    activity = "Chess Club"
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert resp.json()["message"].startswith("Signed up")
    # verify via GET
    get_resp = client.get("/activities")
    assert email in get_resp.json()[activity]["participants"]


def test_signup_missing_activity(client):
    resp = client.post("/activities/Nonexistent/signup", params={"email": "x@x.com"})
    assert resp.status_code == 404


def test_signup_duplicate(client):
    # use existing participant from fixture data
    resp = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})
    assert resp.status_code == 400


def test_unregister_success(client):
    email = "michael@mergington.edu"
    activity = "Chess Club"
    resp = client.delete(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert resp.json()["message"].startswith("Unregistered")
    # verify removed
    get_resp = client.get("/activities")
    assert email not in get_resp.json()[activity]["participants"]


def test_unregister_not_registered(client):
    resp = client.delete("/activities/Chess Club/signup", params={"email": "nobody@mergington.edu"})
    assert resp.status_code == 400


def test_unregister_missing_activity(client):
    resp = client.delete("/activities/Unknown/signup", params={"email": "test@x.com"})
    assert resp.status_code == 404
