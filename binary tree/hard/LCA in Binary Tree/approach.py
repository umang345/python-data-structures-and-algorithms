# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca,_,_ = self.helper(root,p,q)
        return lca

    def helper(self, root,p,r) -> Tuple['TreeNode',bool, bool]:
        if root is None:
            return (None,False,False)
        
        leftNodeRes,pFoundLeft,rFoundLeft = self.helper(root.left,p,r)
        rightNodeRes, pFoundRight, rFoundRight = self.helper(root.right,p,r)

        if not leftNodeRes is None:
            return (leftNodeRes,True, True)
        if not rightNodeRes is None:
            return (rightNodeRes,True, True)
        
        pFound = pFoundLeft or pFoundRight or p.val == root.val
        rFound = rFoundLeft or rFoundRight or r.val == root.val

        if pFound and rFound:
            return (root,pFound, rFound)
        
        return (None,pFound, rFound)
        

        