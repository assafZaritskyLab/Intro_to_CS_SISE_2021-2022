### Counter example:

class Person:
    counter = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.counter += 1


print(f"The number of persons in the system is: {Person.counter}")

p1 = Person("Yossi", "Cohen", 30)
p2 = Person("Ron", "Levi", 22)
print(f"The number of persons in the system is: {Person.counter}")

p3 = Person("Ronit", "Israeli", 22)
print(f"The number of persons in the system is: {p1.counter}")
print(f"The number of persons in the system is: {Person.counter}")
p1 = Person("Yossi", "Cohen", 30)
p2 = Person("Ron", "Levi", 22)
print(f"The number of persons in the system is: {Person.counter}")
