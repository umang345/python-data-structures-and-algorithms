# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftCount = self.maxDepth(root.left)
        rightCount = self.maxDepth(root.right)
        return 1+max(leftCount,rightCount)