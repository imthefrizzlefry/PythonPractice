import unittest
import socks

class sockPairTests(unittest.TestCase):
    def test_singlePairOfSocks(self):
        inputArray = [1,1]
        inputSize = 2

        expectedPairs = 1

        self.assertEqual(expectedPairs, socks.sockMerchant(inputSize, inputArray))

    def test_HackerRankTestCase1(self):
        inputArray = [10,20,20,10,10,30,50,10,20]
        inputSize = 9

        expectedPairs = 3

        self.assertEqual(expectedPairs, socks.sockMerchant(inputSize, inputArray))

    def test_HackerRankTestCase8(self):
        inputArray = [1,1,3,1,2,1,3,3,3,3]
        inputSize = 10

        expectedPairs = 4

        self.assertEqual(expectedPairs, socks.sockMerchant(inputSize, inputArray))