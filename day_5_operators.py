## ** Arithmetic Operators **
## ** returns the numeric values **
a = 20
b = 3
print("Addition of a,b is", a + b) # 23
print("Subtraction of a,b is", a - b) # 17
print("Multiplication of a,b is", a * b) # 60
print("Division of a,b is", a / b) # 6.6667
print("Modulus of a,b is", a % b) # 2
print("floor division of a,b is", a // b) # 6
print("Exponentiation of a,b is", a ** b) #8000

## ** Assignment Operators **
a = 10  # Assign 10 to 'a'

a += 5   # Same as a = a + 5
print("a += 5:", a)  # 15

a -= 3   # Same as a = a - 3
print("a -= 3:", a)  # 12

a *= 2   # Same as a = a * 2
print("a *= 2:", a)  # 24

a /= 4   # Same as a = a / 4
print("a /= 4:", a)  # 6.0 (division always returns float)

a //= 2  # Same as a = a // 2
print("a //= 2:", a)  # 3 (floor division)

a %= 2   # Same as a = a % 2
print("a %= 2:", a)  # 1 (remainder)

a **= 3  # Same as a = a ** 3
print("a **= 3:", a)  # 1 ** 3 = 1
                       

 ## ** Comparision Operators *
a = 10
b = 5
print("a == b:", a == b)   # False (10 is not equal to 5)
print("a != b:", a != b)   # True (10 is not equal to 5)
print("a > b:", a > b)     # True (10 is greater than 5)
print("a < b:", a < b)     # False (10 is not less than 5)
print("a >= b:", a >= b)   # True (10 is greater than or equal to 5)
print("a <= b:", a <= b)   # False (10 is not less than or equal to 5)

## ** Logical Operators **
a = True
b = False

print("a and b:", a and b)  # False (Both must be True)
print("a or b:", a or b)    # True (At least one must be True)
print("not a:", not a)      # False (Inverts True to False)



## ** Identity Operators **
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print("a is b:", a is b)        # True (same memory location for integers)
print("a is not b:", a is not b)  # False

print("c is d:", c is d)        # False (different objects, even if values are the same)
print("c is not d:", c is not d)  # True

## ** Membership Operators **
numbers = [1, 2, 3, 4, 5]
text = "Hello, Python!"

print(3 in numbers)      # True (3 exists in the list)
print(10 in numbers)     # False (10 is not in the list)
print("Python" in text)  # True (Substring "Python" exists in text)
print("Java" not in text) # True ("Java" is not in the text)


