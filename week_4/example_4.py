### Question 1 - Remove duplicates from a list

def remove_duplicates_v1(x):
    """

    Return a new list without duplicates

    :param x: a list of elements.
    :return: A list without duplicated elements
    """
    seen_elements = []
    for elem in x:
        if elem not in seen_elements:
            seen_elements.append(elem)
        else:
            print(elem)
    return seen_elements


remove_duplicates_v1([1, 1, 1, 2, 2, 2, 3, 1])
