## Example 2: Inheritance problem


def partition(lst):
    return partition_helper(lst, 0, 0)


def partition_helper(lst, liora, yosi):
    if not lst:  # lst == []
        return liora == yosi
    return partition_helper(lst[1:], liora + lst[0], yosi) or partition_helper(lst[1:], liora, yosi + lst[0])

print(partition([2, 9, 6, 1]))
print(partition([2, 9, 6]))
