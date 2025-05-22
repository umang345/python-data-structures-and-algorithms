from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = list(sorted(preorder))
        return self.helper(inorder, preorder, 0, len(preorder)-1, 0, len(preorder)-1)

    def helper(self, inorder, preorder, preLeft, preRight, inLeft, inRight):
        if inLeft>inRight:
            return None

        currNodeValue = preorder[preLeft]
        currPreCount = 0
        inIndex = inLeft
        while inorder[inIndex]!=currNodeValue:
            currPreCount+=1
            inIndex+=1
        
        node = TreeNode(currNodeValue)
        node.left = self.helper(inorder, preorder, preLeft+1, preLeft+currPreCount,inLeft, inIndex-1)
        node.right = self.helper(inorder, preorder, preLeft+currPreCount+1,preRight, inIndex+1, inRight)
        return node
    

'''
Time complexity -> O(nlogn)+O(n)
SC -> O(n) for inorder array
'''