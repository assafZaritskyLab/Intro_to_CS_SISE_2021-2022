# Tuples

### Tuples are faster to create
# tuple_example_1 = ()
# for x in range(10):
#      tuple_example_1 += (x,)
tuple_example = tuple(x for x in range(10))  # immutable
list_example = list(x for x in range(10))  # mutable


t = ("don't", 'worry', 'be', 'happy')
print(t)
print(t[0])
print(t[-1])
print(t[1:3])

