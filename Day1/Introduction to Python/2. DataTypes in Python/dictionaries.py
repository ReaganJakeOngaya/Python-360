# Dictionaries
# A dictionary is a collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type and can be duplicated.
# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
user_public = True
# Accessing values
print(my_dict["name"])  # Output: Alice

for key, value in my_dict.items():
    if user_public:
        print(f"{key}: {value}")
    else:
        print("Data is private")
        
# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)

# Updating a dictionary value
my_dict["age"] = 31
update_dict = my_dict
print(update_dict)