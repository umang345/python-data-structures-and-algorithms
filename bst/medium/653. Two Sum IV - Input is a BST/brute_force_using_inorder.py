# Definition for a binary tree node.
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []
        
        if root is None:
            return False
        queue = deque()
        queue.append(root)
        while not queue[-1].left is None:
            queue.append(queue[-1].left)

        while len(queue)>0:
            currNode = queue.pop()
            inorder.append(currNode.val)
            if not currNode.right is None:
                queue.append(currNode.right)
                while not queue[-1].left is None:
                    queue.append(queue[-1].left)
        
        start,end = 0, len(inorder)-1

        while start<end:
            if inorder[start]+inorder[end] == k:
                return True
            elif inorder[start]+inorder[end] < k:
                start+=1
            else:
                end-=1
        
        return False
    
'''
TC -> O(n) + O(n)
SC -> O(n)
'''