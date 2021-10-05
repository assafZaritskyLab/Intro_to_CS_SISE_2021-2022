def decorate_any_print(func1):  # -> None : Annotations for return type
    def inner():
        print('########################')
        func1()
        print('########################')

    return inner


def print_with_prefix() -> None:
    print("This does something")


pretty = decorate_any_print(print_with_prefix)
pretty()


