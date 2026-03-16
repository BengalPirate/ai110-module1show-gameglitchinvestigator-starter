# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I started, the game had multiple bugs that made the experience unreliable. The most obvious one was the hint logic: a guess above the secret could tell the player to go higher, and a guess below the secret could tell the player to go lower. I also found a type bug where the secret number was sometimes converted to a string, which broke normal number comparisons. On top of that, Hard mode used a smaller range than Normal mode, and the score logic behaved inconsistently for wrong guesses.

---

## 2. How did you use AI as a teammate?

I used AI as a pair-programming teammate for both diagnosis and cleanup, but I did not trust suggestions automatically. One correct suggestion was to move reusable logic into `logic_utils.py` so the hint, scoring, and parsing behavior could be tested in isolation. I verified that approach by running `pytest` after the refactor and making sure the imports and helper behavior still worked. One misleading direction was assuming the existing comments meant the app was already correct; the tests showed that import and behavior problems still existed, so I had to verify everything with actual execution instead of trusting the comments.

---

## 3. Debugging and testing your fixes

I treated each bug as fixed only after I could explain the logic change and confirm it with tests. The main verification step was running `pytest` against the helper functions in `logic_utils.py`, especially the tests for reversed hints, valid and invalid parsing, difficulty ranges, and score updates. I also used `python -m py_compile app.py logic_utils.py tests/test_game_logic.py` to confirm the files were syntactically clean. A helpful example was `test_guess_too_high()`, which verifies that guessing `60` against a secret of `50` returns `Too High` and tells the player to go lower.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script from top to bottom on every interaction, so state management has to be explicit. `st.session_state` is what keeps the secret number, attempt count, score, and history from disappearing on each rerun. That also means reset behavior matters a lot, because stale values can leak into a new round if the reset path misses a field. In this project, I had to make sure both the New Game button and difficulty changes rebuilt the game state cleanly.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is marking suspicious logic with short `# FIXME` and `# FIX` comments while debugging, because it makes the reasoning visible and easier to review later. Next time, I would run the test suite immediately before touching any code so I have a clear baseline instead of relying on comments or assumptions. This project also reinforced that AI-generated code is useful as a draft, not as proof of correctness. The real work is still in reviewing the logic, writing tests, and confirming the behavior yourself.
