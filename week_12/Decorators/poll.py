def star(func):
    def inner(*args, **kwargs):
        print("*" * 3)
        func(*args, **kwargs)
        print("*" * 3)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 3)
        func(*args, **kwargs)
        print("%" * 3)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
