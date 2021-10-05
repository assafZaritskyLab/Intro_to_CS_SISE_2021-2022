
# def squares(x):
#     return x**2
#
#
# def funky_for_loop(iterable, action_to_do):
#     for item in iterable:
#         print(action_to_do(item))
#
#
# number = [1, 2, 3]
# funky_for_loop(number, squares)



def squares(x):
    return x**2

def funky_for_loop_iter(iterable, action_to_do):
    """"
        The code pretty much defines the way looping works under the hood in Python.
    """
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            print(action_to_do(item))


number = [1, 2, 3]
funky_for_loop_iter(number, squares)

