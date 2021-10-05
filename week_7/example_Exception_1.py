def exception_example(lst, i, value):
    if i >= len(lst):
        raise IndexError("given index is greater than list length")
    if type(value) != int:
        raise TypeError("given type is not int")
    if value not in lst:
        raise ValueError("given value is not in list")
    return lst[i], lst.index(value)

# region example 0
# a, b = exception_example([1, 2, 3], 2, 1)
# print(f"a = {a}")
# print(f"a = {b}")
# endregion

# region example 1
# a, b = exception_example([1, 2, 3], 2, 1.1)
# print(f"a = {a}")
# print(f"a = {b}")
# endregion

# region example 2
# try:
#     a, b = exception_example([1, 2, 3], 2, 1)
# except Exception as e:
#     print("Exception has occurred!")
# else:
#     print(f"a = {a}")
#     print(f"a = {b}")
# endregion

# region example 3
# try:
#     a, b = exception_example([1, 2, 3], 2, 1.1)
# except:
#     # print(e)
#     print("Exception has occurred!")
# else:
#     print(a, b)
# endregion

# region example 4
# # In this example we want to print the error
# try:
#     a, b = exception_example([1, 2, 3], 2, 1.1)
# except IndexError as e:
#     print("IndexError Exception:", e)
# except TypeError as e1:
#     print("TypeError Exception:", e1)
# except ValueError as e:
#     print("ValueError Exception:", e)
# except Exception as e:
#     print("Something else happened:", e)
# else:
#     print(a, b)
#
# print("shir")
# endregion

# region example 5
# # In this example we want the same behavior for different exceptions
# # there is no special handling for ValueError
# # and we also don't need to print the error
# # No else statement
try:
    a, b = exception_example([1, 2, 3], 4, 1)
except (TypeError):
    print("TypeError Exception")
except Exception:
    # print("Something went wrong!")
    pass

print("s")
# endregion
