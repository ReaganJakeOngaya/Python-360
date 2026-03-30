# Sets are a built-in data type in Python that allow you to store an unordered collection of unique items.
# Sets are defined using curly braces {} or the set() constructor.
# Sets do not allow duplicate items and do not maintain any order.
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding items to a set using add() method
my_set.add(6)
print("Set after adding an item:", my_set)

# Removing items from a set using remove() method
my_set.remove(3)
print("Set after removing an item:", my_set)

# Using the len() function to get the number of items in a set
number_of_items = len(my_set)
print("Number of items in the set:", number_of_items)