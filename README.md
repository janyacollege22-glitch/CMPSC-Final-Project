# NUMGUESSR — Number Guessing Game



## About the Project

NUMGUESSR is a single-player number guessing game where the computer randomly generates a secret number and the player must guess it using feedback clues. After each guess, the game tells you whether your guess was **too high**, **too low**, or **correct**.

---

## Features

- Random number generation using a defined range
- Three difficulty levels: Easy, Medium, Hard
- Feedback after every guess: Too High / Too Low / Correct
- Attempt tracking with a limited number of lives
- Replay system — play multiple rounds in one session
- Session stats: wins, losses, and win percentage
- Full input validation — handles non-numbers, out-of-range, and duplicates
- Runs entirely in the terminal — no browser required
- Proximity hints: "Much too high / low" when gap > 20
- End-of-round replay prompt with running stats

### Running

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


## How to Play

1. **Select a difficulty** — Easy, Medium, or Hard
2. **A secret number is generated** within the difficulty's range
3. **Type your guess** and press `GUESS` (browser) or hit Enter (terminal)
4. **Read the feedback:**
   - **TOO HIGH** — your guess is above the secret number, guess lower
   - **TOO LOW** — your guess is below the secret number, guess higher
   - **CORRECT!** — you found it, the game ends
5. **You lose** if you run out of attempts — the secret number is revealed
6. **Play again** or return to the main menu after each round


## Game Logic

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


## Technologies Used

| Technology | Purpose                            |
|------------|------------------------------------|
| Python 3   | Terminal game logic                |
| `random`   | Secret number generation           |

---

---
**License:**
**This Project was created as a school Final Project. For Educational Purposes only 

**Project Review**
So, for this project, I made a number-guessing game. The idea is pretty simple: the computer picks a random number, and you have to figure out what it is just by guessing. After each guess, it tells you if you went too high or too low, and you keep going until you either nail it or run out of tries. 
The way the game works is that the computer secretly picks a number using a random number generator. randint, and then just waits for you to start guessing. You pick a difficulty at the start, which controls how big the range is and how many guesses you get. Easy is 1 to 50 with 15 lives, medium is 1 to 100 with 10, and hard goes all the way to 200 but only gives you 7 shots. Every wrong guess nudges you in the right direction, and if you are really far off, it tells you "much too high" or "much too low" so you are not totally lost.
For the logic, I basically just used a while loop that keeps going until the player either guesses right or runs out of attempts. Inside the loop, there is an if statement comparing the guess to the secret number: too big, too small, or correct. The difficulty settings are stored in a dictionary, so I could just look up the range and attempt limit by name instead of writing out a separate block of code for every level. 
The hardest part, honestly, was input validation. I had to think through every weird thing someone could type, letters, decimals, numbers outside the range, hitting enter with nothing, guessing the same number twice, and handle each one without it counting as a wasted attempt. That took way longer than I expected.

