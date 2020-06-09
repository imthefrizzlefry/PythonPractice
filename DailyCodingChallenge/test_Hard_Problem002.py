import unittest
from Hard_Problem02 import arrayOfProducts

class arrayOfProductsTests(unittest.TestCase):
    def test_arrayOfProducts_Example(self):
        # Arrange
        inputArray = [1,2,3,4,5]
        expectedResult = [120,60,40,30,24]

        # Act
        actualResult = arrayOfProducts(inputArray)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def test_arrayOfProducts_EmptyArray(self):
        # Arrange
        inputArray = []
        expectedResult = []

        # Act
        actualResult = arrayOfProducts(inputArray)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def test_arrayOfProducts_negativeNumber(self):
        # Arrange
        inputArray = [1,-2,3,4,5]
        expectedResult = [-120,60,-40,-30,-24]

        # Act
        actualResult = arrayOfProducts(inputArray)

        # Assert
        self.assertEqual(expectedResult, actualResult)

    def test_arrayOfProducts_SingleElement(self):
        # Arrange
        inputArray = [5]
        expectedResult = [1]

        # Act
        actualResult = arrayOfProducts(inputArray)

        # Assert
        self.assertEqual(expectedResult, actualResult)