#implicit Type Casting

num1 = 10 # int
num2 = 3.6 # float
result = num1 + num2
#print(result)
#print(type(result))

# implicit- int to complex
a = 5
c = 2 + 3j
result1 = a + c
#print(result1)
#print(type(result1))

#implicit int with boolean
# in python it consider 0 as false , 1 as True

a = 10
b = True

result2 = a + b
#print(result2)
#print(type(result2))

#Explicit Type Casting
num1  = "10" #str
#print(type(num1))
num1 = int(num1)
#print(type(num1))
num2 = 5 #int
result = num1 + num2
#print(result)

my_list = [3, 5, 6, 8, 9, 3, 5, 10]
print(type(my_list))
my_list = set(my_list)
print(type(my_list))
my_list = list(my_list)
print(my_list)
print(type(my_list))
