import logging

''' This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(strTree):
    ''' returns a tree given it's string representation '''

def serialize(root):
    ''' returns a string that represents a binary tree '''
    strTree = ''

    if(root.val):
        strTree += root.val
    
    strTree += '('
    if(root.left):        
        strTree += serialize(root.left)
    strTree += ')'

    strTree += '('
    if(root.right):
        strTree += serialize(root.right)
    strTree += ')'

    return strTree

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    node = Node('root', Node('left', Node('left.left')), Node('right'))

    logging.debug(serialize(node))
    
    #assert deserialize(serialize(node)).left.left.val == 'left.left'