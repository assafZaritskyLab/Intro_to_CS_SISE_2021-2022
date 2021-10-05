class Count:
    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        raise StopIteration


count = Count(0, 3)
print(next(count))
print(next(count))
for n in count:
    print(n)
# print(sum(count))





