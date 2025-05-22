from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        if root.val == key:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                nextGreater = root.right
                while not nextGreater.left is None:
                    nextGreater = nextGreater.left
                
                root.val, nextGreater.val = nextGreater.val, root.val
                root.right = self.deleteNode(root.right, key)
                
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right,key)
        
        return root