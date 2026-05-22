import pytest

from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.entries = []
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_entry(client, app):
    client.post("/entries/new", data={
        "date": "2026-01-01",
        "subject": "math",
        "notes": "algebra"
    })

    assert len(app.entries) == 1
    assert app.entries[0]["subject"] == "math"
    assert app.entries[0]["notes"] == "algebra"

def test_filter_by_subject(client, app):
    app.entries = [
        {"date": "2026-01-01", "subject": "math", "notes": "algebra"},
        {"date": "2026-01-02", "subject": "cs", "notes": "python"},
    ]
   
  

    response = client.get("/?subject=math")
  
    assert b"algebra" in response.data
    assert b"python" not in response.data
