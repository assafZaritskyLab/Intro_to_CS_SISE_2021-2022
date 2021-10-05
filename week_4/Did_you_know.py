#
# ##### Did you know?
#
# def div_with_portion_and_reminder(num, div):
#     """num and div are positive integers"""
#     return num // div, num % div
#
#
# res = div_with_portion_and_reminder(50, 7)
# print(res)
# print(type(res))
#
#

def build(n):
    if n == 0:
        return []
    x = build(n-1)
    x.append(n)
    return x

# def build_1(n):
#     if n == 0:
#         return []
#     x = build_0(n-1)
#     x.append(n)
#     return x
#
# def build_0(n):
#     if n == 0:
#         return []
#     x = build_0(n-1)
#     x.append(n)
#     return x

print(build_2(2))
