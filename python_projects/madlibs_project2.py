# creating a story using string concatenation that allows a user
# to play a madlib game by inputing different adjectives and so on. 

# creating the variables where the user inputs the needed data in the madlib.
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")
adjective3 = input("adjective: ")
adjective4 = input("adjective: ")
plural_noun = input("plural_noun: ")
noun1 = input("noun: ")
verb = input("verb: ")
noun2 = input("noun: ")
adjective5 = input("adjective: ")
adjective6 = input("adjective: ")
noun3 = input("noun: ")
adjective7 = input("adjective: ")
sound = input("sound: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
noun4 = input("noun: ")
sound1 = input("sound: ")
adjective8 = input("adjective: ")
plural_noun2 = input("plural_noun: ")

# creating a variable that holds the madlib game
# using triple double quotes since the string covers the multiple lines
The_mysterious_Island = f"""As I stepped off the {adjective1} boat and onto 
the {adjective2} sand, I couldn't help but feel a sense of {adjective3} excitement.
The Island was rumoured to be {adjective4} and full of hidden {plural_noun}. 
I had always been fascinated by the {noun1} of the island and was determined to
{verb} it's secrets.

As I made my way through the dense {noun2}, I stumbled upon a {adjective5} temple.
The entrance was guarded by a {adjective6} statue of a {noun3}. I felt a sense of 
{adjective7} as I approached the statue, but as I reached out to touch it, I heard 
a loud {sound}.

Suddenly, the temple began to {verb1} and I found myself {verb2} down a long, dark
{noun4}. I landed with a {sound1} and looked around to see that I was in a {adjective8}
room filled with {plural_noun2}.
"""

# execute the madlib using the print statement
print(The_mysterious_Island)