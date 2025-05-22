from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.helper(inorder, postorder, 0, len(inorder)-1, 0, len(inorder)-1)
    
    def helper(self, inorder:list, postorder:list, inLeft:int, inRight:int, postLeft:int, postRight:int):
        '''
        inorder = [9,3,15,20,7], 
        postorder = [9,15,7,20,3]
        '''
        if inLeft>inRight:
            return None 
        
        currNodeVal = postorder[postRight]
        currNode = TreeNode(currNodeVal)

        countPostOrder = 0
        inIndex = inLeft

        while inorder[inIndex] != currNodeVal:
            inIndex+=1
            countPostOrder+=1
        
        currNode.left = self.helper(inorder, postorder, inLeft, inIndex-1, postLeft, postLeft+countPostOrder-1)
        currNode.right = self.helper(inorder, postorder, inIndex+1, inRight, postLeft+countPostOrder, postRight-1)
        return currNode