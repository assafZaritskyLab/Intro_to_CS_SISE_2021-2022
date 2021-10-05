import copy


class Vector:
    """
    A class used to represent a vector.
    :attribute values: a list of numbers that describe the vector.
    """

    def __init__(self, lst):
        """
        Constructor for vector class.
        :param lst: a list of numbers
        """
        self.values = lst


list_vector = [3, 3, 7]
v_1 = Vector(list_vector)  # __init__
print(v_1.values)
# list_vector.append(10)
# print(v_1.values)
