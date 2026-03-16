# Game Glitch Investigator

## Setup

1. Install dependencies with `pip install -r requirements.txt`.
2. Start the app with `python -m streamlit run app.py`.
3. Run the automated checks with `pytest`.

## Demo

The repaired app is a Streamlit number guessing game with three difficulty levels, score tracking, and consistent high/low hints. The game now keeps the correct secret number for the selected difficulty, resets cleanly on a new game, and only counts valid guesses toward the attempt limit.

Add a screenshot of a winning run here before submission. The assignment expects a real screenshot, so this section still needs that manual capture.

## Document Your Experience

This project started with several logic and state bugs that made the game unreliable. I used AI as a debugging partner, but I verified each change by reading the code, running `pytest`, and checking the app behavior against the assignment goals.

Key fixes included moving core logic into `logic_utils.py`, correcting the reversed hint messages, removing the secret-number type mismatch bug, fixing the hard difficulty range, and making the score logic consistent. I also tightened the Streamlit state flow so switching difficulty or starting a new game fully resets the session with the correct range.

Testing now covers the core helper functions in `logic_utils.py`, including win detection, high/low hints, parsing valid and invalid guesses, difficulty ranges, and scoring behavior. This gives a reproducible way to verify the repairs instead of relying only on manual playthroughs.

## Files

- `app.py`: Streamlit UI and session-state management.
- `logic_utils.py`: Game logic helpers for parsing, hinting, ranges, and scoring.
- `tests/test_game_logic.py`: Pytest coverage for the repaired logic.
- `reflection.md`: Written reflection for the assignment prompts.
