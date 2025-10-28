# Numbers and floats in Python
# Python has several numeric data types, the most common being int (integer) and float (floating-point number).
# You can perform various arithmetic operations using these numeric types.
# Integer (int) - whole numbers without a decimal point
# Floats - numbers with a decimal point

age = 23
print("I am " + str(age) + " years old.")

# Floating-point number (float) - numbers with a decimal point
height = 5.6
print("My height is " + str(height) + " feet.")

# Basic arithmetic operations
a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b  # Returns the largest integer less than or equal to the division result
modulus = a % b          # Returns the remainder of the division
exponentiation = a ** b   # Raises a to the power of b
print("Addition: " + str(addition))
print("Subtraction: " + str(subtraction))
print("Multiplication: " + str(multiplication))
print("Division: " + str(division))
print("Floor Division: " + str(floor_division))
print("Modulus: " + str(modulus))
print("Exponentiation: " + str(exponentiation))

# Type conversion
int_to_float = float(age)  # Convert int to float
float_to_int = int(height)  # Convert float to int (truncates decimal part)
print("Integer to Float: " + str(int_to_float))
print("Float to Integer: " + str(float_to_int))

# Using the built-in round() function to round a float to the nearest integer
rounded_height = round(height)
print("Rounded Height: " + str(rounded_height))

# Using the built-in abs() function to get the absolute value of a number
negative_number = -15
absolute_value = abs(negative_number)
print("Absolute Value: " + str(absolute_value))

# Using the built-in pow() function to raise a number to a power
power_value = pow(a, b)  # Equivalent to a ** b
print("Power Value using pow(): " + str(power_value))

# Using the built-in divmod() function to get quotient and remainder
quotient, remainder = divmod(a, b)
print("Quotient: " + str(quotient))
print("Remainder: " + str(remainder))       

# Using the built-in max() and min() functions to find the maximum and minimum of two numbers
maximum_value = max(a, b)
minimum_value = min(a, b)
print("Maximum Value: " + str(maximum_value))
print("Minimum Value: " + str(minimum_value))       

# Using the built-in sum() function to get the sum of a list of numbers
numbers_list = [a, b, 5, 7, 9]
total_sum = sum(numbers_list)
print("Total Sum: " + str(total_sum))

# Using the built-in round() function to round a float to a specified number of decimal places
precise_height = round(height, 1)  # Rounds to 1 decimal place  
print("Height rounded to 1 decimal place: " + str(precise_height))

# Using the built-in format() function to format numbers
formatted_number = format(1234567.89123, ',.2f')  # Formats number with commas and 2 decimal places
print("Formatted Number: " + str(formatted_number))

# Using the built-in complex() function to create a complex number
complex_number = complex(2, 3)  # 2 is the real part
print("Complex Number: " + str(complex_number)) #3 is the imaginary part

# Using the built-in isinstance() function to check the type of a variable
is_age_int = isinstance(age, int)
print("Is age an integer? " + str(is_age_int))

is_height_float = isinstance(height, float)
print("Is height a float? " + str(is_height_float))
is_complex_number = isinstance(complex_number, complex)
print("Is complex_number a complex number? " + str(is_complex_number))

# Using the built-in type() function to get the type of a variable
age_type = type(age)
print("Age Type: " + str(age_type))
height_type = type(height)
print("Height Type: " + str(height_type))
complex_number_type = type(complex_number)
print("Complex Number Type: " + str(complex_number_type))

# Using the built-in bin(), oct(), and hex() functions to convert integers to binary, octal, and hexadecimal representations
binary_representation = bin(a)  # Binary representation
octal_representation = oct(a)   # Octal representation
hexadecimal_representation = hex(a)  # Hexadecimal representation
print("Binary Representation of " + str(a) + ": " + str(binary_representation))
print("Octal Representation of " + str(a) + ": " + str(octal_representation))
print("Hexadecimal Representation of " + str(a) + ": " + str(hexadecimal_representation))


# Using the built-in int() function to convert binary, octal, and hexadecimal strings back to integers
int_from_binary = int(binary_representation, 2)
int_from_octal = int(octal_representation, 8)
int_from_hexadecimal = int(hexadecimal_representation, 16)
print("Integer from Binary: " + str(int_from_binary))
print("Integer from Octal: " + str(int_from_octal))
print("Integer from Hexadecimal: " + str(int_from_hexadecimal))

# Using the built-in float() function to convert a string to a float
float_from_string = float("23.45")      
print("Float from String: " + str(float_from_string))

# Using the built-in int() function to convert a string to an integer
int_from_string = int("42")
print("Integer from String: " + str(int_from_string))

# Using the built-in complex() function to convert a string to a complex number
complex_from_string = complex("2+3j")
print("Complex Number from String: " + str(complex_from_string))

# Using the built-in round() function to round a float to the nearest integer
rounded_value = round(4.7)
print("Rounded Value of 4.7: " + str(rounded_value))

# Using the built-in abs() function to get the absolute value of a float
absolute_float_value = abs(-9.81)
print("Absolute Value of -9.81: " + str(absolute_float_value))

# Using the built-in pow() function to raise a float to a power
float_power_value = pow(2.5, 3)
print("2.5 raised to the power of 3 using pow(): " + str(float_power_value))

# Using the built-in divmod() function to get quotient and remainder of floats
float_quotient, float_remainder = divmod(7.5, 2.5)
print("Float Quotient: " + str(float_quotient))
print("Float Remainder: " + str(float_remainder))

# Using the built-in max() and min() functions to find the maximum and minimum of two floats
max_float_value = max(3.5, 7.2)
min_float_value = min(3.5, 7.2)
print("Maximum Float Value: " + str(max_float_value))
print("Minimum Float Value: " + str(min_float_value))

# Using the built-in sum() function to get the sum of a list of floats
float_numbers_list = [1.5, 2.5, 3.5, 4.5]
total_float_sum = sum(float_numbers_list)
print("Total Float Sum: " + str(total_float_sum))   

# Using the built-in format() function to format floats
formatted_float_number = format(12345.6789, ',.3f')  #Formats float with commas and 3 decimal places
print("Formatted Float Number: " + str(formatted_float_number))

# Using the built-in isinstance() function to check the type of a float variable
is_height_float = isinstance(height, float)
print("Is height a float? " + str(is_height_float))

# Using the built-in type() function to get the type of a float variable
height_type = type(height)  
print("Height Type: " + str(height_type))

# Using the built-in round() function to round a float to a specified number of decimal places
precise_height = round(height, 2)  # Rounds to 2 decimal places
print("Height rounded to 2 decimal places: " + str(precise_height))
 
# Using the built-in format() function to format floats
formatted_float_number = format(98765.4321, ',.4f')  #Formats float with commas and 4 decimal places
print("Formatted Float Number: " + str(formatted_float_number))

#underscore(_) as a visual separator for large numbers
large_number = 1_000_000_000
print("Large Number with underscores: " + str(large_number))

# Using the built-in isinstance() function to check the type of a large number variable
is_large_number_int = isinstance(large_number, int)
print("Is large_number an integer? " + str(is_large_number_int))

