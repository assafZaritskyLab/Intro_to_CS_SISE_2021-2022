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



# v_1 = Vector("shir")
# # v_1 = Vector(5000)
# print(v_1.values)

try:
    v_1 = Vector("shir")
except ValueError as e1:
    print(e1)
# except Exception as e:
#     print(e)
# except OverflowError as e:
#     print(e)


print("init vector")

