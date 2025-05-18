# Definition for a binary tree node.

from collections import deque
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)

        while len(queue)>0:
            currRow = []
            currLen = len(queue)
            while currLen>0:
                currNode = queue.popleft()
                if not currNode.left is None:
                    queue.append(currNode.left)
                if not currNode.right is None:
                    queue.append(currNode.right)
                currRow.append(currNode.val)
                currLen-=1
            result.append(currRow)
        
        return result
            
