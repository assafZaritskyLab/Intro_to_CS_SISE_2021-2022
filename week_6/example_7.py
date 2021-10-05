# Example 5: Insertion sort

def insertion_sort(lst):
    for i in range(1, len(lst)):  # Traverse through 1 to len(lst)
        value = lst[i]
        j = i - 1
        # move elements of lst[0…i-1], that are greater than value
        while j >= 0 and lst[j] > value:  # lst = [1, 4, 7, 2, 19, -10],  j = 2  value = 2
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value  # assign the value to appropriate cell in the list

# [ 3, 2, 1]


ls = [4, 1, 7, 2, 19, -10]
print(ls)
insertion_sort(ls)
print(ls)