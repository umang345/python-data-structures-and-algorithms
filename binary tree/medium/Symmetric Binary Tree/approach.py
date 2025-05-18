# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)
    
    def helper(self, node1:TreeNode, node2:TreeNode):

        if node1 is None and node2 is None:
            return True
        if (node1 is None and not node2 is None) or (not node1 is None and node2 is None) or (node1.val!=node2.val):
            return False

        return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)