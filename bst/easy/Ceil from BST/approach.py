from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    
    curr = root
    res = inf
    found = False
    while not curr is None:
        if curr.data >= x:
            found = True
            res = min(res, curr.data)
            curr = curr.left 
        else:
            curr = curr.right 

    if not found:
        return -1    
    return res