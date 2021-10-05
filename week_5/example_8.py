
# http://pythontutor.com/visualize.html#mode=edit


# reading an array with/out slicing for less pythonTutor demo
def longest_increasing_slicing(lst):
    return longest_increasing_rec_slicing(lst, 0)


def longest_increasing_rec_slicing(lst, last_used):
    if len(lst) == 0:
        return 0
    with_next = 0
    if lst[0] > last_used:
        with_next = 1 + longest_increasing_rec_slicing(lst[1:], lst[0])
    without_next = longest_increasing_rec_slicing(lst[1:], last_used)
    return max(with_next, without_next)


def longest_increasing_no_slicing(lst):
    return longest_increasing_rec_no_slicing(lst, 0, 0)


def longest_increasing_rec_no_slicing(lst, last_used, prog_index):
    if len(lst) - prog_index == 0:
        return 0
    with_next = 0
    if lst[prog_index] > last_used:
        with_next = 1 + longest_increasing_rec_no_slicing(lst, lst[prog_index], prog_index + 1)
    without_next = longest_increasing_rec_no_slicing(lst, last_used, prog_index + 1)
    return max(with_next, without_next)


a1 = [1, 9, 77, 1, 4, 5]

print(longest_increasing_slicing(a1))
print(longest_increasing_no_slicing(a1))

