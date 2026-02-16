# The function pauses the program and waits for the user to enter data.

input = input("Please enter your age: ")
if int(input) <= 17:
    print("You are a minor.")
else:
    print("You are an adult.")