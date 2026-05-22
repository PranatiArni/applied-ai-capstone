# CLAUDE.md

Context Claude Code reads automatically when started in this repo.

## What this project is

A **Daily Study Tracker** — a lightweight Flask web app for logging what I
study each day. Each entry is a `{date, subject, notes}` record. The home
page shows all entries in reverse-chronological order and supports optional
filtering by subject. The goal is to make study consistency visible over
time, not to build a fully-featured productivity tool.

The structure intentionally mirrors `applied-ai-sandbox` (the cohort
practice repo) so I can reuse patterns I already know.

## Stack

- Python 3.10+
- Flask 3.x
- pytest
- Jinja2 templates, vanilla HTML/CSS
- In-memory state only (`app.entries: list[dict]`) — no database, no ORM

Persistence across restarts is **not** a requirement for this version.

## Data model

Every entry is exactly:

```python
{"date": str, "subject": str, "notes": str}
```

Do not add fields (id, tags, duration, etc.) unless a task explicitly
requires it.

## How to run things

```bash
# Run the app
python app.py
# → http://localhost:5000

# Run all tests
pytest

# Run tests for a single task
pytest tests/test_task_NN.py
```

## Conventions

- **Type hints** on every function and route handler (use
  `from __future__ import annotations` at the top of `app.py`).
- **Small, focused helpers** instead of large route blocks — e.g.,
  `sort_entries_newest_first(...)`, `filter_by_subject(...)`. Routes
  should orchestrate, not contain business logic.
- **In-memory state stays simple**: read/write `app.entries` directly in
  the route or helper. No hidden globals, no mutation in templates.
- **UI logic belongs in templates**, not Python. Routes pass plain data
  (lists, dicts, strings) to Jinja and let the template format it.
- **Deterministic sort/filter**: given the same input list, sorting and
  filtering must always produce the same output. No reliance on dict
  insertion order tricks or timestamps generated inside the sort.
- **Task = test file**: each task in `tasks/` corresponds to
  `tests/test_task_NN.py`. A task is "done" when its tests pass.
- Keep changes scoped to the active task; don't refactor unrelated code.

## Things Claude should NOT do

- **No new dependencies** (no SQLAlchemy, no SQLite, no Jinja extensions,
  no React/Vue/HTMX, no Tailwind) without explicit approval.
- **Do not edit tests** to make failures go away. Fix `app.py` or the
  templates instead — tests are the spec.
- **Do not change the data model** beyond `{date, subject, notes}`
  unless I explicitly ask.
- **Do not mix UI logic into Python routes** beyond passing template
  variables. No HTML strings in `app.py`.
- **Do not over-engineer**: no auth, no user accounts, no analytics, no
  config layers, no blueprint splitting for a single-file app.
- **Do not add features outside the defined scope** (a study log with
  subject filtering). New ideas → ask first.

## Working with Claude here

- Read the task file in `tasks/` before writing code.
- Plan before implementing — ask for a plan first on anything non-trivial.
- Run `pytest` after each substantive change.
- If Claude proposes editing a test to "make it pass," push back. The
  tests are the spec.
