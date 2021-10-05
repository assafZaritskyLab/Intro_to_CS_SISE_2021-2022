def merge(l1, l2):
    """
    Merging 2 sorted lists into one sorted list - O(n1)+O(n2)
    :param l1: sorted list, not changing.
    :param l2: sorted list, not changing.
    :return: sorted list with all members of l1 and l2
    """
    res = []
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:  # adding the smallest
            res.append(l1[i1])
            i1 += 1
        else:
            res.append(l2[i2])
            i2 += 1
    res += l1[i1:] + l2[i2:]  # adding the rest of the list unhandled
    return res


def merge_sort(lst):
    """
    Sorting a list with O(log2(n))
    :param lst: a (probably) unsorted list
    :return: a sorted list
    """
    n = len(lst)
    if n <= 1:
        return lst
    return merge(merge_sort(lst[0:n // 2]), merge_sort(lst[n // 2:n]))
    # two recursive calls, both half's of the list


# %%

ls = [4, 1, 7, 2, 19, -10]
print(ls)
ls = merge_sort(ls)
