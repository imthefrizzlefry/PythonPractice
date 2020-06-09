class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
# def levelOrder(root):
#     #Write your code here
#     h = height(root) 
#     for i in range(h): 
#         printGivenLevel(root, i) 
  
  
# # Print nodes at a given level 
# def printGivenLevel(root , level): 
#     if root is None: 
#         return
#     if level == 0: 
#         print(root.info, end=" "), 
#     else: 
#         printGivenLevel(root.left , level-1) 
#         printGivenLevel(root.right , level-1) 

# def height(node): 
#     if node is None: 
#         return 0 
#     else : 
#         return max(height(node.left)+1, height(node.right)+1)


def levelOrder(root):
    queue = None if root is None else [root]

    while queue:
        print(queue[0].info, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

print("Input: None")
print("Output:")
levelOrder(None)


myNode = Node(5)

print("Input: 5")
print("Output:")
levelOrder(myNode)

myNode.right = Node(6)
print("Input: \n  5\n / \\\n-   6")
print("Output:")
levelOrder(myNode)

myNode.right.left = Node(9)
print("Input: \n  5\n / \\\n-   6\n   /\n  9")
print("Output:")
levelOrder(myNode)

myNode.right.right = Node(12)
print("Input: \n  5\n / \\\n-   6\n   / \\\n  9   12")
print("Output:")
levelOrder(myNode)

myNode.right.left.right = Node(4)
print("Input: \n  5\n / \\\n-   6\n   / \\\n  9   12\n   \\\n    4")
print("Output:")
levelOrder(myNode)