def example_1():
    numbers = [5, 3, 4, 6]
    print(sorted(numbers))
    print(sorted(numbers, reverse=True))  # decreasing


# example_1()


def example_2():
    names = ["Apple", "apple", "Banana", "Avocado"]
    print(names)
    print(sorted(names))
    print(sorted(names, key=len))  # sort by length of string


# example_2()


def tail(collection): return collection[-1]  # one liner!!


def example_3():
    names = ["Apple", "apple", "Banana", "Avocado"]
    print(tail(names))
    print(tail(names[0]))
    print(sorted(names, key=tail))  # key is a function
    print(names)  # TODO in-place?

    names = ["apple", "Apple", "Banana", "Avocado"]
    print(sorted(names, key=tail))  # TODO apple ? Apple?


example_3()










def my_comparator(string): return len(string), string


def example_4():
    names = ["Avocado", "Apple", "Banana", "apple", "Baboon"]
    print(sorted(names, key=my_comparator))

# example_4()
