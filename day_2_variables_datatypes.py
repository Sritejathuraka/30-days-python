# declaring a variable

fruit_name = "apple"
fruit_quantity = 5
fruit_price = 1.5

#Datatypes
#Numeric type
'''
.int: - 20, 30, 20,-2 , -3
.float: 3.14, 2.09, - 4.52
.complex: 3+4j, 7+6j
'''

age = 20 #int
price = 2.5 #float
complex = 2+4j #complex

# Boolean
'''
true or false
'''
is_raining = False

#sequence Types

'''
str - string : collection of characters enclosed in quotes
list : is a collection of different types of elements - mutable(it can modify after creation)
tuple: is a collection of different types of elements - immutable(can not be modify after creation)
'''
person_name = "teja"
fruit_list = ["apple", 5, 1.5]
fruit_tuple = ("apple", 5, 1.5)
fruit_list[1] = "mango"
fruit_list[2] = "orange"


# setType
'''
.set - it stores a unique and unordered elements - mutable
.frozenset - it stores a unique and unordered elements - immutable
'''
my_set = {3, 5, 5, 7,4,9,10,5,3,2}
my_frozenset = frozenset([5,6,2,8,8,3,2,2])

#mapping
'''
.dict - it is used to store key-value pair
'''
my_dict = "name"

print(type(my_dict))