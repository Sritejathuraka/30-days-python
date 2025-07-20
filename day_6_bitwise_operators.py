##Bitwise Operators
# 
# #AND (&)
a = 5
b = 6
print("result for a & b is",a & b )

print(bin(a & b))

##OR(|)
a = 10
b = 11

print("Result for OR |", a | b)


# XOR (^)

a = 14
b = 15
print("result for XOR is", a ^ b)


# NOT (~)

a = 12
print("result for NOT", ~a)


#Left Shift <<
a = 9
print("Left shift by 1", a << 2)

#RIGHT Shift <<
a = 9
print("RIGHT  shift by 1", a >> 2)

#Practice Examples
# 1. Check if a number is even or odd using bitwise operator
def is_even(n):
    return (n & 1) == 0 # Explanation: The last bit of even numbers is always 0. So n & 1 will be 0 if even, 1 if odd.

# Example
print(is_even(4))  # True (even)
print(is_even(5))  # False (odd)

#2. Swap two numbers without using a third variable

a = 5
b = 9

a = a ^ b
b = a ^ b
a = a ^ b #Explanation: Using XOR to swap values. Neat bitwise trick!

print(a, b)  # Output: 9 5

#3 Left Shift
a = 3    # 0011
print(a << 1)  # Output: 6 (0110) Explanation: Left shift multiplies by 2 → 3 × 2 = 6

#4 Check if a number is a power of 2 using bitwise AND
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(1))   # True (2^0)
print(is_power_of_two(2))   # True (2^1)
print(is_power_of_two(16))  # True (2^4)
print(is_power_of_two(18))  # False
print(is_power_of_two(0))   # False

