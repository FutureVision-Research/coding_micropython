# This Mad Lib story asks the user for the names and details of a family going to the beach.
# The program will then construct a story using those user inputs.


def create_beach_madlib():
    # Ask for the names of the family members
    parent1 = input("Enter a boy's name: ")
    parent2 = input("Enter a girl's name: ")
    child = input("Enter the child's name: ")
    
    # Ask for other details
    adjective1 = input("Enter an adjective: ")
    plural_noun1 = input("Enter a plural noun: ")
    plural_noun2 = input("Enter another plural noun: ")
    food1 = input("Enter a type of food: ")
    body_of_water = input("Enter an adjective: ")
    plural_noun3 = input("Enter another plural noun: ")
    adjective2 = input("Enter another adjective: ")
    food2 = input ("Enter a type of food: ")
    noun = input("Enter a noun: ")
    game = input("Enter another noun: ")
    adjective3 = input("Enter one more adjective: ")

    story = f"""
    One sunny morning, {parent1} and {parent2} decided to take their family to the beach. They packed their {adjective1} bag with {plural_noun1}, {plural_noun2}, and plenty of {plural_noun3}.
    Excitedly, they drove to lake {body_of_water}, singing songs along the way.

    When they arrived, {child} ran straight to the shoreline and started collecting {adjective2} seashells. Meanwhile, {parent1} built a towering sand {noun}, and {parent2} set out towels and umbrellas.
    After a while, the family played kick the {game} in the warm sand and enjoyed a delicious picnic lunch of {food1} and {food2}.

    As the sun began to set, they watched the sky turn {adjective3} colors. It was a day to remember, and everyone agreed they would return again soon.
    """

    print(story)

create_beach_madlib()

