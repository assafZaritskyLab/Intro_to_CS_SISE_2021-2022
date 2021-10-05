class StaticFieldExample:
    sf = 0

    def __init__(self, x):
        self.x = x


o1 = StaticFieldExample(5)
o2 = StaticFieldExample(10)
print(f"o1.sf = {o1.sf}, o2.sf = {o2.sf}")
print(f"o1.x = {o1.x}, o2.x = {o2.x}")

StaticFieldExample.sf = 1
print(f"o1.sf = {o1.sf}, o2.sf = {o2.sf}")

StaticFieldExample.sf = 0
o1 = StaticFieldExample(5)
o2 = StaticFieldExample(10)
print(f"o1.sf = {o1.sf}, o2.sf = {o2.sf}")

o1.sf = 1
print(f"o1.sf = {o1.sf}, o2.sf = {o2.sf}")

StaticFieldExample.sf = 2
print(f"o1.sf = {o1.sf}, o2.sf = {o2.sf}")