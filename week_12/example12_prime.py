## Infinite prime counter

class infinit_counter:
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            curr = self.start
            self.start += 1
            return curr
        raise StopIteration


def is_prime(x):
    #     print(int(x**0.5))
    for num in range(2, int(x ** 0.5) + 1):
        if x % num == 0:
            return False
    return True


counter = infinit_counter(2, end=10)
prime_gen = (x for x in counter if is_prime(x))


print(type(counter))
print(type(iter(counter)))
print(type(prime_gen))
for i in prime_gen:
    print(i)

# def func():
#     for x in counter:
#         if is_prime(x):
#             yield x

