from os import *
from sys import *
from collections import *
from math import *

from typing import List


class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathInATree(root: TreeNode, x: int) -> List[int]:
    result = []
    helper(root, x, result)
    return result
    

def helper(root:TreeNode, x:int, result:list) -> bool:
    
    if root is None:
        return False
    
    result.append(root.data)
    if root.data == x:
        return True 
    
    currRes = helper(root.left,x,result)
    if currRes:
        return True 
    currRes = helper(root.right,x,result)
    if currRes:
        return True 
    
    result.pop()