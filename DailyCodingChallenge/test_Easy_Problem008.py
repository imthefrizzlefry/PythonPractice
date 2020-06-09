import unittest
from Easy_Problem008 import count_unival_subtree
from Easy_Problem008 import Node

class CountUniversalSubtreeTests(unittest.TestCase):
    def test_findSumOfTests_Example(self):
        #arrange
        example_tree = Node(0)
        example_tree.left = Node(1)
        example_tree.right = Node(0)

        example_tree.right.left = Node(1)
        example_tree.right.right = Node(0)

        example_tree.right.left.left = Node(1)
        example_tree.right.left.right = Node(1)

        expected_result = 5

        #act
        actual_result = count_unival_subtree(example_tree)

        #assert
        self.assertEqual(expected_result, actual_result)