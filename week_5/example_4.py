"""
GCD
Greatest common divisor(GCD) of two numbers - Euclidean Algorithm

"""

# region gcd
def gcd(a, b):
    while b != 0:
        reminder = a % b
        a = b
        b = reminder
    return a
# endregion

# region rec_gcd
def rec_gcd(a, b):
    if b == 0:
        return a
    return rec_gcd(b, a % b)

# endregion


a, b = 123, 36
# print(gcd(a, b))
print(rec_gcd(a, b))

a, b = 24, 60
print(gcd(a, b))
print(rec_gcd(a, b))

# print(60 % 24)  # 12
# print(24 % 60)  # 24
