"""
Fast power
"""
import time

def fast_pow(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_pow(x ** 2, n / 2)
    return x * fast_pow(x ** 2, (n - 1) / 2)


print(fast_pow(2, 8))
print(2 ** 8)


# print(fast_pow(2, 80))
# print(2 ** 80)

