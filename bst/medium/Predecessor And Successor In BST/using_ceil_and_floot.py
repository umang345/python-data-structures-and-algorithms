from os import *
from sys import *
from collections import *
from math import *

'''
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
      
'''

def floor(root, key):
    curr = root
    result = inf 
    found = False
    while not curr is None:
        if curr.data <= key:
            curr = curr.right
        else:
            result = min(result, curr.data)
            found = True 
            curr = curr.left 
    
    if not found:
        return -1
    
    return result


def ceil(root, key):
    curr = root 
    result = -inf
    found = False 

    while not curr is None:
        if curr.data >=key:
            curr = curr.left 
        else:
            result = max(result, curr.data)
            curr = curr.right
            found = True 
    
    if not found:
        return -1
    return result 

def predecessorSuccessor(root, key):
    return [ceil(root, key), floor(root, key)]

