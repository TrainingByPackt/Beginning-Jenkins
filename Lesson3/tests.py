import unittest

from run import *


class TestNumbers(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(type(sumOfNumbers(1,2)) is int)
    
    def test_sum(self):
        self.assertEqual(sumOfNumbers(1,2), 3)




if __name__ == "__main__":
    unittest.main()