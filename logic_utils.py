def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Changed Hard mode from (1, 50) to (1, 200) to make it actually harder than Normal
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200  # FIXED: Was 1, 50 which made Hard easier than Normal
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIXME: Logic was backwards - when guess > secret, should say "Go LOWER!"
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Corrected the reversed hint logic
    if guess > secret:
        return "Too High", "📉 Go LOWER!"  # FIXED: Was "Go HIGHER!"
    else:
        return "Too Low", "📈 Go HIGHER!"  # FIXED: Was "Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: Simplified score logic - wrong guesses always subtract points
    if outcome == "Too High":
        return current_score - 5  # FIXED: Was adding/subtracting based on even/odd attempts

    if outcome == "Too Low":
        return current_score - 5

    return current_score
