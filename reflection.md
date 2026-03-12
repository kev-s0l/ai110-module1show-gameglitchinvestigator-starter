# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It looked like a basic number guessing game, with adjustable difficulty settings, score counter, attempt tracker, and a debug section
that showed a secret number. It seemed fine at first then I noticed issues.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

After realizing that the secret was the answer, I noticed that the hints were backwards. Whenever the user provided a guess higher
than the answer, they were asked to guess higher and the opposite was true when the guess was lower than answer.

Later on, when wanting to reset to a new game, nothing really changed except for the 'secret' which gave a false image of a game reset when in reality the state of the game stayed the same. Only a full page reset would achieve a 'new game' state

Taking a look at the difficulties, the ranges for 'Normal' and 'Hard' seemed to be switched. Hard should have the larger range of 1-100 instead of  its current 1-50 range. Switching difficulties also doesn't prompt the correct range to the user and its a stagnant "Guess a number between 1 and 100" 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

ChatGPT is my current go-to AI tool.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It suggested a couple of changes when I asked it to fix the refresh button feature and it was able to fully reset the status of the game
and its playability. I tested it by playing the game a couple of times and hitting reset whenever I felt like it. Didn't seem to run 
into any issues since then.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Still involving the reset feature, I noticed that it still kept the last number the user input last on the 'guess' tab. It suggested resetting the key but after testing it, I was given an error message so I promptly reverted the change and kept it as it was. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

If after play testing, never ran into the same issue again nor did it appear under any instance of the game running


- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I mostly ran manual tests such as inputting the incorrect data types, clicking buttons in different sequences seeing if by some miracle,
I found out that I accidentally allowed a combination of button clicks to do something.


- Did AI help you design or understand any tests? How?

Just helped adjust the current one by adding ",_" after 'result' since guess_check returns a tuple.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

In the original code, on some turns it converted the secret number into a string instead of keeping it as an integer. That meant the comparison logic no longer behaved normally, so even when the actual stored value had not changed, the game acted inconsistently and made it seem like the answer was shifting.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Reruns is pretty much a way that after clicking a button, stops the current script and restarts from the top. Session-state is a means 
for the application to remember specific data such as in this instance, number of guesses, score, attempts, etc. Its like its own memory


- What change did you make that finally gave the game a stable secret number?

Removing the uneeded data type changes and try/catches. Keeping it one data type (int) helped keep the constant comparison between guess and the secret consistent and accurate

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Before asking for anything, giving context to the AI about what im working on before asking it to walk me through the codebase. Makes
it a lot easier to digest. Also giving it my ideas and asking for feedback.


- What is one thing you would do differently next time you work with AI on a coding task?

Try creating more tests

- In one or two sentences, describe how this project changed the way you think about AI generated code.

It's as useful as you are. If you understand the basics, expected outputs, and general logic it will help.