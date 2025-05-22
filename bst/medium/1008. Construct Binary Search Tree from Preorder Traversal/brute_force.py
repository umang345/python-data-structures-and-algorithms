from typing import *

'''
Insert Node in BST according to PreOrder O(nlogn) -> O(n*n) for skewed
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        [8,5,1,7,10,12]
        '''
        head = None
        for num in preorder:
            head = self.insertInBst(head, num)
        return head 

    
    def insertInBst(self, root:TreeNode, num:int) -> TreeNode:
        if root is None:
            return TreeNode(num)
        
        if root.val > num:
            root.left = self.insertInBst(root.left, num)
        else:
            root.right = self.insertInBst(root.right, num)
        
        return root