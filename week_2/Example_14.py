# Greatest common divisor(GCD) of two numbers - naive version
a = int(input("Please insert number: "))
b = int(input("Please insert number: "))
for r in range(a, 0, -1):
    if a % r == 0 and b % r == 0:
        break
print("The GCD of", a, "and", b, "is", r)