import unittest


def exception_example(lst, i, value):
    if i >= len(lst):
        raise IndexError("given index is greater than list length")
    if type(value) != int:
        raise TypeError("given type is not int")
    if value not in lst:
        raise ValueError("given value is not in list")
    return lst[i], lst.index(value)


class TestTirgul8(unittest.TestCase):
    def test_exception_example(self):
        self.assertEqual(exception_example([1, 2, 3], 2, 1), (3, 0))
        with self.assertRaises(TypeError):
            exception_example([1, 2, 3], 2, 1.1)
        with self.assertRaises(ValueError):
            exception_example([1, 2, 3], 2, 5)
        with self.assertRaises(IndexError):
            exception_example([1, 2, 3], 3, 1)


unittest.main(argv=[''], verbosity=2, exit=False)
