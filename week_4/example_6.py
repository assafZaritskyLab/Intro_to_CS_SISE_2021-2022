### Question 1 - Remove duplicates in-place - A good solution


# todo http://pythontutor.com/visualize.html#mode=edit

def remove_duplicates_v2(x):
    """
    Remove duplicates in-place

    :param x: a list of elements.
    :return: A list without duplicated elements
    """
    seen_elements = []
    i = -1
    while i < len(x) - 1:
        i = i + 1
        if x[i] not in seen_elements:
            seen_elements.append(x[i])
        else:
            x.pop(i)  # i = 1  [1, 1, X, 2, 2, 2, 3, 1] -> [1, X, 2, 2, 2, 3, 1] ->  i = 0
            i = i - 1


li1 = [1, 1, 1, 2, 2, 2, 3, 1]
# li1 = [1,2,1,2,1,2,1,2]
# li1 = [1,2,3,4]
print(li1)
remove_duplicates_v2(li1)
print(li1)
