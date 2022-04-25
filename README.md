# Elite Insights Json Guesser
A basic program that focuses on parsing an existing JSON of a Guild Wars 2 ArcDPS log, cutting it down, and then allowing the user to guess the DPS order in a situation similar to Wordle.

As of right now, the program is pretty barebones. There is the createJson.py, which given a much larger JSON of a Guild Wars 2 ArcDPS log, cuts it down to the only three data points we need (Player Name, Player Profession, Player DPS), and outputs it as a seperate JSON. The other program, useJson.py, takes in this cut down log, and currently has a very barebones guessing game in the console that allows the user to guess the profession, and either get a "yes" or "no".

In the future, I hope to have this program act similar to Wordle, where it will tell you if the guess is right, wrong, or right but in the wrong place. I also want to eventually put this into a website similar to Wordle, which is why createJson exists to drastically cut down on the size of the JSON files, and make it easier for me to work with.
