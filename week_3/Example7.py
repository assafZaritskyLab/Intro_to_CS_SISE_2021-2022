def is_prime(x):
    is_prime = True,
    i = 2
    while i <= x ** 0.5:
        if x % i == 0:
            is_prime = False
            break
        i += 1
    return is_prime


def print_prime_in_range(x):
    for i in range(2, x):
        if is_prime(i):
            print(i)


print_prime_in_range(1000)