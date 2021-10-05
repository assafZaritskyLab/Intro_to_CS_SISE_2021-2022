# if-else statemet # 14, 7 # 18, 6
a = int(input("Please insert an integer number: "))
b = int(input("Please insert another integer number: "))
if a % 7 == b % 7:  # compare between the reminders
    print("The numbers have the same reminder by 7")
else:
    print("The numbers have different reminders by 7")