def print_array_with_wrapper(lst, idx):
    if len(lst) >= idx:
        return
    else:
        print(lst[idx])
        print_array_with_wrapper(lst, idx + 1)


def print_array_wrapper(lst):
    return print_array_with_wrapper(lst, 0)


lst = [1, 2, 3]
print_array_wrapper(lst)