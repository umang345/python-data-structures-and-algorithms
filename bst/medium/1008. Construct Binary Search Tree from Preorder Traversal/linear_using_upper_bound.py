from typing import *
from math import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, [0], inf)

    def helper(self,preorder:list, pos:list, upperBound:int) -> TreeNode:
        
        if pos[0] >= len(preorder) or preorder[pos[0]]>upperBound:
            return None

        node = TreeNode(preorder[pos[0]])
        pos[0]+=1

        node.left = self.helper(preorder, pos, node.val)
        node.right = self.helper(preorder, pos, upperBound)

        return node