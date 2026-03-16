# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**

  This is a number guessing game where players try to guess a secret number within a limited number of attempts. Players receive hints ("Too High" or "Too Low") to guide their guesses, and earn points based on how quickly they find the correct number. The game has three difficulty levels (Easy, Normal, Hard) with different number ranges and attempt limits.

- [x] **Detail which bugs you found.**

  1. **Reversed Hints Bug**: The hint logic was backwards - when guess > secret, it said "Go HIGHER!" instead of "Go LOWER!"
  2. **Secret Type Switching Bug**: On even-numbered attempts, the secret was converted to a string, breaking numeric comparisons
  3. **Hard Mode Range Bug**: Hard difficulty had range 1-50 while Normal had 1-100, making Hard easier than Normal
  4. **Score Logic Bug**: "Too High" outcome randomly added or subtracted points based on attempt parity
  5. **State Reset Bug**: New Game button and difficulty changes didn't reset all state properly

- [x] **Explain what fixes you applied.**

  1. Refactored all game logic functions from app.py to logic_utils.py for better separation of concerns
  2. Corrected hint messages so "Too High" says "Go LOWER!" and "Too Low" says "Go HIGHER!"
  3. Removed the type-switching logic that converted secret to string on even attempts
  4. Changed Hard mode range to 1-200 to make it genuinely harder than Normal mode
  5. Simplified score logic so wrong guesses consistently subtract 5 points
  6. Added reset_game_state() helper to properly reset all session state
  7. Added difficulty-change detection to automatically reset game when switching modes
  8. Fixed attempt counting to start at 0 and only increment on valid guesses
  9. Created comprehensive pytest test suite with 12 tests covering all core functions and edge cases

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
