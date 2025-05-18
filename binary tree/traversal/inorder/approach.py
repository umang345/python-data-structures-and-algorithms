from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderHelper(root, result)
        return result

    def inorderHelper(self, root:TreeNode, result:list):
        if root is None:
            return
        
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)
        return 