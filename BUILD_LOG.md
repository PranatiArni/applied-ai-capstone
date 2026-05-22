## Task 1 — <sScaffold the repo>
- Brief: create a flask project structure, templates, routes file bases, and a claude.md.
- What Claude proposed: to create a flask project structure with templates, ampty home page, python app.py, templates/home.html, requirements,txt, pyproject.toml, tests/conftest.py, and claude.md
- What I changed before approving: I made sure claude didn't make a new claude.md because it had already created one in the beginning. 
- Verification: I entered in sample data and saw that it worrked
- One thing I learned: I had to alias python=python3 in order to make sure it didn't cause any problems, which is an important suggestion claude gave that I had to check.

## Task 2 — <define memory data model>
- Brief: use an entre list in app with date, subject, and notes about it
- What Claude proposed: Since the entry list was already declared in task 1, it suggested hard coding verification entries
- What I changed before approving: Making sure to call the verification entries from the main and not mutating the exisitng entries inside thte create app and sure it was in newest first order
- Verification: added cample entries into the code and confirmed they were being stored
- One thing I learned: Making sure the entries are being added in insertion order will hhelp it add in newest-firstt and aid in filtering afterr

## Task 3 — <create add entry page>
- Brief: add a route to a form that has subject and notes, with the date auto filled
- What Claude proposed: saving entries, cancel, clicking button for page loads. 
- What I changed before approving: made sure the task 3 post behavior will redirect to home
- Verification: sumbitted form with sample values
- One thing I learned: making sure to check the condition that claude tells you it won't do is important, such as how it said it wont check for empty fields and errors

## Task 4 — <entry creation code>
- Brief: wire the form POST to be able to append a new entry for the submission into app.entries
- What Claude proposed: rreplace stum comment with 3 key appends with date, subject, notes from request.form
- What I changed before approving: keep the post-redirect-get pattern
- Verification: submitted form and tracked entry table
- One thing I learned: making sure to verify is very important as sometimes you realize that claude didnt check for verification or errorrs

## Task 5 — <create main timeline view>
- Brief: Create a route that renders all fo the entries sorted by the newest created first
- What Claude proposed: add a helperr method in app.py and updatte home to call it
- What I changed before approving: making sure date in auto-filled
- Verification: added entries to make surre backdatted entries lands at the bottom and future dates ones land at the top
- One thing I learned: helper methods are very important and can help next tasks too as they are module level.

## Task 6 — <filtering>
- Brief: end the route to accept subjec filtering and filter the entries by subject
- What Claude proposed: use the prrevious helper in app.py to update and remove the placeholder comment. an inside of template, filter the row and empty-state copy in css
- What I changed before approving: make sure clicking ALL is still an option to go back
- Verification: filtered entries based on math, chemistry, and reading tto make sure they wroked
- One thing I learned: claude will not check for tests if it is in another task, and will only do the minimum to be fast

## Task 7 — <short name>
- Brief: [link or paste]
- What Claude proposed: [1-2 lines]
- What I changed before approving: [1-2 lines]
- Verification: [what you ran or clicked to confirm it works]
- One thing I learned:

## Task 8 — <short name>
- Brief: [link or paste]
- What Claude proposed: [1-2 lines]
- What I changed before approving: [1-2 lines]
- Verification: [what you ran or clicked to confirm it works]
- One thing I learned:


