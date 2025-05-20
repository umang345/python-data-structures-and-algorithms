# Definition for a binary tree node.
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        result = []
        if root is None:
            return result

        parentMap = dict()
        self.populateParentMap(root,parentMap)

        queue = deque()
        queue.append(target)
        visited = set()

        while k>0 and len(queue)>0:
            k-=1
            currLen = len(queue)
            while currLen > 0:
                currLen-=1
                node = queue.popleft()
                visited.add(node.val)
                if not node.left is None and not node.left.val in visited:
                    queue.append(node.left)
                if not node.right is None and not node.right.val in visited:
                    queue.append(node.right)
                if not parentMap.get(node.val) is None and not parentMap[node.val].val in visited:
                    queue.append(parentMap[node.val])
                
        while len(queue)>0:
            result.append(queue.popleft().val)
        
        return result
                
                

    def populateParentMap(self, root:TreeNode, parentMap:dict):
        if root is None:
            return 

        if not root.left is None:
            parentMap[root.left.val] = root
        
        if not root.right is None:
            parentMap[root.right.val] = root
        

        self.populateParentMap(root.left, parentMap)
        self.populateParentMap(root.right, parentMap)