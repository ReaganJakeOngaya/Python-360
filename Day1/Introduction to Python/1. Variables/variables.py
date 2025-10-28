# The "\n" is used to create a new line in the output.

message = "Hello, Reagan! \nThis is a Python script."
print(message)

#multiple assignment
x, y, z = 5, 10.5, "Python"
print("x:", x)
print("y:", y)
print("z:", z)

# Swapping values of two variables
a = 15
b = 30
print("Before swapping:")
print("a:", a)
print("b:", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp
print("After swapping:")
print("a:", a)
print("b:", b)

# Swapping without using a temporary variable
a, b = b, a
print("After swapping without temp variable:")
print("a:", a)
print("b:", b)

# Constants in Python (by convention, constants are written in uppercase)
PI = 3.14159
GRAVITY = 9.81  # m/s^2
print("Value of PI:", PI)   
print("Value of GRAVITY:", GRAVITY)

# Using augmented assignment operators
count = 0
count += 1
print("Count after incrementing:", count)

count *= 5
print("Count after multiplying by 5:", count)
count -= 3
print("Count after decrementing by 3:", count)

count /= 2
print("Count after dividing by 2:", count)  

# Multiple variable assignment and augmented assignment
width = height = depth = 10
print("Width:", width)
print("Height:", height)
print("Depth:", depth)

volume = width * height * depth
print("Volume of the cube:", volume)

# Using augmented assignment to update volume
volume += 100
print("Updated Volume after adding 100:", volume)
