#Q1: Write a Python program to take two numbers as input and print their sum, difference, product, and quotient.
# Taking two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing arithmetic operations
sum_result = num1 + num2  # Addition
difference = num1 - num2  # Subtraction
product = num1 * num2  # Multiplication
quotient = num1 / num2  # Division

# Printing the results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#Q2: Given a number n, calculate and print its square and cube.
# Taking input from user
n = int(input("Enter a number: "))

# Calculating square and cube
square = n ** 2  # Square of the number
cube = n ** 3  # Cube of the number

# Printing the results
print("Square of", n, "is:", square)
print("Cube of", n, "is:", cube)

#Q3: Assign two boolean values (True or False) to two variables and print the result of and, or, and not operations between them.
# Assigning boolean values
a = True
b = False

# Logical operations
print("a AND b:", a and b)  # True if both are True
print("a OR b:", a or b)  # True if at least one is True
print("NOT a:", not a)  # Negation of a

#Q4: Take a number as input and update its value by adding 5 using the += operator, then print the new value.
# Taking input
num = int(input("Enter a number: "))

# Updating value using += operator
num += 5  # Equivalent to num = num + 5

# Printing updated value
print("Updated value:", num)

#Q5: Assign a value to a variable, multiply it by 3 using the *= operator, and print the updated value.

# Assigning a value to a variable
num = 4

# Using *= operator to multiply by 3
num *= 3  # Equivalent to num = num * 3

# Printing the updated value
print("Updated value:", num)


#Q6: Create a list with five numbers and print whether 10 is in the list using the in operator.
# Creating a list with five numbers
numbers = [2, 5, 10, 15, 20]

# Checking if 10 is in the list
print("Is 10 in the list?", 10 in numbers)  # Returns True if found, else False

#Q7: Create a string and check whether the letter 'z' is not in the string using the not in operator.
# Defining a string
text = "hello world"

# Checking if 'z' is NOT in the string
print("Is 'z' NOT in the string?", 'z' not in text)  # Returns True if 'z' is not present

#Q8: Assign the same integer value to two different variables and print the result of checking if both refer to the same memory location using is.

# Assigning the same integer value to two variables
x = 100
y = 100

# Checking if both refer to the same memory location
print("Do x and y refer to the same object?", x is y)  # True for small integers (-5 to 256 in Python)


#Q9: Create two lists with identical elements and print whether they refer to the same object using is not.

# Creating two lists with identical elements
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Checking if they are different objects in memory
print("Do list1 and list2 refer to different objects?", list1 is not list2)  # True because they are stored separately
