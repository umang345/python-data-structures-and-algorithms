from typing import *
from math import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -inf, inf)

    def helper(self, root:TreeNode, leftLimit, rightLimit) -> bool:
        if root is None:
            return True
        
        if root.val > leftLimit and root.val < rightLimit:
            return self.helper(root.left, leftLimit, root.val) and self.helper(root.right, root.val, rightLimit)
        else:
            return False