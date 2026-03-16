# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first analyzed the game, I identified several critical bugs by reading through the code:

1. **Reversed Hints Bug**: In app.py:38-40, the hint logic is backwards. When `guess > secret`, the code says "Go HIGHER!" but it should say "Go LOWER!". Similarly, when `guess < secret`, it says "Go LOWER!" when it should say "Go HIGHER!". This makes the game nearly impossible to win.

2. **Secret Type Switching Bug**: In app.py:158-161, on even-numbered attempts, the secret number is converted to a string (`secret = str(st.session_state.secret)`). This breaks integer comparisons and causes the check_guess function to use string comparison logic instead of numeric logic, leading to incorrect and confusing behavior.

3. **Hard Mode Range Bug**: In app.py:10, Hard difficulty returns range (1, 50) while Normal returns (1, 100). This makes Hard mode easier than Normal mode, which is backwards. Hard difficulty should have a wider range to make it more challenging.

4. **Score Logic Bug**: In app.py:58-60, when the outcome is "Too High", the game adds 5 points if the attempt number is even and subtracts 5 points if odd. This random scoring behavior doesn't make sense - wrong guesses should consistently penalize the player.

---

## 2. How did you use AI as a teammate?

I used Claude Code (an AI-powered CLI tool) for this project. I treated the AI as a pair programming partner, carefully reviewing each suggestion rather than blindly accepting code.

**Example of a correct AI suggestion**: When refactoring the check_guess function to logic_utils.py, the AI correctly identified that the hint logic was reversed (lines 38-40 in the original app.py). When `guess > secret`, it said "Go HIGHER!" instead of "Go LOWER!". I verified this was correct by tracing through the logic manually - if I guess 60 and the secret is 50, my guess is too high, so I should go lower. The fix was confirmed by running pytest tests that specifically check the hint messages match the outcomes.

**Example of an incorrect/misleading initial approach**: My first instinct was to try running the Streamlit app interactively to find bugs through gameplay. However, this would have been time-consuming and might have missed subtle bugs. Instead, I used code analysis to identify all bugs systematically by reading through the logic. This was more efficient and comprehensive - I found the secret type-switching bug (lines 158-161) that only occurs on even-numbered attempts, which I might have missed through random gameplay testing.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by using a two-step verification process: first, I manually traced through the logic to understand why the fix should work, and second, I wrote automated pytest tests to verify the behavior programmatically. This combination gave me high confidence the fixes were correct.

**Key test example**: For the reversed hints bug, I wrote `test_guess_too_high()` which checks that when `guess=60` and `secret=50`, the outcome is "Too High" AND the message contains "LOWER". This test would have failed before my fix (since the original message said "HIGHER"), but now passes, confirming the logic reversal was corrected. I also created a comprehensive test suite with 12 tests covering edge cases like decimal inputs, empty strings, and boundary values to ensure robustness.

The AI helped me design comprehensive tests by suggesting I test not just the outcome but also verify the hint messages contain the correct directional advice ("HIGHER" vs "LOWER"). This caught a potential issue where I could have fixed the outcome but left the message wrong. The AI also helped me think about edge cases like testing that Hard difficulty is genuinely harder than Normal by asserting `hard_high > normal_high` in the test.

---

## 4. What did you learn about Streamlit and state?

Streamlit "reruns" the entire Python script from top to bottom every time a user interacts with the app (like clicking a button or typing input). This is different from traditional web apps where only parts of the page update. To remember information between reruns (like the secret number, score, or attempt count), Streamlit provides `st.session_state` - a dictionary-like object that persists data across reruns. Without session state, the secret number would regenerate on every button click, making the game impossible to play! This is why the "New Game" button bug was critical - it wasn't properly resetting all session state variables, causing the game to behave inconsistently when starting a new game.

---

## 5. Looking ahead: your developer habits

**Habit to reuse**: I want to continue the practice of adding inline code comments that mark where bugs were fixed (using `# FIXME:` and `# FIX:` comments). This creates a clear audit trail showing what was wrong and how it was corrected, which is valuable for code reviews and future maintenance. It also helps me think critically about whether I truly understand what I'm fixing versus just applying changes blindly.

**What I'd do differently**: Next time, I would run the existing pytest tests BEFORE making any changes to establish a baseline of what's passing vs failing. In this project, I jumped straight to code analysis and fixes, but running tests first would have given me immediate feedback about which functions were already broken, potentially saving time and providing a clearer starting point.

**How this changed my thinking about AI-generated code**: This project reinforced that AI-generated code should always be treated as a first draft that requires critical human review, not a finished product. The bugs were subtle but logical - reversed conditionals, type mismatches, and inconsistent scoring - exactly the kinds of errors a human would make when writing quickly without careful testing. AI is a powerful accelerator for development, but human judgment is essential for verification and quality control.
