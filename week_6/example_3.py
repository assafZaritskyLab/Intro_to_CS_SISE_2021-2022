from sympy.series.gruntz import timeit


def partition(lst):
    return partition_helper(lst, 0, 0)


def partition_helper(lst, liora, yosi):
    if not lst:
        return liora == yosi
    return partition_helper(lst[1:], liora + lst[0], yosi) or partition_helper(lst[1:], liora, yosi + lst[0])


def partition_memo(lst):
    return partition_memo_helper(lst, 0, 0, {})


def partition_memo_helper(lst, s1, s2, memo):
    if not lst:  # lst == []
        return s1 == s2
    key = (len(lst), s1, s2)
    if key not in memo:
        give_Liora = partition_memo_helper(lst[1:], s1 + lst[0], s2, memo)
        give_Yosi = partition_memo_helper(lst[1:], s1, lst[0] + s2, memo)
        memo[key] = give_Liora or give_Yosi
    # else:
    #     print(key)
    return memo[key]


print(partition_memo([9, 1, 1, 1, 1, 1, 1, 1, 1]))  # len = 9  # (6, 10, 1)

# 1, 1, 1, 1, 1, 1
# 9, 1
# 1



# print(partition([9, 1, 1, 1, 1, 1, 1, 1, 1]))
# print(partition_memo([2, 9, 6, 1, 1]))
# print(partition_memo([2, 9, 6, 1]))

# print("time it no memo")
# print("%.20f" %timeit(partition([9, 1, 1, 1, 1, 1, 1, 1, 1])))
# print("time it with memo")
# print("%.20f" %timeit(partition_memo([9, 1, 1, 1, 1, 1, 1, 1, 1])))