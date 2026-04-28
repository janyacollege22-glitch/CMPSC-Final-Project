"""
Number Guessing Game

"""

import random


# Difficulty configuration
DIFFICULTY_SETTINGS = {
    "1": {"name": "Easy",   "max_attempts": 15, "range": (1, 50)},
    "2": {"name": "Medium", "max_attempts": 10, "range": (1, 100)},
    "3": {"name": "Hard",   "max_attempts":  7, "range": (1, 200)},
}


# Input helpers 
def get_integer_input(prompt: str) -> int:
    """Keep asking until the user enters a valid integer."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit():
            return int(raw)
        print("Invalid input - please enter a whole number.\n")


def get_choice(prompt: str, valid: set) -> str:
    """Keep asking until the user enters one of the valid choices."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid:
            return choice
        print(f"Please enter one of: {', '.join(sorted(valid))}\n")


# Difficulty selection
def choose_difficulty() -> dict:
    """Display a menu and return the chosen difficulty settings."""
    print("\n" + "─" * 40)
    print("  SELECT DIFFICULTY")
    print("─" * 40)
    for key, cfg in DIFFICULTY_SETTINGS.items():
        low, high = cfg["range"]
        print(f"  {key}. {cfg['name']:<8}  "
              f"Range {low}–{high}  |  {cfg['max_attempts']} attempts")
    print("─" * 40)

    choice = get_choice("Enter 1, 2, or 3: ", {"1", "2", "3"})
    return DIFFICULTY_SETTINGS[choice]


# Core game 
def play_game() -> bool:
    """
    Run one round of the guessing game.
    Returns True if the player won, False otherwise.
    """
    cfg = choose_difficulty()
    low, high = cfg["range"]
    max_attempts = cfg["max_attempts"]
    secret = random.randint(low, high)

    attempts = 0
    print(f"\n  I'm thinking of a number between {low} and {high}.")
    print(f"    You have {max_attempts} attempt(s). Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess = get_integer_input(
            f"Attempt {attempts + 1}/{max_attempts} "
            f"({remaining} left) – Your guess: "
        )
        attempts += 1

        # Boundary feedback
        if guess < low or guess > high:
            print(f"  Out of range! Guess must be between {low} and {high}.\n")
            attempts -= 1          # don't penalise an out-of-range guess
            continue

        # Core feedback
        if guess == secret:
            print(f"\n  Congratulations! {secret} is correct!")
            print(f"      You guessed it in {attempts} attempt(s).\n")
            return True
        elif guess > secret:
            gap = guess - secret
            hint = "Much too high!" if gap > 20 else "Too high! "
            print(f"  {hint}\n")
        else:
            gap = secret - guess
            hint = "Much too low! " if gap > 20 else "Too low! "
            print(f"  {hint}\n")

    # Out of attempts 
    print(f"\n  Out of attempts! The number was {secret}. Better luck next time!\n")
    return False


# Session loop 
def main() -> None:
    """Entry-point: show banner, play rounds, show session stats."""
    print("\n" + "═" * 40)
    print("       NUMBER GUESSING GAME")
    print("═" * 40)

    wins = losses = 0

    while True:
        if play_game():
            wins += 1
        else:
            losses += 1

        print(f"   Session stats – Wins: {wins}  |  Losses: {losses}")
        again = get_choice("\nPlay again? (y/n): ", {"y", "n"})
        if again == "n":
            break

    total = wins + losses
    print("\n" + "═" * 40)
    print("  Thanks for playing!")
    if total:
        pct = wins / total * 100
        print(f"  Final: {wins}W / {losses}L  ({pct:.0f}% win rate)")
    print("═" * 40 + "\n")


if __name__ == "__main__":
    main()