# Exceptions in python are runtime errors that allow developers to 
# handle errors properly without stopping the program
# Common exceptions include ValueError, TypeError, ZeroDivisionError, etc.
# We can use try-except blocks to catch and handle exceptions gracefully

# Example of handling a ValueError when converting a string to an integer
user_input = "abc"
try:
    number = int(user_input)
    print(f"The number is: {number}")
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer.")
    
# Example of handling a ZeroDivisionError
num1 = 10
num2 = 0
try:
    result = num1/num2
    print(f"{num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print(f"Error: Cannot divide by zero ('{num2}')")
    
# Example of handling a TypeError
value1 = "Hello"
value2 = 5
try:    
    combined = value1 + value2
    print(f"Combined value: {combined}")
except TypeError:
    print(f"Error: Cannot combine '{value1}' (str) and '{value2}' (int)")
    
    
# We can also create custom exceptions by defining a new class that 
# inherits from the built-in Exception class
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"Caught a custom error: {e}")
    