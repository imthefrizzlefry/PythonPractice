import logging

''' This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtree(root):
    count = 0
    if root.left and root.right:
        count = count + 1 if root.left.val == root.right.val else count
    else:
        count = count + 1 if root.left == root.right else count

    count = count + count_unival_subtree(root.left) if root.left else count
    count = count + count_unival_subtree(root.right) if root.right else count
    return count

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    example_tree = Node(0)
    example_tree.left = Node(1)
    example_tree.right = Node(0)

    example_tree.right.left = Node(1)
    example_tree.right.right = Node(0)

    example_tree.right.left.left = Node(1)
    example_tree.right.left.right = Node(1)

    result = count_unival_subtree(example_tree)

    logging.debug(result)
