def example_1(x):
    if x % 2 == 0:
        print(str(x) + ' is even.')
    else:
        print(str(x) + ' is odd.')


def example_1_better(x):
    print(str(x) + (' is even.' if x % 2 == 0 else ' is odd.'))


def example_2(x):
    print(x ** 0.5)


# example_2(9)  # 3.0
# example_2(-9)  # (1.8369701987210297e-16+3j)


def example_2_better(x):
    print(x ** 0.5) if x >= 0 else print("{} i".format((-x) ** 0.5))


# example_2_better(9)  # 3.0
# example_2_better(-9)  # 3.0 i


def example_3():
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    print(str(a) + '=' + str(b) if a == b else str(a) + '>' + str(b) if a > b else str(a) + '<' + str(b))
