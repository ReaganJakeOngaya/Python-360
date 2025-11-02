# This script demonstrates the use of a for loop in Python.
# for loops are used to iterate over a sequence (like a list, tuple, or string).
#They are best used when the number of iterations is known beforehand.


# For loop example: Welcoming new students to a Python course
new_students = ["Reagan", "Mike", "Peter", "Mercy", "Alice", "Makee"]

for student in new_students:
    print("Welcome to the Python course, " + student + "!")
    
# Output:
# Welcome to the Python course, Reagan!
# Welcome to the Python course, Mike!
# Welcome to the Python course, Peter!
# Welcome to the Python course, Mercy!
# Welcome to the Python course, Alice!
# Welcome to the Python course, Makee!

# In this example, the for loop iterates over each name in the new_students list.
# For each iteration, it prints a welcome message personalized with the student's name.

#slicing in for loops
for student in new_students[0:3]:
    print("Hi " + student + ", welcome aboard! You are among the first three students to join.")

for student in new_students[3:]:
    print("Hello " + student + ", glad to have you with us!")

#copying a list
student_registered = new_students[:]
print("Registered Students: ", student_registered)


new_students.extend(["John","Pedro"])
print("New Students after appending: ", new_students)

#copying a list using for loop
updated_students = []

for student in new_students:
    updated_students.append(student)
print("Updated Students List: ", updated_students)

# Another example: Calculating the square of numbers in a list
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    square = number ** 2
    print("The square of", number, "is", square)    
    
# Doing something after a for loop
print("All done!")

#Making numerical lists using range() function and for loop
# happy newyear countdown


for num in range(10, 0, -1):  # This will generate a countdown from 10 to 0
    print("Number:", num)
print("Happy New Year!")

# checking for the unregistered students
unregistered_students = []

for student in new_students:
    if student not in student_registered:
        unregistered_students.append(student)

print("Unregistered Students: ", unregistered_students)
