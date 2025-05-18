from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    preorder, inorder, postorder = [],[],[]
    helper(root, preorder, inorder, postorder)
    return [inorder, preorder, postorder]

def helper(root, preorder, inorder, postorder):
    if root is None:
        return
    
    preorder.append(root.data)
    helper(root.left, preorder, inorder, postorder)
    inorder.append(root.data)
    helper(root.right, preorder, inorder, postorder)
    postorder.append(root.data)
