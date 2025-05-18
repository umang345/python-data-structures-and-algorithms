from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)

        while len(queue)>0:
            result.append(queue[-1].val)
            currLen = len(queue)
            while currLen > 0:
                currLen-=1
                node = queue.popleft()
                if not node.left is None:
                    queue.append(node.left)
                if not node.right is None:
                    queue.append(node.right)
        
        return result