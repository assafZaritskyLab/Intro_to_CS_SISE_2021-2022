class Count:
    """
    Iterator that counts
    """

    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


count = Count()
print(next(count))
print(next(count))
for n in count:
    print(n)

