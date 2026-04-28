# 🎮 NUMGUESSR — Number Guessing Game

> A retro arcade-style number guessing game available in both a **Python terminal version** and a **browser-based frontend** (HTML/CSS/JS).

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Python Version](#running-the-python-version)
- [How to Play](#how-to-play)
- [Difficulty Levels](#difficulty-levels)
- [Game Logic](#game-logic)
- [Input Validation](#input-validation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## 🕹️ About the Project

NUMGUESSR is a single-player number guessing game where the computer randomly generates a secret number and the player must guess it using feedback clues. After each guess, the game tells you whether your guess was **too high**, **too low**, or **correct**.
- **`number_guessing_game.py`** — A fully featured terminal/CLI version


---

## ✨ Features

- 🎲 Random number generation using a defined range
- 📊 Three difficulty levels: Easy, Medium, Hard
- 💬 Feedback after every guess: Too High / Too Low / Correct
- 🔢 Attempt tracking with a limited number of lives
- ♻️ Replay system — play multiple rounds in one session
- 📈 Session stats: wins, losses, and win percentage
- ✅ Full input validation — handles non-numbers, out-of-range, and duplicates
- 🖥️ Runs entirely in the terminal — no browser required
- 🔥 Proximity hints: "Much too high / low" when gap > 20
- 🔁 End-of-round replay prompt with running stats

## 📁 Project Structure

```
numguessr/
│
├── number_guessing_game.py     # Python terminal version
└── README.md                   # You are here
```

---

## 🚀 Getting Started

### Prerequisites

**For the Python version:**
- Python 3.x installed ([download here](https://www.python.org/downloads/))
- No external libraries required — uses only the built-in `random` module

### Running the Python Version

1. **Clone the repository** (or download the file directly):
   ```bash
   git clone https://github.com/YOUR_USERNAME/numguessr.git
   cd numguessr
   ```

2. **Run the game:**
   ```bash
   python3 number_guessing_game.py
   ```

3. **Follow the on-screen prompts** to select a difficulty and start guessing!

---


## 🎯 How to Play

1. **Select a difficulty** — Easy, Medium, or Hard
2. **A secret number is generated** within the difficulty's range
3. **Type your guess** and press `GUESS` (browser) or hit Enter (terminal)
4. **Read the feedback:**
   - 🔻 **TOO HIGH** — your guess is above the secret number, guess lower
   - 🔺 **TOO LOW** — your guess is below the secret number, guess higher
   - ✅ **CORRECT!** — you found it, the game ends
5. **You lose** if you run out of attempts — the secret number is revealed
6. **Play again** or return to the main menu after each round

---

## ⚙️ Difficulty Levels

| Difficulty | Range   | Max Attempts | Notes                        |
|------------|---------|:------------:|------------------------------|
| 🟢 Easy    | 1 – 50  | 15           | Great for beginners          |
| 🟡 Medium  | 1 – 100 | 10           | Default / balanced challenge |
| 🔴 Hard    | 1 – 200 | 7            | Tough — every guess counts   |


---

## 🧠 Game Logic

The core game loop works as follows:

```
1. Generate secret = random integer in [low, high]
2. While attempts_remaining > 0:
     a. Prompt player for a guess
     b. Validate the input
     c. If guess == secret  → WIN, end game
     d. If guess > secret   → "Too High", decrement attempts
     e. If guess < secret   → "Too Low",  decrement attempts
3. If attempts exhausted without correct guess → LOSE, reveal secret
```

**Proximity hints** (both versions):
- Gap > 20 → "Much too high / low"
- Gap ≤ 3  → "🔥 Burning hot!" (browser) / extra emphasis (terminal)

---

## 🛡️ Input Validation

Handle every edge case:

| Input              | Response                                      |
|--------------------|-----------------------------------------------|
| Non-numeric text   | Error message, not counted as an attempt      |
| Decimal number     | Error message, whole numbers only             |
| Out-of-range guess | Error message, not counted as an attempt      |
| Duplicate guess    | Warning message, not counted as an attempt    |
| Empty input        | Error message, prompt re-shown                |
| Invalid difficulty | Re-prompted until a valid option is entered   |

---

## 🛠️ Technologies Used

| Technology | Purpose                            |
|------------|------------------------------------|
| Python 3   | Terminal game logic                |
| `random`   | Secret number generation           |

---

**Terminal Version:**
```
════════════════════════════════════════
       NUMBER GUESSING GAME
════════════════════════════════════════

  SELECT DIFFICULTY
  1. Easy      Range 1–50   | 15 attempts
  2. Medium    Range 1–100  | 10 attempts
  3. Hard      Range 1–200  |  7 attempts

🎯  I'm thinking of a number between 1 and 100.
    You have 10 attempt(s). Good luck!

Attempt 1/10 (10 left) – Your guess: 50
  Too high! 🔻

Attempt 2/10 (9 left) – Your guess: 25
  Too low! 🔺

Attempt 3/10 (8 left) – Your guess: 37
  ✅  Congratulations! 37 is correct!
      You guessed it in 3 attempt(s).
```

---

**Ideas for future features:**
- [ ] Leaderboard / high score tracking
- [ ] Sound effects for the browser version
- [ ] A timer mode (race against the clock)
- [ ] Multiplayer — two players take turns guessing
- [ ] Mobile-optimised layout improvements

---
**License:**
**This Project was created as a school Final Project. For Educational Purposes only 

