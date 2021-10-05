
#  determine whether a number is prime or not
number = int(input("Enter a number larger than 1: "))
is_prime = True  # assuming the number is prime
i = 2
while i < number and is_prime:  # check from 2 to number - 1
    if number % i == 0:
        is_prime = False
    i += 1  # i = i + 1
if is_prime:
    print("The chosen number is prime")
else:
    print("The chosen number is not prime")