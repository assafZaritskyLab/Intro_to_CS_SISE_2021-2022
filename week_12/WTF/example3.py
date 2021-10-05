## Unpacking

counts = {'apples': 2, 'oranges': 1}
x, y = counts
print(x)
print(y)

counts = {'apples': 2, 'oranges': 1}
dict_iter = iter(counts)
print(next(dict_iter))
print(next(dict_iter))


# x, y, z = [1, 2, 3]  # A list
# print(x, y, z)
#
# x, y, z = 1, 2, 3  # A tuple
# print(x, y, z)
#
# x, y, z = {1: 'a', 2: 'b', 3: 'c'}  # A dictionary
# print(x, y, z)
#
# x, y, z = (a for a in (1, 2, 3))  # A generator
# print(x, y, z)
