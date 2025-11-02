# Lists in Python
#Lists are ordered collections of items that can hold multiple values in a single variable.
#Lists are defined using square brackets [] and items are separated by commas.
fruits = ['Apple', 'Banana', 'Cherry']
print("Fruits List: " , fruits)

# Accessing list items using indexing (0-based index)
first_fruit = fruits[0]
print("First Fruit: " + first_fruit)

# Modifying list items
fruits[1] = 'Blueberry'
print("Modified Fruits List: " , fruits)

# Adding items to a list using append() method
fruits.append('Orange')
print("Fruits List after append: " , fruits)

# Removing items from a list using remove() method
fruits.remove('Cherry')
print("Fruits List after remove: " , fruits)

# Using the len() function to get the number of items in a list
number_of_fruits = len(fruits)
print("Number of fruits in the list: " + str(number_of_fruits))

#Using the insert() method to add an item at a specific position
fruits.insert(1, 'Mango')
print("Fruits List after insert: " , fruits)

# Using the pop() method to remove an item at a specific position
removed_fruit = fruits.pop(2)
print("Fruits List after pop: " , fruits)
print("Removed Fruit: " + removed_fruit)    

# Using the sort() method to sort the list in ascending order
fruits.sort()
print("Sorted Fruits List: " , fruits)

#Using the del() method to remove an item at a specific position
del fruits[0]

#adding multiple items to a list using extend() method
fruits.extend(['Pineapple', 'Grapes'])
print("Fruits List after extend: " , fruits)

#Deliting multiple items from a list using slicing
del fruits[1:3]
print("Fruits List after del: " , fruits)

#printing reversed list using slicing
reversed_fruits = fruits[::-1]
print("Reversed Fruits List: " , reversed_fruits)

#printing using the reverse() method
fruits.reverse()
print("Fruits List after reverse(): " , fruits)

# Using the index() method to find the index of an item in the list
banana_index = fruits.index('Banana') if 'Banana' in fruits else -1
print("Index of Banana: " + str(banana_index))

# Using the clear() method to remove all items from the list
fruits.clear()
print("Fruits List after clear: " , fruits)

#Making Numerical Lists using range() function
numbers = list(range(1, 11))  # Creates a list of numbers from 1 to 10
print("Numerical List: " , numbers)