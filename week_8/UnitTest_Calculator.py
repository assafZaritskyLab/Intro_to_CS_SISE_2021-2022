class Calculator:

    # def __add__(self, a):
    #     return self + a
    def add(self, a, b):  # __add__
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


import unittest

c = Calculator()


class TestTirgul8(unittest.TestCase):

    def test_add(self):
        self.assertEqual(c.add(2, 5), 7)
        self.assertEqual(c.add(0, 0), 0)
        self.assertEqual(c.add(-10, 10), 0)

    def test_sub(self):
        self.assertEqual(c.sub(100, 15), 85)
        self.assertEqual(c.sub(4, 10), -6)
        self.assertEqual(c.sub(0, 0), 0)
        self.assertEqual(c.sub(50, 50), 0)

    def test_mul(self):
        self.assertEqual(c.mul(0, 15), 0)
        self.assertEqual(c.mul(1, 10), 10)
        self.assertEqual(c.mul(3, 7), 21)
        self.assertEqual(c.mul(7, 3), 21)

    def test_div(self):
        self.assertEqual(c.div(75, 25), 3)
        self.assertEqual(c.div(0, 10), 0)
        self.assertEqual(c.div(7, 1), 7)
        self.assertEqual(c.div(10, 4), 2.5)


if __name__ == "__main__":
    unittest.main()  # TODO: fail
    #  verbosity=2 more detailed information
    # main supports being used from the interactive interpreter by passing in the argument exit=False.
    # This displays the result on standard output without calling sys.exit():


