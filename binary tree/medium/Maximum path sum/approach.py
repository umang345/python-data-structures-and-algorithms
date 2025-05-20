# Definition for a binary tree node.
from typing import *
from math import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        _, result = self.helper(root)
        return result 

    def helper(self, root:TreeNode) -> Tuple[int, int]:
        if root is None:
            return (0, 0)
        
        leftSum, leftMax = self.helper(root.left)
        rightSum, rightMax = self.helper(root.right)

        sumIncludingCurrentNode = root.val + leftSum + rightSum
        currMax = -inf
        currMax = max(currMax, root.val + leftSum + rightSum)
        currMax = max(currMax, root.val + leftSum)
        currMax = max(currMax, root.val + rightSum)
        currMax = max(currMax, root.val)

        currSum = root.val + max(leftSum, rightSum)

        return (currSum, currMax)