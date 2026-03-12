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

- [ ] Describe the game's purpose.
The game is a number-guessing app where the player tries to guess a randomly generated secret number within a limited number of attempts based on the selected difficulty.
- [ ] Detail which bugs you found.
The secret number was sometimes converted to a string, causing incorrect comparisons.
The hint messages were reversed (ex: “Too High” told the player to go higher).
The reset/new game behavior and difficulty range handling caused inconsistent gameplay.
- [ ] Explain what fixes you applied.
Removed the code that converted the secret number to a string so it stays a stable integer.
Corrected the hint messages so they properly guide the player.
Cleaned up the game reset and difficulty logic so the secret number and range stay consistent.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

![Winning Screen](winning_screen.png)
![Passing Pytest](passing_pytest.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
