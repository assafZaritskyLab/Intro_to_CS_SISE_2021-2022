# Square all generator


def square_all_gen(numbers):
    for n in numbers:
        yield n ** 2  # return Generator, wait next()


my_numbers = [x for x in range(10)]
squeres_all_gen = square_all_gen(my_numbers)
print(squeres_all_gen)
print(next(squeres_all_gen))
print(next(squeres_all_gen))
print(next(squeres_all_gen))
print(next(squeres_all_gen))
# todo http://pythontutor.com/visualize.html#mode=edit

# todo another way
my_numbers = [x for x in range(10)]
square_all_gen = (n ** 2 for n in my_numbers)
print(square_all_gen)
for x in square_all_gen:
    print(x)
