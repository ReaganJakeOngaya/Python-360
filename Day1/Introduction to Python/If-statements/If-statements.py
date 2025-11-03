# If statements
# They are used to make decisions in code based on conditions.


age = 12
licenced = True

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
cars = ["Toyota", "BMW", "Audi", "Mercedes"]

for car in cars:
    if car == "BMW" or car == "Audi" or car == "Mercedes":
        print(car + " is a luxury car.")
    else:
        print(car + " is a regular car. No offense to Toyota owners.")
        
if age >= 18 and licenced:
    print("You can drive a car.")
elif licenced == False:
    print("You cannot drive a car. Please obtain a license.")
elif age < 18:
    print("You cannot drive a car. You are too young.")
    
print("You cannot drive a car.")

# Nested if statements
if age >= 18:
    if licenced:
        print("You can drive a car.")
    else:
        print("You cannot drive a car. Please obtain a license.")
        
else:
    print("You cannot drive a car. You are too young.")
    
# Ternary operator
status = "adult" if age >= 18 else "minor"
print("You are an " + status + ".")

# Example with multiple conditions
temperature = 25
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
elif temperature > 10:
    print("It's a cool day.")
else:
    print("It's a cold day.")
    
# Using 'in' keyword 
