# Example 1: Ascending digits number
def is_ascending_digits(num):
    """
    Determines if a number has only real ascending digits (from the right).
    :param num: a positive integer number
    :return: true / false
    """
    if num < 10:
        return True
    if num % 10 >= num // 10 % 10:  # num = 1942 -> num % 10 = 2 ,  num // 10 % 10 = 4
        return False
    return is_ascending_digits(num // 10)  # 1942//10 = 194.2



print(is_ascending_digits(1942))  # 1 > 9 , 9 < 4
# print(is_ascending_digits(987321))
# print(is_ascending_digits(1))
# print(is_ascending_digits(11))


