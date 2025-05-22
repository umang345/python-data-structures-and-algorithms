# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = [0]
        return self.helper(root,pos, k).val

    def helper(self, root:TreeNode, pos:list, k:int) -> TreeNode:
        if root is None:
            return None
        
        if not root.left is None:
            leftRes = self.helper(root.left, pos, k)
            if not leftRes is None:
                return leftRes
        
        pos[0]+=1
        if pos[0]==k:
            return root
        
        return self.helper(root.right,pos,k)