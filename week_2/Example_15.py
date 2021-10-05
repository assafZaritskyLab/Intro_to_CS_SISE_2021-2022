# Greatest common divisor(GCD) of two numbers - Euclidean Algorithm
# •	If A = B*Q + R and B≠0 then GCD(A,B) = GCD(B,R) where Q is an integer, R is an integer between 0 and B-1
a = int(input("Please insert the first number: "))
b = int(input("Please insert the second number: "))
j = a
i = b
while i != 0:
    reminder = j % i
    j = i
    i = reminder
print("The GCD of", a, "and", b, "is", j)
