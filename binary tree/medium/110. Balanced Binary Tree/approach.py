# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result,_  = self.helper(root)
        return result

    def helper(self, root:TreeNode) -> tuple[bool,int]:
        if root is None:
            return (True,0)
        
        leftRes, leftHeight = self.helper(root.left)
        rightRes, rightHeight = self.helper(root.right)

        result = leftRes and rightRes and (abs(leftHeight-rightHeight)<=1)
        currHeight = 1+max(leftHeight, rightHeight)

        return (result, currHeight)
        