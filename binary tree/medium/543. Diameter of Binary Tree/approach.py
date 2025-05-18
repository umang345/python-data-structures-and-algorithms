# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        _, diameter = self.helper(root)
        return diameter-1
        
    '''
    0 -> height of currNode
    1 -> maxDiameter
    '''
    def helper(self, root:TreeNode) -> tuple[int, int]:
        if root is None:
            return (0,0)
        
        leftCount, leftMax = self.helper(root.left)
        rightCount, rightMax = self.helper(root.right)

        currDia = 1+leftCount+rightCount
        currMaxHeight = 1+max(leftCount, rightCount)
        maxDia = max(currDia, max(leftMax, rightMax))

        return (currMaxHeight, maxDia)

    