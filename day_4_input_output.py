# Output concept in python

# Standard output
print("Hello, World!")

personName = "Arjun"
print(personName)

# Formatted output

name = "Arjun"
age = 10
print(f"My name is {name} and my age is {age} ")


# output with seperator

print("python", "is","awesome", sep=(" | "))

# output with end

print("python", end=(" @ "))
print("is", end=(" 3 "))
print("awesome")

# Output combining both Sep and end

print("python", "java", "c++", sep=(" | "), end=(" "))
print("are popular languages")


# Input in Python
name = input("Enter name:")

# **Int input**
age = int(input("ENter age:"))

# **Float input**
price = float(input("Enter price"))

## **Boolean input**
is_raining = bool(input("is Raining"))
is_raining = bool(int(input("Enter 1  for True, 0 for False:")))
print("is Raining", is_raining)
print("datatype is", type(is_raining))

## **Taking multiple input**

name, age, city = input("Enter Details:").split(",")
print("name is:", name)
print("age is:", age)
print("city is:", city)

a, b = map(int,input("Enter two numbers:").split())
print("Sum is:", a + b)

# **Taking List input**

numbers = set(list(input("Enter numbers:").split()))
print("Numbers list is", numbers)