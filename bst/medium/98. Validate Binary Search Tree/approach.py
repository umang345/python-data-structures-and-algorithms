from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result,_,_ = self.helper(root)
        return result

    def helper(self, root:TreeNode) -> Tuple[bool,int, int]:
        if root is None:
            return (True,-inf, inf)
        
        leftRes, leftMax, leftMin = self.helper(root.left)
        rightRes, rightMax ,rightMin = self.helper(root.right)

        currRes = leftRes and rightRes and (root.val > leftMax and root.val < rightMin)

        currMin = min(root.val, min(leftMin, rightMin))
        currMax = max(root.val, max(leftMax, rightMax))

        return (currRes, currMax, currMin) 