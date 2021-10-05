def is_above_70(x): return x > 70
def example_1():
    grades = [55, 82, 47, 95, 88, 68, 99]
    print(filter(is_above_70, grades))
    print(grades)
    print(list(filter(is_above_70, grades)))
    print(type(filter(is_above_70, grades)))


def valid_test_grades(grades): return grades >= 0 and grades <= 100


def example_2():
    more_grades = [103, -18, 79, 55, 990, 73, 200, 99, 0]
    print(more_grades)
    print(list(filter(valid_test_grades, more_grades)))


example_1()
example_2()