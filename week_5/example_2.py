"""
Printing array both ways
"""


# http://pythontutor.com/visualize.html#mode=edit

# region print_array
def print_array(lst):  # 1, 2, 3
    if len(lst) == 0:
        return
    else:
        print(lst[0])
        print_array(lst[1:])

# endregion
# region print_array_reverse  # 3, 2, 1
def print_array_reverse(lst):
    if len(lst) == 0:
        return
    else:
        print_array_reverse(lst[1:])
        print(lst[0])


# endregion


lst = [1, 2, 3]
print_array(lst)
print_array_reverse(lst)
