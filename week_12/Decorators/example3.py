
"""
examples for builtin decorators
"""
from functools import lru_cache

num_of_calls = 0


@lru_cache(maxsize=20)
def factorial(n):
    global num_of_calls
    num_of_calls += 1
    return n * factorial(n-1) if n != 0 else 1


print(f"factorial(10) = {factorial(10)}")
print(f"num_of_calls = {num_of_calls}")
num_of_calls = 0
print(f"factorial(11) = {factorial(11)}")
print(f"num_of_calls = {num_of_calls}")
num_of_calls = 0
print(f"factorial(8) = {factorial(8)}")
print(f"num_of_calls = {num_of_calls}")
num_of_calls = 0
print(f"factorial(13) = {factorial(13)}")
print(f"num_of_calls = {num_of_calls}")
