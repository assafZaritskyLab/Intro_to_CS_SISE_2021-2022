# create multiplication table
multiplication_table = []
for i in range(4):
    multiplication_table.append([])
    for j in range(4):
        multiplication_table[i].append(i * j)

for row in multiplication_table:
    print(row)

#  create multiplication table - using list comprehension
mul_table = [[x * y for x in range(4)] for y in range(4)]
print(mul_table)
