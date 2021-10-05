class Vector:

    def __init__(self, cords):
        self.cords = tuple(cords)

    def __repr__(self):
        return str(self.cords)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])
print(sorted([v1, v2, v3]))

