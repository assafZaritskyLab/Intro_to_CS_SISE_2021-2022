from functools import total_ordering

class Vector:

    def __init__(self, cords):
        self.cords = tuple(cords)

    def __repr__(self):
        return str(self.cords)

    def norm(self):
        return sum([x ** 2 for x in self.cords]) ** 0.5

    def cords(self):
        return self.cords

    def __gt__(self, other):  # >
        return self.norm() > other.norm()

    def __eq__(self, other):
        return self.norm() == self.norm()


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])
print(sorted([v1, v2, v3]))
print(v1 > v2)
print(v1 < v2)
print(Vector([1, 2, 3]) == Vector([1, 2, 3]))
print(Vector([1, 2, 3]) != Vector([1, 2, 3]))
print(Vector([4, 5, 6]) >= Vector([1, 2, 3]))

print("==", v1 == v2)
print("!=", v1 != v2)
print(">:", v1 > v2)
print("<:", v1 < v2)
print(">=:", v1 >= v2)
print("<=:", v1 <= v2)
