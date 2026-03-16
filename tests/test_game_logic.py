from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

# Test check_guess function - verifies the reversed hints bug fix
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" with "LOWER" hint
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # This verifies the reversed hints bug was fixed

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" with "HIGHER" hint
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message  # This verifies the reversed hints bug was fixed

# Test parse_guess function - edge case testing
def test_parse_guess_valid_integer():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_guess_decimal():
    # Should convert decimal to integer
    ok, value, error = parse_guess("42.7")
    assert ok is True
    assert value == 42

def test_parse_guess_empty():
    ok, value, error = parse_guess("")
    assert ok is False
    assert "Enter a guess" in error

def test_parse_guess_invalid():
    ok, value, error = parse_guess("not a number")
    assert ok is False
    assert "not a number" in error

# Test get_range_for_difficulty - verifies Hard mode range fix
def test_difficulty_ranges():
    easy_low, easy_high = get_range_for_difficulty("Easy")
    assert easy_low == 1 and easy_high == 20

    normal_low, normal_high = get_range_for_difficulty("Normal")
    assert normal_low == 1 and normal_high == 100

    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert hard_low == 1 and hard_high == 200  # Verifies Hard is harder than Normal
    assert hard_high > normal_high  # Ensures Hard is actually harder

# Test update_score function - verifies consistent score logic
def test_update_score_win():
    # Winning on first attempt should give maximum points
    score = update_score(0, "Win", 1)
    assert score == 80  # 100 - 10 * (1 + 1) = 80

def test_update_score_too_high():
    # "Too High" should always subtract 5 points regardless of attempt number
    score_even = update_score(100, "Too High", 2)
    score_odd = update_score(100, "Too High", 3)
    assert score_even == 95  # Verifies consistent scoring (no longer adds on even attempts)
    assert score_odd == 95

def test_update_score_too_low():
    # "Too Low" should always subtract 5 points
    score = update_score(100, "Too Low", 1)
    assert score == 95

# Edge case tests for robustness
def test_check_guess_edge_cases():
    # Test with boundary values
    outcome, message = check_guess(1, 1)
    assert outcome == "Win"

    outcome, message = check_guess(200, 100)
    assert outcome == "Too High"

    outcome, message = check_guess(1, 100)
    assert outcome == "Too Low"
