from functools import reduce

# 0 + 1 +2 = 3
def add_nums(x, y):
    print("s")
    return x + y


def example_1():
    print(reduce(add_nums, range(11)))
    print(type(reduce(add_nums, range(11))))


def example_2():
    print(reduce(add_nums, range(11)))
    print(type(reduce(add_nums, range(11))))
    print(reduce(add_nums, range(11), 10))


example_1()
# example_2()