import unittest
import bestBuyingPrice

class bestBuyingPriceTests(unittest.TestCase):
    def test_ExampleSet(self):
        inputArray = [3,7,9,14,5,8,1,11,7,13,0,7]
        expectedResult = 12

        self.assertEqual(expectedResult, bestBuyingPrice.findMaxGain(inputArray))

    def test_emptyInputList(self):
        inputArray=[]
        expectedResult = 0

        self.assertEqual(expectedResult, bestBuyingPrice.findMaxGain(inputArray))

    def test_positiveGain(self):
        inputArray=[5,6]
        expectedResult = 1

        self.assertEqual(expectedResult, bestBuyingPrice.findMaxGain(inputArray))

    def test_noGain(self):
        inputArray=[5,5]
        expectedResult = 0

        self.assertEqual(expectedResult, bestBuyingPrice.findMaxGain(inputArray))

    def test_negativeGain(self):
        inputArray=[5,4]
        expectedResult = 0

        self.assertEqual(expectedResult, bestBuyingPrice.findMaxGain(inputArray))

    def test_firstPairGraiterGainThanLaterPair(self):
        inputArray=[5,10,4,6]
        expectedResult = 5

        self.assertEqual(expectedResult, bestBuyingPrice.findMaxGain(inputArray))