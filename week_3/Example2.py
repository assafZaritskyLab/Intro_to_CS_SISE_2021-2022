def len_3():
    my_li2 = [[1, 2, 3],
              [4, 5],
              [6, 7, 8]]
    for i in range(3):  # sub list - number colum
        for j in range(len(my_li2)):  # main list
            # TODO remove  if i < len(my_li2[j]): i = 2; j = 1
            if i < len(my_li2[j]):
                print(my_li2[j][i])


# len_3()

def number():
    my_li2 = [[1, 2, 3], [4, 5], [6, 7, 8, 100]]

    for i in range(3):  # sub list
        for j in range(len(my_li2)):  # main list
            if i < len(my_li2[j]):
                print(my_li2[j][i])


# number()

def longest_column():
    my_li2 = [[1, 2, 3],
              [4, 5],
              [6, 7, 8, 10000]]

    longest_col = 0
    for i in range(len(my_li2)):  # main list
        if len(my_li2[i]) > longest_col:  # sub list
            longest_col = len(my_li2[i])

    for i in range(longest_col):  # i = 0.. 4
        # [0,0] -> [1,0] -> [2,0]
        for j in range(len(my_li2)):  # j =0... 3
            if i < len(my_li2[j]):
                print(my_li2[j][i])

longest_column()
