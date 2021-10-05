### Question 4 - 2 dices
rolls = {}
for dice1 in range(1, 7):  # first die
    for dice2 in range(1, 7):  # second die
        newTuple = (dice1, dice2)
        total = dice1 + dice2
        combinations = rolls.get(total, [])
        combinations.append(newTuple)
        rolls[total] = combinations  # why?
print(rolls)
print(rolls.items())
for key, value in rolls.items():  # print result # todo
    percentage = len(value) / 36.0
    print(f"{key}: {int(100 * (percentage))}%")


list_tmp = ["a", "b", "c", "d"]
for index, value in enumerate(list_tmp):
    print("index = ", index, "value = ", value)


