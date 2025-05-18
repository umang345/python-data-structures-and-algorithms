from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderHelper(root,result)
        return result
    
    def preorderHelper(self, root:TreeNode, result:list):
        if root is None:
            return
        
        result.append(root.val)
        self.preorderHelper(root.left, result)
        self.preorderHelper(root.right, result)
        return
        