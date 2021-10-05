def fibonacci_mem(n):
    """ Wrapper function for fib,
        with memoization in a dictionary """

    # initial dictionary with f0 and f1
    fib_dict = {0: 1, 1: 1}
    return fib(n, fib_dict)


def fib(n, fib_dict):
    # print(n)  # diagnostic printing
    if n not in fib_dict:
        res = fib(n - 1, fib_dict) + fib(n - 2, fib_dict)
        fib_dict[n] = res
    return fib_dict[n]


print(fibonacci_mem(6))
