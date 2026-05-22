"""Tests for Task 6 — subject filtering (helper + route)."""
from __future__ import annotations

from app import filter_by_subject


ENTRIES = [
    {"date": "2026-05-21", "subject": "Math",     "notes": "chapter-4-integrals"},
    {"date": "2026-05-20", "subject": "Physics",  "notes": "kinematics-review"},
    {"date": "2026-05-19", "subject": "Math",     "notes": "chapter-3-derivatives"},
    {"date": "2026-05-18", "subject": "Reading",  "notes": "novel-chapter"},
]


def test_empty_subject_returns_all_entries():
    assert filter_by_subject(ENTRIES, "") == ENTRIES
    assert filter_by_subject(ENTRIES, None) == ENTRIES


def test_filter_returns_only_matching_subject():
    result = filter_by_subject(ENTRIES, "Math")
    assert len(result) == 2
    assert all(e["subject"] == "Math" for e in result)


def test_filter_is_case_insensitive():
    assert filter_by_subject(ENTRIES, "math") == filter_by_subject(ENTRIES, "Math")
    assert filter_by_subject(ENTRIES, "MATH") == filter_by_subject(ENTRIES, "Math")


def test_filter_with_no_match_returns_empty():
    assert filter_by_subject(ENTRIES, "Klingon") == []


def test_filter_preserves_input_order():
    result = filter_by_subject(ENTRIES, "Math")
    assert [e["notes"] for e in result] == [
        "chapter-4-integrals",
        "chapter-3-derivatives",
    ]


def test_filter_does_not_mutate_input():
    snapshot = [dict(e) for e in ENTRIES]
    filter_by_subject(ENTRIES, "Math")
    assert ENTRIES == snapshot


def test_route_filters_by_query(client, app):
    app.entries.extend(ENTRIES)

    res = client.get("/?subject=Math")
    assert res.status_code == 200
    assert b"Entries (2)" in res.data
    assert b"chapter-4-integrals" in res.data
    assert b"chapter-3-derivatives" in res.data
    assert b"kinematics-review" not in res.data
    assert b"novel-chapter" not in res.data


def test_route_filter_is_case_insensitive(client, app):
    app.entries.extend(ENTRIES)

    res = client.get("/?subject=math")
    assert res.status_code == 200
    assert b"Entries (2)" in res.data
    assert b"chapter-4-integrals" in res.data


def test_route_with_no_filter_shows_all(client, app):
    app.entries.extend(ENTRIES)

    res = client.get("/")
    assert res.status_code == 200
    assert b"Entries (4)" in res.data
