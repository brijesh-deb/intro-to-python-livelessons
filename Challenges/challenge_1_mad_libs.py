"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""

# Write a story with some words missing
story = """
Roses are {colour}\n
Violets are {colour2}\n
Sugar is {adjective}\n
And so are you
"""

# Ask the user to provide the missing words
colour =input("Enter colour: ")
colour2 =input("Enter colour2: ")
adjective =input("Enter adjective: ")

# Display the final story
print(story.format(colour=colour,colour2=colour2,adjective=adjective))
