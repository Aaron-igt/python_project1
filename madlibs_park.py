# create the variables to allow the user to input the information enabling them to play the madlib game.
# the variables hold the words for the blank spaces in the madlib game.

adjective1 = input("Adjective: ")
name1 = input("Name: ")
colour1= input("colour: ")
scent1 = input("scent: ")
adjective2 = input("adjective: ")
animal1 = input("animal: ")
noun1 = input("noun: ")
adjective3 = input("adjective: ")
place1 = input("place: ")
plural_noun1 =input("plural_noun: ")
object1 = input("object: ")
adjective4 = input("adjective: ")
noun2 = input("noun: ")
food1 = input("food: ")

# create a variable which holds the madlib game
# using f-strings to include the blank spaces in the madlib game
A_day_at_the_park = f"""
                        A DAY AT THE PARK
One day, a {adjective1} person named {name1} decided to visit the park. The sky was {colour1}, and the
air smelt {scent1}. As {name1} walked along, they saw a {adjective2} {animal1} playing with a {noun1}.

Suddenly, a {adjective3} sound came from the {place1}. Curious, {name1} ran towards it, only to find a group of {plural_noun1}
dancing around a {object1}. 'what a {adjective4} day!' they thought.

In the end, {name1} sat down on a {noun2} and enjoyed a delicious {food1} while watching the sunset. It was the perfect end to a
{adjective4} day at the park."""

# print the variable that holds the madlib game in order to execute the code 
print(A_day_at_the_park)