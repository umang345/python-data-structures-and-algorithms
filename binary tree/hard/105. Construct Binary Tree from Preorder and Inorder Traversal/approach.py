from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder -> [3,9,20,15,7]
        inorder -> [9,3,15,20,7]

        '''
        return self.helper(preorder, inorder, 0, len(preorder)-1, 0, len(preorder)-1)
    
    def helper(self, preorder:list, inorder:list, preLeft:int, preRight:int, inLeft:int, inRight:int):
        if preLeft>preRight:
            return None
        
        currNodeVal = preorder[preLeft]
        currNode = TreeNode(currNodeVal)

        countForPreOrderIndex = 0
        inIndex = inLeft

        while inorder[inIndex]!=currNodeVal:
            inIndex+=1
            countForPreOrderIndex+=1

        currNode.left = self.helper(preorder, inorder, preLeft+1, preLeft+countForPreOrderIndex, inLeft, inIndex-1)
        currNode.right = self.helper(preorder, inorder, preLeft+countForPreOrderIndex+1, preRight, inIndex+1, inRight)
        return currNode
        