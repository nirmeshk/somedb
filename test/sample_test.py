import unittest


def func(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test_answer(self):
        assert func(3) == 4
