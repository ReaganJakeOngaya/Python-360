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
updated_dict = my_dict
print(updated_dict)
print(my_dict)

for key, value in sorted(my_dict.items()):
    if user_public:
        print(f"{key}: {value}")
    else:
        print("Data is private")

# Removing a key-value pair
del my_dict["city"]
print(my_dict) 

# Nested Dictionaries
people_dict = {
    "person1": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles",
        "job": "Designer",
        "skills": ["Photoshop", "Illustrator", "Figma"]
    },
    "person2": {
        "name": "Carol",
        "age": 28,
        "city": "Chicago",
        "job": "Manager",
        "skills": ["Leadership", "Communication", "Strategic Planning"]
    }
}

for person, details in people_dict.items():
    print(f"\nDetails of {person}:")
    for key, value in details.items():
        if user_public:
            print(f"{key}: {value}")
        else:
            print("Data is private") 