


def flatten_rowwise(my_list):
    ans = []
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            ans.append(my_list[i][j])
    return ans


# z = flatten_rowwise(my_li)
# print(z)


my_li = [[1, 2, 3],
         [4, 5],
         [6, 7, 8]]

def flatten_rowwise_second(my_list):
    ans = []
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            ans.append(my_list[i][j])
    return ans


z = flatten_rowwise_second(my_li)
print(z)
