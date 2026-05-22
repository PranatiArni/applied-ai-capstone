"""Daily Study Tracker — a tiny Flask app for logging what I study each day."""
from __future__ import annotations

from datetime import date

from flask import Flask, redirect, render_template, request, url_for


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "study-tracker-not-a-real-secret"

    # In-memory store. Resets on every restart — persistence isn't a goal
    # for this version. Each entry is {"date": str, "subject": str, "notes": str}.
    app.entries: list[dict] = []  # type: ignore[attr-defined]

    @app.route("/")
    def home():
        active_subject = (request.args.get("subject") or "").strip()
        entries = sort_entries_newest_first(
            filter_by_subject(app.entries, active_subject)
        )
        subjects = sorted({e["subject"] for e in app.entries})
        return render_template(
            "home.html",
            entries=entries,
            subjects=subjects,
            active_subject=active_subject,
        )

    @app.route("/entries/new", methods=["GET", "POST"])
    def new_entry():
        if request.method == "POST":
            app.entries.append({
                "date": (request.form.get("date") or "").strip(),
                "subject": (request.form.get("subject") or "").strip(),
                "notes": (request.form.get("notes") or "").strip(),
            })
            return redirect(url_for("home"))
        return render_template("new_entry.html", today=date.today().isoformat())

    return app


def sort_entries_newest_first(entries: list[dict]) -> list[dict]:
    """Return a new list sorted by date (ISO YYYY-MM-DD), newest first.

    Stable: entries sharing a date keep their insertion order.
    """
    return sorted(entries, key=lambda e: e["date"], reverse=True)


def filter_by_subject(entries: list[dict], subject: str) -> list[dict]:
    """Return entries whose subject matches `subject` (case-insensitive).

    An empty / None subject returns the list unchanged. Deterministic:
    preserves the input order.
    """
    if not subject:
        return list(entries)
    needle = subject.strip().lower()
    return [e for e in entries if e["subject"].lower() == needle]


def _seed_sample_entries(app: Flask) -> None:
    """Populate app.entries with a few illustrative records for dev runs.

    Called only from __main__ so tests start from an empty list.
    """
    app.entries.extend([
        {"date": "2026-05-19", "subject": "Math",
         "notes": "Worked through chapter 3 derivatives problems."},
        {"date": "2026-05-20", "subject": "Physics",
         "notes": "Reviewed kinematics equations and practice problems."},
        {"date": "2026-05-21", "subject": "Math",
         "notes": "Started chapter 4 on integrals."},
        {"date": "2026-05-21", "subject": "Reading",
         "notes": "Finished the assigned chapter and took notes."},
    ])


if __name__ == "__main__":
    app = create_app()
    _seed_sample_entries(app)
    app.run(debug=True, port=5000)
