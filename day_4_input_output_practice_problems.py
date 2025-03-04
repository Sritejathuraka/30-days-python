# Ask the user for their name and store it in the variable 'name'
name = input("Enter your name: ")
print("Hello,", name + "! Welcome to Python.")

# Take two numbers as input from the user, split them by space, and convert them to integers
a, b = map(int, input("Enter two numbers separated by space: ").split())
sum_result = a + b
print("Sum:", sum_result)

# Take three color names as input from the user and split them into a list
color1, color2, color3 = input("Enter three favorite colors separated by space: ").split()
print(color1, color2, color3, sep="-")

# Print the sentence without using multiple print() statements by setting 'end' parameter
print("Python", end=" ")
print("is", end=" ")
print("awesome")