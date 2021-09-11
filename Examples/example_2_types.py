print(type(1))
print(type(3.14))
print(type('papaya'))
print(type(True))
print(type(False))
print(type(None))
print(type([1, 2, 10]))     # List
print(type((1, 2, 10)))     # Tuple; immutable list
print(type({1,2,3}))        # Set

# frozenset; immutable Set; initialize from iterable
fs = frozenset([1,2,3,4,2,3]) # initialize from List
print(type(fs))
print(frozenset((1,2,3,4,2,3))) # initialize from Tuple
print(frozenset({33,44,55,66,33})) # initialize from Set
print(frozenset({'a':'aaa','b':'bbb','c':'ccc'})) # initialize from Dictionary

print(type({'apple': 'A round fruit', 'banana': 'A long yellow fruit',
            'cucumber': 'A long green fruit'}))

# convert list to a set
my_list=[1,5,2,5,2,10,11]
print(my_list)
my_set = set(my_list)  # duplicate elements will be ignored while converting
print(my_set)

# access an element of dictionary
fruits = {'apple': 'A round fruit', 'banana': 'A long yellow fruit',
            'cucumber': 'A long green fruit'}
print(fruits["banana"])


