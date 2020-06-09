import unittest
from Medium_Problem05 import car
from Medium_Problem05 import cdr
from Medium_Problem05 import cons

class pairOperationsTests(unittest.TestCase):
    def test_car_Example(self):
        # Arrange
        a = 3
        b = 4
        expected = 3

        # Act
        actual = car(cons(a,b))

        # Assert
        self.assertEqual(expected, actual)

    def test_cdr_Example(self):
        # Arrange
        a = 3
        b = 4
        expected = 4

        # Act
        actual = cdr(cons(a,b))

        # Assert
        self.assertEqual(expected, actual)