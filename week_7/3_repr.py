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

        if not isinstance(lst, list):
            raise ValueError("Wrong parameter type")
        self.values = copy.copy(lst)
        self.name = "shir"

    def __repr__(self):
        """
        print function override
        """
        return str(self.values) + str(self.name)


list_vector = [1, 2, 3]
v_1 = Vector(list_vector)  # __init__
print(v_1.values)
print(v_1)