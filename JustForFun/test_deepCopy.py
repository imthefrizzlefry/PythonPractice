import unittest
from deepCopy import Node

class deepCopyTests(unittest.TestCase):
    
    def test_createNodeWithExpectedValue(self):
        expectedValue = 1.0

        inputNode = Node(expectedValue)

        self.assertEqual(expectedValue, inputNode.value)

    def test_createNodeWithExpectedChildren(self):
        expectedChildren = [1,2,3,4,5]

        inputNode = Node(1, expectedChildren)

        self.assertEqual(expectedChildren, inputNode.children)

    def test_deepCopySimpleNote(self):
        inputA = Node(1.0, [])
        inputB = inputA.deep_copy()

        inputA.value = 2.0

        self.assertEqual(1.0, inputB.value)
        self.assertEqual(2.0, inputA.value)
    def test_deepCopypreservesListContents(self):
        inputA = Node(1.0, [Node(2.0)])
        inputB = inputA.deep_copy()

        inputA.children[0].value = 3.0

        self.assertEqual(2.0, inputB.children[0].value)
        self.assertEqual(3.0, inputA.children[0].value)
    def test_deepCopyInterDependancyPreservesLinks(self):
        inputA = Node(1.0)
        inputB = Node(2.0,[inputA])
        inputA.children.append(inputB)

        inputC = inputA.deep_copy()
        inputC.value = 3.0
        inputC.children[0].value = 4.0

        # inputA and inputB have an interdependancy
        self.assertIs(inputA, inputB.children[0])
        self.assertIs(inputB, inputA.children[0])

        # inputC is a new object, as it's child is a clone of inputB
        self.assertIsNot(inputA, inputC)
        self.assertIsNot(inputB, inputC.children[0])
        self.assertIsNot(inputA.value, inputC.value)
        self.assertIsNot(inputB.value, inputC.children[0].value)

        # validate the values within inputA & B were copied over
        self.assertEqual(3.0, inputC.value)
        self.assertEqual(4.0, inputC.children[0].value)
        self.assertNotEqual(inputA.value, inputC.value)


        # it is sufficient to ensure the grandchild is the same object.
        self.assertIs(inputC, inputC.children[0].children[0]) # inputC is it's own grandchild
        self.assertIs(inputC.children[0], inputC.children[0].children[0].children[0]) # the child of inputC is it's own grandchild
