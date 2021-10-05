"""
Now with arguments
"""


def protect_from_zero(func1):
    def inner(a, b):
        if b == 0:
            print("b can not be 0, protecting!")
            b = 1
        return func1(a, b)

    return inner


@protect_from_zero
def division_without_remainder(a: int, b: int):
    return int(a / b)


division_without_remainder(5, 0)


# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner()