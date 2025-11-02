# Tuples
# they are Immutable (cannot be changed after creation)

# Creating a tuple
dimensions = (1920, 1080,)
print("Original dimensions:", dimensions)

#Tuples and For Loops
#Example of iterating through a tuple
for dimension in dimensions:
    print(dimension)
    
print("\n") 

# Modifying a Tuple
# Reassigning a new tuple to the same variable
dimensions = (1280, 720)
print("Modified dimensions:", dimensions)

# Tuples with one item
single_item_tuple = (5,)
print("Single item tuple:", single_item_tuple)

# Tuple unpacking
width, height = dimensions
print("Width:", width)
print("Height:", height)

# Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
for pair in nested_tuple:
    print("Pair:", pair)
    
print("\n")

# Advantages of Tuples
# Tuples can be used as keys in dictionaries due to their immutability
tuple_key = (1, 2)
my_dict = {tuple_key: "This is a tuple key"}
print("Dictionary with tuple key:", my_dict)

# Tuples can be more memory efficient than lists
import sys

list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print("Memory size of list:", sys.getsizeof(list_example))
print("Memory size of tuple:", sys.getsizeof(tuple_example))

# Conclusion
# Tuples are a useful data type in Python for storing ordered, immutable collections of items.
# They offer advantages in terms of memory efficiency and can be used as dictionary keys.
# Understanding tuples is essential for effective Python programming.
# End of the tutorial on Tuples in Python.