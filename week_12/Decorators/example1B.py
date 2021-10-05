def decorate_any_print(func1):  # fuc1 = print_with_prefix
    def inner():
        print('########################')
        func1()
        print('########################')

    return inner


@decorate_any_print
def print_with_prefix() -> None:
    print("This does something")


print_with_prefix()
