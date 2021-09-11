"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""


def area(r):
    return (22/7)*r*r

def circumference(r):
    return 2*(22/7)*r

radius = input("Circle radius: ")

print('Area: '+str(area(10)))  # <-- Call the area function and print the result
print('Circumference: '+str(circumference(10)))  # <-- Call the circumference function and print
