from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        O(n) time and O(1) space
        '''
        curr = root
        result = []
        while not curr is None:
            if not curr.left is None:
                prev = curr.left
                while not prev.right is None and not prev.right is curr:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    result.append(curr.val)
                    curr = curr.right
            else:
                result.append(curr.val)
                curr = curr.right
        
        return result