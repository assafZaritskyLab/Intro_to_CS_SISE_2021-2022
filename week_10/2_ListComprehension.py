def example_1():
    l1 = [x for x in 'Python']
    print(l1)


def example_2():
    l1 = [x for x in (1, 2, 3, 4)]
    print(l1)


def example_3():
    l1 = [x for x in ('Bgu', 'here', 'i', 'come')]  # 1st level only!!
    print(l1)


def example_4():
    d = {'a': 1, 'b': 2}
    l1 = [x for x in d]  # keys only
    print(l1)


def example_5():
    list = [1, 2, 3, 4]
    tuple = ('Bgu', 'for', 'you')
    l1 = [x for x in list if x % 2 == 0]
    print(l1)
    # l2 = []
    # for x in tuple:
    #     if 'u' in x:
    #         l2.append(x)
    l2 = [x for x in tuple if 'u' in x]
    print(l2)


example_5()


def example_6():
    l1 = [x for x in [1, 2, 3, 4] if x % 2 == 0 if x > 3]
    print(l1)


def example_7():
    l1 = [x for x in [1, 2, 3, 4] if x % 2 == 0 and x > 3]
    print(l1)


# example_1()
# example_2()
# example_3()
# example_4()
# example_6()
# example_7()