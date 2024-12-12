# Mad Libs Camping Story

# Get inputs from the user for each blank in the story
family_member = input("Enter a family name: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
plural_noun1 = input("Enter a plural noun: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")
food_item = input("Enter a food item: ")
adjective3 = input("Enter another adjective: ")
sound = input("Enter a sound: ")
noun2 = input("Enter another noun: ")
adjective4 = input("Enter another adjective: ")
creature = input("Enter a creature: ")
verb = input("Enter a verb: ")
object1 = input("Enter an object: ")
noun3 = input("Enter another noun: ")
silly_use = input("Enter a verb you would perform on another object: ")
adjective5 = input("Enter another adjective: ")

# Build the story using the inputs
story = f"""
The Silly Camping Trip

Once upon a time, the {family_member} family decided to go camping in the {adjective1} woods.
They packed their {noun1} and {plural_noun1} for the trip. 
When they arrived at the campsite, they were greeted by a {adjective2} {animal}. 
The {animal} seemed very {emotion}, so the family decided to feed it some {food_item}. 

As the sun set, the {family_member} family sat around the campfire and told {adjective3} stories.
Suddenly, they heard a {sound} coming from the {noun2}. 
It was a {adjective4} {creature}! They all {verb} and hid behind a {object1}. 

The next morning, they woke up to find their {noun3} missing!
They searched everywhere but couldn't find it. 
Finally, they discovered that the {animal} had taken it to use as a {silly_use}.
Everyone laughed and agreed that this was the most {adjective5} camping trip ever.
"""

# Print the final story
print(story)
