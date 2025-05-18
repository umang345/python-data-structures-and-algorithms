# Definition for a binary tree node.
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if root is None:
            return result

        stack, resultStack = deque(), deque()

        stack.append(root)

        while len(stack) > 0:
            poppedNode = stack.pop()
            resultStack.append(poppedNode)
            if not poppedNode.left is None:
                stack.append(poppedNode.left)
            if not poppedNode.right is None:
                stack.append(poppedNode.right)
        
        while len(resultStack)>0:
            result.append(resultStack.pop().val)
        
        return result

        