import unittest
from Medium_Problem03 import Node
from Medium_Problem03 import serialize


class SerializeDeserializeTreeTests(unittest.TestCase):
    def test_serializeDeserializeTree_Example(self):
        # Arrange
        inputNode = Node('root', Node('left', Node('left.left')), Node('right'))

        expectedResult = 'root(left(left.left()())())(right()())'

        # Act
        actualResult = serialize(inputNode)

        # Assert
        self.assertEqual(expectedResult, actualResult)