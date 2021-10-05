## Looping twice

numbers = [1, 2, 3, 4, 5]
squares_list = [n ** 2 for n in numbers]
print(type(squares_list))
print(squares_list)

numbers = [1, 2, 3, 4, 5]
squares = (n ** 2 for n in numbers)
print(type(squares))
print(squares)
print(tuple(squares))
print(tuple(squares))

# print(list(squares))
# print(list(squares))
