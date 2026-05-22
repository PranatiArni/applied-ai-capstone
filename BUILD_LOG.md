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


## AI WORKFLOW
- Tools Used:
I used Chat during the planning phase in order to break the study tracker into clear steps and tasks and to also decide the route structure before writing any code. I then took the plan given by chat and used Claude Code to build onto 8 different tasks for execution to implement the flask routes, filtering logic, and new entries, because it was best at making changes as it had access to all my files and the context I gave. I used Copilot when doing automated testing with its fill-line feature in order to fill in small gaps in pytest files, complete repetitive code lines, and suggest minor syntax improvements when I was already editing. I also used Chat for reviewing and debugging when something broke, such as during py-test failures, because it was better at explaining what is the most likely cause in these types of errors and how I could fix it. A moment where Chat clearly outperformed Claude Code was during debugging a failing test, because Chat was able to identify the most common situation when errors like this occur and helped trace how to fix the problem I was having even without prior context. However, Claude Code initially tried to “fix” app logic and ended up breaking and changing more things that I had to undo. I switched mid-task from Claude Code to Chat when pytest errors started appearing, because Claude Code kept adding onto implementation rather than identifying the main issue and how to change only that part. 

## Reflection:
- The agentic workflow let me ship this that i couldnt have done alone in 4 hours by giving me a one page planner before starting my implementation, rather than me having to go in a write every single condition I needed and creating all of the references and contexts for myself. I used claude code to create and build all my files, which would have taken me more time to figure out what files I needed and how to use them if I didn't have these workflows. Chat allowed me to debug faster than going through it myself. Most importantly, Claude code was able to be written by main task implementation after I had carefully approved and verified all of the changes it would make in just a few minutes, which saved hours of time for me. However, I did have to step in an override clause when it began to go out of scope and change files that I didn't want it to touch, or when it started to change the app logic in ways that didn’t match my original idea. I had to remind Claude of the specification and not to go outside of them, and keep the app simple without over-complicating the code. I knew how I wanted my web to function and which changes each feature would make, so I had to remind Claude of what I wanted since it didn’t know that. Regarding judgement and knowledge gaps, this project revealed that I tend to take several AI workflows as granted and that they are always right if we give them instructions. However, during this capstone project, I realized that oftentimes the Claude implementation didn’t end up like my guidelines, and I often missed these because I blindly trusted it. This showed me that I have to slow down my judgement and carefully ask Claude to plan the changes first before implementing them so I can see red flags in what it does and stop it before it creates errors. I will be able to bring this into my internship by using the workflow steps I used in the first way, including asking chat to plan first, clarify individually what i am building and then putting it into chat, checking its plan before implementation, verifying its implementation, writing pay tests, and making sure the features are working manually.
