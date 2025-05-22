from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root

        leftNode = None
        if not root.left is None:
            leftSubTreeNode = self.flatten(root.left)
            leftNode = leftSubTreeNode
            while not leftNode.right is None:
                leftNode = leftNode.right
        
        rightNode = root.right
        if not leftNode is None:
            root.right = leftSubTreeNode
            leftNode.right = rightNode
            root.left = None 
            leftNode.right = self.flatten(rightNode)
        else:
            root.right = self.flatten(root.right)
        return root