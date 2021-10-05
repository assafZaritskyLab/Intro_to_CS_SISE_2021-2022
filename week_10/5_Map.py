

# def map_function(function_arg, l1):
#     for x in l1:
#         yield function_arg(x)  # yield = return generator
#
#
# ans = map_function(cube, range(10))

def cube(x): return x ** 3

def example_1():
    print(map(cube, range(10)))
    print(list(map(cube, range(10))))
    print(type(map(cube, range(10))))


# example_1()


def calc_sum(x1, x2):
    return x1 + x2


def example_1B():
    print(list(map(calc_sum, [1, 2, 3, 4, 5], [10, 20, 30])))


def example_2():
    weights = [70, 80, 90, 82]
    heights = [172, 172, 175, 188]
    BMI_res = []
    for i in range(len(weights)):
        height_m = heights[i] / 100
        BMI = weights[i] / (height_m ** 2)
        BMI_res.append(BMI)

    for i in range(len(BMI_res)):
        if BMI > 18.5 and BMI_res[i] < 25:
            BMI_res[i] = "Good!"
        else:
            BMI_res[i] = "Bad!"
    print(heights)
    print(weights)
    print(BMI_res)


def calc_BMI(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)


def BMI_result(BMI):
    if BMI > 18.5 and BMI < 25:
        return "Good!"
    return "Bad!"


def example_3():
    weights = [70, 80, 90, 82]
    heights = [172, 172, 175, 188]
    BMI_res = map(BMI_result, map(calc_BMI, weights, heights))
    print(heights)
    print(weights)
    print(list(BMI_res))


# example_1()
# example_1B()
# example_2()
# example_3()

# Lazy loading
def example_4():
    l1 = [1, 2, 3]
    l2 = []
    l3 = map(l2.append, l1)
    print(l2)
    print(l3)

    l1 = [1, 2, 3]
    l2 = []
    l3 = list(map(l2.append, l1))
    print(l3)
    print(l2)
# example_4()


def example_4B():
    l1 = [1, 2, 3]
    l2 = []
    return_from_map = map(l2.append, l1)
    print(return_from_map)
    print(type(return_from_map))
    print(l2)


def example_5():
    l1 = [1, 2, 3]
    l2 = []
    it = map(l2.append, l1)
    print(l2)
    next(it)
    print(l2)
    next(it)
    print(l2)
    next(it)
    print(l2)


# example_4B()
example_5()
