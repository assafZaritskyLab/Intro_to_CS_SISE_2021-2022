def example_1():
    no_one = [False, False, False]
    some_ones = [True, False, True]
    every_one = [True, True, True]
    empty_one = []
    print('any:')
    print(any(no_one))
    print(any(some_ones))
    print(any(every_one))
    print(any(empty_one))

    print('all:')
    print(all(no_one))
    print(all(some_ones))
    print(all(every_one))
    print(all(empty_one))


# example_1()


def example_2():
    a = [1, 2]
    b = [1, 2, 3, 4]
    l1 = [element in b for element in a]
    print(l1)

# example_2()


def example_3():
    a = [1, 2]
    b = [1, 2, 3, 4]
    l1 = all([element in b for element in a])
    print(l1)

# example_3()


def example_4():
    b = [1, 2, 3, 4]
    l1 = [element % 2 == 0 for element in b]
    print(l1)
    print(all(l1))
    print(any(l1))


# example_4()


l1 = [0, 1, 2]
print(all(l1))  # False
print(any(l1))  # True
# 0 - False
# <>0 - True


# def all(list):
#     for a in list:
#         if a == False:
#             return False
#     return True
#
#
# def any(list):
#     for a in list:
#         if a == True:
#             return True
#     return False


