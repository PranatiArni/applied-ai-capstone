"""Tests for Task 4 — form POST appends an entry to app.entries."""
from __future__ import annotations


def test_get_form_renders(client):
    res = client.get("/entries/new")
    assert res.status_code == 200
    assert b'name="date"' in res.data
    assert b'name="subject"' in res.data
    assert b'name="notes"' in res.data


def test_post_appends_entry(client, app):
    assert app.entries == []
    res = client.post("/entries/new", data={
        "date": "2026-05-21",
        "subject": "Math",
        "notes": "Studied integrals",
    })
    assert res.status_code == 302
    assert app.entries == [
        {"date": "2026-05-21", "subject": "Math", "notes": "Studied integrals"},
    ]


def test_post_redirects_to_home(client):
    res = client.post("/entries/new", data={
        "date": "2026-05-21", "subject": "X", "notes": "y",
    })
    assert res.status_code == 302
    assert res.headers["Location"].endswith("/")


def test_multiple_posts_append_each(client, app):
    for i in range(3):
        client.post("/entries/new", data={
            "date": f"2026-05-2{i}",
            "subject": f"Subj{i}",
            "notes": f"note{i}",
        })
    assert len(app.entries) == 3
    assert [e["subject"] for e in app.entries] == ["Subj0", "Subj1", "Subj2"]


def test_post_strips_whitespace(client, app):
    client.post("/entries/new", data={
        "date": "  2026-05-21  ",
        "subject": "  Math  ",
        "notes": "  with edges  ",
    })
    assert app.entries[0] == {
        "date": "2026-05-21",
        "subject": "Math",
        "notes": "with edges",
    }
