### Question 1 - Remove duplicates in-place

# todo http://pythontutor.com/visualize.html#mode=edit


def remove_duplicates_v2(x):
    """
    Remove duplicates in-place.

    :param x: a list of elements.
    :return:
    """
    seen_elements = []
    for elem in x:
        if elem not in seen_elements:
            seen_elements.append(elem)
    x = list(seen_elements)


li = [1, 1, 2]
print(li)
remove_duplicates_v2(li)
print(li)
