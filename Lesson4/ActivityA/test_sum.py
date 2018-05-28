import unittest

from sum import *

class TestSum(unittest.TestCase):

    def test_sum_1(self):
        self.assertEqual(add_numbers(1,2), 3, "expected sum of 1 and 2 to be 3 but got " + str(add_numbers(1,2)))

    def test_sum_2(self):
        self.assertEqual(add_numbers(10,20), 30, "expected sum of 10 and 20 to be 30 but got " + str(add_numbers(10,20)))

    def test_sum_3(self):
        self.assertEqual(add_three_numbers(10,20,30), 60, "expected sum of 10, 20 and 30 to be 60 but got" + str(add_three_numbers(10,20,30)))

if __name__ == "__main__":
    unittest.main()
