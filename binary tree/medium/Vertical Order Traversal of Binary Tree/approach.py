# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        hashMap = dict()
        queue = deque()
        queue.append((0, root))

        while len(queue)>0:
            currLen = len(queue)
            currRow = []
            while currLen>0:
                col,node = queue.popleft()
                currLen-=1
                if not node.left is None:
                    queue.append((col-1, node.left))
                if not node.right is None:
                    queue.append((col+1,node.right))
                
                currRow.append((col,node))
            
            currRow.sort(key=lambda x : (x[0], x[1].val))
            for tup in currRow:
                col, node = tup
                if hashMap.get(col) is None:
                    hashMap[col] = []
                hashMap[col].append(node.val)
        result = []
        for key in sorted(hashMap.keys()):
            result.append(hashMap[key])
        
        return result

