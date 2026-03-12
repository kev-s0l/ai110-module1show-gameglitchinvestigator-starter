#FIX: Adjusted game difficulty ranges and allowed attempts to the correct difficulty title
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50

# Nothing changes here from the original
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

#FIX: Removed string comparison and try/except logic so both guess and secret remain integers. 
#FIX: Adjusted hints to print correctly using ChatGPT
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

# FIX: Simplified scoring so points are only awarded on a win based on how few attempts the player used, 
#      removing inconsistent penalties and bonuses from incorrect guesses.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        bonus = max(100 - 10 * (attempt_number - 1), 10)
        return current_score + bonus
    return current_score


