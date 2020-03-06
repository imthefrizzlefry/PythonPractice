class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        myArray=[]
        if(root):
            if(root.left):
                myArray.extend(self.inorderTraversal(root.left))
            
            myArray.append(root.val)
            
            if(root.right):
                myArray.extend(self.inorderTraversal(root.right))
        return myArray

    def preorderTraversal(self, root):
        myArray=[]
        if(root):
            myArray.append(root.val)

            if(root.left):
                myArray.extend(self.preorderTraversal(root.left))
            
            if(root.right):
                myArray.extend(self.preorderTraversal(root.right))
        return myArray
    def postorderTraversal(self, root):
        myArray=[]
        if(root):
            if(root.left):
                myArray.extend(self.postorderTraversal(root.left))
            
            if(root.right):
                myArray.extend(self.postorderTraversal(root.right))

            myArray.append(root.val)
        return myArray