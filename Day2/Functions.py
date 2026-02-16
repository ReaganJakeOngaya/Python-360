# They are blocks of code that perform a specific task. 
# They are reusable and can be called multiple times in a program. 
# Functions can take parameters and return values. They help to organize code and make it more readable.

def greet_user(botName="PythonBot", modelYear=2023):
    name = input("Please enter your name: ")
    print(f"Hello, {name}! I am {botName}. I was created in {modelYear}. You can ask me anything about Python programming. I am a Python bot created to assist you in learning Python. Let's have fun coding together!")

greet_user("Alice", 2023)