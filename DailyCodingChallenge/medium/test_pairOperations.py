import unittest
import pairOperations

class pairOperationsTests(unittest.TestCase):
    def test_car_Example(self):
        # Arrange
        a = 3
        b = 4
        expected = 3

        # Act
        actual = pairOperations.car(pairOperations.cons(a,b))

        # Assert
        self.assertEqual(expected, actual)

    def test_cdr_Example(self):
        # Arrange
        a = 3
        b = 4
        expected = 4

        # Act
        actual = pairOperations.cdr(pairOperations.cons(a,b))

        # Assert
        self.assertEqual(expected, actual)