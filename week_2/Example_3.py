
#  if-elif-else statement
a = int(input("Please insert the first side: "))
b = int(input("Please insert the second side: "))
c = int(input("Please insert the third side: "))

if a == b == c:  # There are all equal
    print("Equilateral triangle")
elif a == b or a == c or b == c:  # only two equal
    print("Isosceles triangle")
else:  # all three sides have different lengths
    print("Scalene triangle")