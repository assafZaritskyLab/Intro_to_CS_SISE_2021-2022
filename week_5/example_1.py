import time

"""
ITERATIVE VS RECURSION
"""


# region sum_of_digits_iter_func
def sum_of_digits_iter_func(number_digits):
    current_sum = 0
    while number_digits > 0:
        digit = number_digits % 10
        current_sum += digit
        number_digits = number_digits // 10  # // = Floor division
    return current_sum

# endregion

# region sum_of_digits_rec_func
def sum_of_digits_rec_func(number_digits):
    if not number_digits:  # 0 = False
        return 0
    return number_digits % 10 + sum_of_digits_rec_func(number_digits // 10)

# endregion

# number_digits = 47109823112  # 47109823112 -> 4+7+1+0+9+8+2+3+1+1+2 = 38
# print(sum_of_digits_iter_func(number_digits))
# # print(sum_of_digits_rec_func(number_digits))


def sum_of_digits_rec_func_12(number_digits):
    if not number_digits:  # 0 = False
        return 0
    return number_digits % 10 + sum_of_digits_rec_func_1(number_digits // 10)


def sum_of_digits_rec_func_1(number_digits):
    if not number_digits:  # 0 = False
        return 0
    return number_digits % 10 + sum_of_digits_rec_func_0(number_digits // 10)


def sum_of_digits_rec_func_0(number_digits):
    if not number_digits:  # 0 = False
        return 0
    return number_digits % 10 + sum_of_digits_rec_func(number_digits // 10)


number_digits = 12  # 12 = 1 + 2 = 3
print(sum_of_digits_rec_func_12(number_digits))
