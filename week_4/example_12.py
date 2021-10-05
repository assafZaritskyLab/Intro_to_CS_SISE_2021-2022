### Question 3 - Students and grades
students = [["yael", 87], ["yuval", 88], ["amir", 100]]
print(students)

# students = ("yael" : 87, "yuval": 88, "amir": 100)
# students = ["yael": 87, "yuval": 88, "amir": 100]
students = {"yael": 87, "yuval": 88, "amir": 100}
# students = {("yael" : 87), ("yuval" : 88), ("amir" : 100)}


students_l = [["yael", 87], ["yuval", 88], ["amir", 100]]
students_d = {"yael": 87, "yuval": 88, "amir": 100}

def get_grade_l(students, name):
    """students is a nested list, name is a string"""
    for stud in students:  # main list
        if stud[0] == name:  # sub list
            return stud[1]


def get_grade_d(students, name):
    """students is a dictionary, name is a string"""
    return students[name]


print(get_grade_l(students_l, 'yael'))
print(get_grade_d(students_d, 'yael'))

