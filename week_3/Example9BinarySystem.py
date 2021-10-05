# while True:
#     x = int(input("Give number"))
#     if x == 0:
#         break

def get_odd():
    flag = True
    ans = 0
    while flag:
        x = int(input("Insert a number between 1 to 7 to keep playing and 0 to stop playing"))
        if x == 0:
            flag = False
        else:
            ans = ans ^ x  # ^ = XOR

    return ans


print(get_odd())


