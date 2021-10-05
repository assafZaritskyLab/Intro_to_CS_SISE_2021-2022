
# nested conditional statement

n = int(input("Please insert an integer number: "))
if n % 2 == 0:
    if n % 5 == 0:  # NESTED if
        print(n, 'is divisible by 2 and by 5, so also by 10.')
    else:  # NESTED else, pertains to NESTED if.
        print(n, 'is divisible by 2 but not by 5.')
elif n % 5 == 0:
    print(n, 'is divisible by 5 but not by 2.')
else:
    print(n, 'is not divisible by 2 and 5.')