def addition_two_numbers(a, b):
    return a + b

result = addition_two_numbers(3, 7)
#print("The result is", result)

#lambda x, y: x + y
result2 = lambda x, y: x + y
#print("The Second Result is,", result2(3, 7))

numbers = [1, 2, 3, 4, 5, 6]
filtered_even = list(filter(lambda n: n % 2 == 0, numbers ))
print("Filtered Even", filtered_even)

squared_numbers = list(map(lambda n: n * n, numbers))
print("squared numbers", squared_numbers)

tuple = [('a', 10), ('e', 2), ('c', 3), ('d', 1)]

sorted_tuple = sorted(tuple, key=lambda n: n[1], reverse=True)
print("Sorted Tuple", sorted_tuple)
