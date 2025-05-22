
from typing import *

'''
Time complexity -> O(logn) * O(logn)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)

        if leftHeight == rightHeight:
            return (2**leftHeight)-1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def getLeftHeight(self, root:TreeNode) -> int:
        if root is None:
            return 0
        
        return 1+self.getLeftHeight(root.left)

    def getRightHeight(self, root:TreeNode) -> int:
        if root is None:
            return 0
        
        return 1+self.getRightHeight(root.right)