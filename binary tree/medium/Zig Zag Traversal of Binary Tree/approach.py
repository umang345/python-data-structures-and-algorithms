# Definition for a binary tree node.
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        if root is None:
            return result 

        queue = deque()
        queue.append(root)
        leftToRight = True

        while len(queue)>0:
            currLen = len(queue)
            currRow = []

            while currLen>0:
                currLen-=1
                node = queue.popleft()
                if not node.left is None:
                    queue.append(node.left)
                if not node.right is None:
                    queue.append(node.right)
                currRow.append(node.val)

            if not leftToRight:
                start, end = 0, len(currRow)-1
                while start<=end:
                    currRow[start], currRow[end] = currRow[end], currRow[start]
                    start+=1
                    end-=1

            result.append(currRow)
            leftToRight = not leftToRight

        return result            
            
                    

            
        