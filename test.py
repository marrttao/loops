# test.py

import unittest
from main import number_of_digits, number_of_zero, sum_of_number, middle_average

class TestNumberOperations(unittest.TestCase):

    def test_positive_integer_digits(self):
        result = number_of_digits(12345, test_mode=True)
        self.assertEqual(result, 5)

    def test_negative_number_digits(self):
        result = number_of_digits(-12345, test_mode=True)
        self.assertEqual(result, 0)

    def test_large_number_digits(self):
        result = number_of_digits(10**100, test_mode=True)
        self.assertEqual(result, 101)

    def test_number_of_zero(self):
        result = number_of_zero(1002003, test_mode=True)
        self.assertEqual(result, 4)

    def test_sum_of_number(self):
        result = sum_of_number(12345, test_mode=True)
        self.assertEqual(result, 15)

    def test_middle_average(self):
        result = middle_average(12345, test_mode=True)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
