# Strings and String Concatenation in Python
# A string is a sequence of characters enclosed in quotes.
# You can use either single quotes (' ') or double quotes (" ") to define a string.
# Strings can be concatenated (joined together) using the + operator.

my_name = "Reagan Jake"
greetings = "My name is " + my_name + ". Nice to meet you!"
print(greetings)

my_name = "Reagan Jake Ongaya"
print("Hello, " + my_name + "! Welcome to the world of Python programming.")

#Use of \n\t for new line and tab space
info = "Name:\n\t" + my_name + "\nAge:\n\t23\nLocation:\n\tNairobi, Kenya"
print(info)

#The rstrip() method removes any trailing characters (characters at the end of a string), space is the default trailing character to remove.
name_with_space = "Reagan Jake Ongaya     "
print("Hello, " + name_with_space + "! Welcome to Python.")
clean_name_without_space = name_with_space.rstrip()
print("Hello, " + clean_name_without_space + "! Welcome to Python.")