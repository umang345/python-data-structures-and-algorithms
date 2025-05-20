# Definition for a binary tree node.
from typing import *
from math import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        if root is None:
            return 0
    
        maxWidth = -inf
        
        queue.append((0, root))
        while len(queue)>0:
            leftLimit, rightLimit = inf, -inf
            currLen = len(queue)
            while currLen>0:
                currLen-=1
                col, node = queue.popleft()
                if not node.left is None:
                    queue.append((col-1, node.left))
                if not node.right is None:
                    queue.append((col+1, node.right))
                
                leftLimit = min(leftLimit, col)
                rightLimit = max(rightLimit, col)
            
            currWidth = abs(rightLimit - leftLimit)
            maxWidth = max(maxWidth, currWidth)
        
        return abs(maxWidth)