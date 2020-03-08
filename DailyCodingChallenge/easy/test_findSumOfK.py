import unittest
from findSumOfK import findSumOfK

class findSumOfKTests(unittest.TestCase):
    def test_findSumOfTests_Example(self):
        s = [10, 15, 3, 7]
        k = 17

        self.assertTrue(findSumOfK(s, k))

    def test_findSumOfTests_ReturnsFalse(self):
        s = [10, 15, 3, 7]
        k = 20

        self.assertFalse(findSumOfK(s, k))

    def test_findSumOfTests_NegativeKValue(self):
        s = [10, -15, 3, 7]
        k = -12

        self.assertTrue(findSumOfK(s, k))

    def test_findSumOfTests_NegativeNumbersInSet(self):
        s = [10, 15, -3, 7]
        k = 12

        self.assertTrue(findSumOfK(s, k))

    def test_findSumOfTests_EmptySet(self):
        s = []
        k = 12

        self.assertFalse(findSumOfK(s, k))
    