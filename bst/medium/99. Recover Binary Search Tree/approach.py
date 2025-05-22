# Definition for a binary tree node.
from typing import *
from collections import *

'''
Similar to finding the inverted pair in sorted array
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        queue = deque()
        queue.appendleft(root)
        while not queue[0].left is None:
            queue.appendleft(queue[0].left)
        
        parent = None
        p1, p2 = None, None

        while len(queue)>0:
            node = queue.popleft()
            if not parent is None:
                if node.val < parent.val:
                    if p1 is None:
                        p1 = parent
                    p2 = node

            parent = node
            if not node.right is None:
                queue.appendleft(node.right)
                while not queue[0].left is None:
                    queue.appendleft(queue[0].left)

        p1.val, p2.val = p2.val, p1.val

'''
TC -> O(n)
SC  -> O(height) 

SC can be made O(1) using morris inorder
'''