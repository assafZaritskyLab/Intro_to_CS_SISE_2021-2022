class SmallValueError(Exception):
    """Raised when input value is too small"""
    pass


def divide(x, y):
    if y > -10:  # 0 > -10
        raise SmallValueError('y is smaller than -10')
    print(x / y)


# divide(50, 10)
#
# divide(50, -11)

# divide(50, 0)

