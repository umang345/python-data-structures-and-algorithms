from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
def changeTree(root): 
    helper(root)

def helper(root) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data 
    
    leftChildVal = root.left.data if not root.left is None else 0
    rightChildVal = root.right.data if not root.right is None else 0
    currChildrenSum = leftChildVal + rightChildVal
    if currChildrenSum < root.data:
        if not root.left is None:
            root.left.data = root.data
        if not root.right is None:
            root.right.data = root.data
    
    root.data = helper(root.left) + helper(root.right)
    return root.data