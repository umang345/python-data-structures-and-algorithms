# Definition for a binary tree node.

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if root is None:
            return result
        
        stack = deque()
        stack.append(root)

        while len(stack)>0:
            if stack[-1] is None:
                stack.pop()
                poppedNode = stack.pop()
                result.append(poppedNode.val)
            else:
                poppedNode = stack.pop()
                stack.append(poppedNode)
                stack.append(None)
                if not poppedNode.right is None:
                    stack.append(poppedNode.right)
                if not poppedNode.left is None:
                    stack.append(poppedNode.left)
        
        return result