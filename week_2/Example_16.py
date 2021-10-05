# #  Longest repeating substring
str_1 = input("Insert the first string ")
str_2 = input("Insert the second string ")
len_1 = len(str_1)
max_common = 0
for i in range(len_1):
    for j in range(i + 1, len_1 + 1):
        print(str_1[i:j])
        if str_1[i: j] in str_2:
            if j - i > max_common:
                max_common = j - i
                print(str_1[i: j])
    print("end")
print("The longest repeating substring = ", max_common)
