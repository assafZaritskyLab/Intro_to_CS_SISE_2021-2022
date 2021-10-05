class square_all_it:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self


squares_iterator = square_all_it([x for x in range(3)])

print(squares_iterator)
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))

# todo http://pythontutor.com/visualize.html#mode=edit

