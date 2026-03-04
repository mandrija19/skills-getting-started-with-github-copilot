import copy
import pytest
from fastapi.testclient import TestClient

from src import app


@pytest.fixture(scope="session")
def client():
    """A test client for the FastAPI app."""
    return TestClient(app.app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the original activities dict after each test."""
    original = copy.deepcopy(app.activities)
    yield
    app.activities.clear()
    app.activities.update(copy.deepcopy(original))
