# creating a story using string concatenation that allows a user
# to play a madlib game by inputing different adjectives and so on. 

# creating the variables where the user inputs the needed data in the madlib.
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")
adjective3 = input("adjective: ")
adjective4 = input("adjective: ")
plural_noun = input("plural_noun: ")
noun = input("noun: ")
verb = input("verb: ")

# creating a variable that holds the madlib game
The_mysterious_Island = f"""As I stepped off the {adjective1} boat and onto 
the {adjective2} sand, I couldn't help but feel a sense of {adjective3} excitement.
The Island was rumoured to be {adjective4} and full of hidden {plural_noun}. 
I had always been fascinated by the {noun} of the island and was determined to
{verb} it's secrets."""

print(The_mysterious_Island)