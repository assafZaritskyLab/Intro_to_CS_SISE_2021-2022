## Example 3: Choose n of k

# todo without debug - we believe!!!
def choose(n, k):
    if k == 0 or n == k:
        return 1
    if n < k:
        return 0
    return choose(n - 1, k - 1) + choose(n - 1, k)


print(choose(4, 2))
print(choose(4, 3))
print(choose(6, 4))  # (6*5)/(6-4)!
