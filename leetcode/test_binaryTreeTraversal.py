import unittest
from binaryTreeTraversal import TreeNode
from binaryTreeTraversal import Solution

class treeTraversalTests(unittest.TestCase):

    def test_traverseTree_gracefullyHandlesNone_insSupportedOrders(self):
        mySolution = Solution()

        self.assertEqual([], mySolution.inorderTraversal(root=None))
        self.assertEqual([], mySolution.preorderTraversal(root=None))
        self.assertEqual([], mySolution.postorderTraversal(root=None))

    def test_traverseTree_isPossible_insSupportedOrders(self):
        testTree = self.TreeBuildingHelper()

        mySolution = Solution()

        self.assertEqual([1,2,3,4,5,6,7,8], mySolution.inorderTraversal(root=testTree))
        self.assertEqual([5,3,2,1,4,7,6,8], mySolution.preorderTraversal(root=testTree))
        self.assertEqual([1,2,4,3,6,8,7,5], mySolution.postorderTraversal(root=testTree))

    def TreeBuildingHelper(self):
        '''  Return a tree with the following structure:
                 5
              3     7
             2 4   6 8
            1
        '''
        testTree = TreeNode(5)
        testTree.left = TreeNode(3)
        testTree.left.left = TreeNode(2)
        testTree.left.left.left = TreeNode(1)
        testTree.left.right = TreeNode(4)
        testTree.right = TreeNode(7) 
        testTree.right.left = TreeNode(6)
        testTree.right.right = TreeNode(8)

        return testTree

if __name__ == '__main__':
    unittest.main()