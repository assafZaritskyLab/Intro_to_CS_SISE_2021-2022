"""
LIS
"""


def longest_increasing(lst):
    return longest_increasing_rec(lst, 0)


def longest_increasing_rec(lst, last_used):
    if len(lst) == 0:
        return 0
    with_next = 0
    if lst[0] > last_used:  # 40 , .... last_used = 20
        with_next = 1 + longest_increasing_rec(lst[1:], lst[0])
    without_next = longest_increasing_rec(lst[1:], last_used)  # max(with_next, without_next)
    return max(with_next, without_next)


print(longest_increasing([1, 2, 8, 3]))

# print(longest_increasing([14, 19, 1, 232, 40, 41, 85, 87, 88, 200]))
# print(longest_increasing([20, 20, 1, 232, 40, 41, 85, 90, 87, 88, 200]))
