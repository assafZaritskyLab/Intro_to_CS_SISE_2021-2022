from functools import reduce

# squared = lambda x, y: x ** y
# print(squared(4, 5))


# print(map(lambda x, y: (x, y), range(10), map(lambda x: x ** 2, range(10))))
# print(list(map(lambda x, y: (x, y), range(10), map(lambda x: x ** 2, range(10)))))


d = {'dani': 30, 'yossi': 25, 'liat': 29, 'shira': 28}
print(d.keys())
print(sorted(d.keys(), key=lambda name: d[name]))

l1 = list(range(100, 1001, 100))
print(l1)
l2 = list(filter(lambda x: x >= 200 and x <= 800, l1))
print(l2)
#
# l1 = list(range(100, 1001, 100))
# print(l1)
# print(list(filter(lambda x: x >= 200 and x <= 800, l1)))
# print(list(map(lambda x: int((x - 200) / 6), filter(lambda x: x >= 200 and x <= 800, l1))))
#
m1 = [[4, 6, 3, 6], [4, 6, 4, 7, 3, 4], [5, 4, 3, 6]]  # wanted - [97, 142, 86]
l1 = list(map(lambda lst: reduce(lambda x, y: x + y, lst), map(lambda lst: map(lambda num: num ** 2, lst), m1)))
# print(l1)
