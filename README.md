# Number Guessing Game

A number guessing game in Python, built in **three versions** that show how the project grew: a basic command-line game, an improved command-line game, and a graphical version built with Tkinter. The computer picks a secret number between 1 and 200, and you try to find it using "too small" / "too big" hints.

Built by Bilel K. while finishing [CS50P](https://cs50.harvard.edu/python/) (Harvard's Introduction to Programming with Python).

![Graphical version of the game](images/interface_with_ai.png)

## The three versions

| | Version 1: basic | Version 2: improved | Version 3: GUI |
|---|---|---|---|
| File | `guessing-game.py` | `improve.py` | `interface_with_ai.py` |
| Interface | Terminal | Terminal | Tkinter window |
| Input check | Rejects non-numbers | Rejects non-numbers and numbers outside 1-200 | Rejects non-numbers and numbers outside 1-200 |
| Attempts | Unlimited | 10 | 10, shown as dots |
| Play again | Run the script again | "yes or no" prompt | "New game" button |
| On a win | Number of guesses and the list of guesses | Number of guesses | Number of guesses and a colored history |
| Extra | | | Shows the remaining range, e.g. "between 126 and 129" |

## Getting started

**Requirements:** Python 3. Tkinter is included with the standard Python installer on Windows and macOS. On some Linux distributions, install it with `sudo apt install python3-tk`.

```bash
git clone https://github.com/bi1e1/guessing-game.git
cd guessing-game
```

Run the version you want:

```bash
python guessing-game.py
python improve.py
python interface_with_ai.py
```

## How to play

1. The game picks a secret number from 1 to 200.
2. Type a guess and press Enter.
3. The game tells you whether your guess is too small or too big.
4. Keep guessing until you find the number. In versions 2 and 3, you have 10 attempts.

In the GUI, each guess is saved as a colored chip: amber means too small, red means too big, and green means correct. Invalid input does not use an attempt.

### Example run (version 2)

```
Give me your guess ::: 100
Your guess is too big !!!
Give me your guess ::: 50
Your guess is too small !!!
Give me your guess ::: 75
Bravo, you finish after 3 guesses !!!
Do you want to play again ? yes or no ::: no
```

**Tip:** always guess the middle of the remaining range (binary search). With this strategy you can find any number from 1 to 200 in at most 8 guesses, so 10 attempts is enough.

## How it works

All three versions share the same core idea: compare the player's guess with the secret number and return one of three results.

```python
def hint(player, secret):
    if secret > player:
        return 'small'
    elif secret < player:
        return 'big'
    else:
        return 'right'
```

This function only compares and returns a value. It does not print or read input, so it is easy to reuse and to test. (Version 1 calls it `hints`.)

### Version 1: basic (`guessing-game.py`)

| Function | Role |
|---|---|
| `main()` | Picks the secret number with `random.randint(1, 200)`, reads each guess with `input()`, and handles invalid input with `try` / `except ValueError`. |
| `rounding()` | Stores each guess in a list with `append()`. |
| `hints()` | Returns `'small'`, `'big'` or `'right'`. |
| `result()` | Prints the hint, or the winning message with the list of all guesses. |

The loop runs until the player guesses correctly, then ends with `sys.exit()`.

### Version 2: improved (`improve.py`)

What changed from version 1:

- **Range check:** numbers below 1 or above 200 are rejected with a message and do not count as a guess.
- **Attempt limit:** the game ends with "Game Over" after 10 guesses.
- **Play again:** after a win or a loss, the player is asked whether to start a new game.
- **Clean exit:** answering "no" ends the program with `sys.exit()`.

| Function | Role |
|---|---|
| `main()` | Picks the secret number and runs the game loop. An inner loop keeps asking until the guess is a number from 1 to 200, and `try` / `except ValueError` catches text input. It ends the game after 10 guesses. |
| `round()` | Stores each valid guess in a list. |
| `hint()` | Returns `'small'`, `'big'` or `'right'`. |
| `result()` | Prints the hint, or the winning message and the number of guesses, then asks to play again. |
| `again()` | Asks "yes or no". "yes" starts a new game by calling `main()`, and "no" exits. |

### Version 3: GUI (`interface_with_ai.py`)

The GUI is a class, `GuessGame`, that extends `tkinter.Tk` and reuses the same hint logic.

| Method | Role |
|---|---|
| `build_ui()` | Creates the title, the attempt dots, the message card, the input field, the buttons and the guess history. |
| `new_game()` | Picks a new secret number and resets the guesses, the range and the display. |
| `on_guess()` | Reads and validates the input, saves the guess, shows the hint and checks for a win or a loss. |
| `draw_dots()` | Draws one dot per attempt used (blue while playing, green on a win, red on a loss). |
| `add_chip()` | Adds the guess to the history, colored by its result. |
| `finish()` | Ends the round by disabling the input field. |
| `show_error()` | Shows an error message when the input is not a whole number from 1 to 200. |

The game also narrows the range as you play. After a "too small" answer the lower bound moves up, and after a "too big" answer the upper bound moves down, so the message "The number is between X and Y" always shows what is still possible. When you lose, the game reveals the secret number.

## Project structure

```
guessing-game/
├── guessing-game.py        # version 1: basic command-line game
├── improve.py              # version 2: improved command-line game
├── interface_with_ai.py    # version 3: Tkinter GUI
├── images/
│   └── interface_with_ai.png
└── README.md
```

## What I practiced

- Functions and return values
- Lists and `append()`
- The `random` module
- Exception handling with `try` / `except`
- Loops and conditionals, including nested loops for input validation
- Basic GUI programming with Tkinter (classes, widgets, events)

## Known limitations and next steps

- [ ] In version 2, re-ask the "play again" question until the answer is "yes" or "no". Right now any other answer returns to the finished game
- [ ] In version 2, replace the recursive `main()` call in `again()` with a loop
- [ ] In version 2, rename `round()`, because it overrides Python's built-in `round()`
- [ ] In version 2, show the secret number when the game is lost
- [ ] Add unit tests for the hint function with `pytest`
- [ ] Move the shared hint logic into one module used by all versions

## About

Versions 1 and 2 and the game logic are my own work, written while learning Python with CS50P. The graphical version was created with the help of an AI assistant, built on top of that logic.
