import unittest
from Calculator import Calculate


class Unittest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculate()

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 8), 14)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 8), 40)

    def test_substract(self):
        self.assertEqual(self.calculator.substract(5, 8), -3)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()
