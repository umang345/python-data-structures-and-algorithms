from collections import deque
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeIterator:
    def __init__(self, root:TreeNode, reverse=False):
        self.queue = deque()
        self.reverse = reverse
        if not root is None:
            self.queue.appendleft(root)
            self.__adjust()
    
    def nextNode(self):
        if self.hasNext():
            currNode = self.queue.popleft()
            if self.reverse:
                if not currNode.left is None:
                    self.queue.appendleft(currNode.left)
                    self.__adjust()
            else:
                if not currNode.right is None:
                    self.queue.appendleft(currNode.right)
                    self.__adjust()
            return currNode
        else:
            raise Exception("Empty Iterator")

    def peekNext(self):
        if self.hasNext():
            return self.queue[0]

    def hasNext(self):
        return len(self.queue)>0

    def __adjust(self):
        if self.reverse:
            self.__adjustReverse()
            return
        
        if len(self.queue)>0:
            while not self.queue[0].left is None:
                self.queue.appendleft(self.queue[0].left)
    
    def __adjustReverse(self):
        if len(self.queue)>0:
            while not self.queue[0].right is None:
                self.queue.appendleft(self.queue[0].right)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        frontIter = TreeIterator(root)
        endIter = TreeIterator(root, True)

        while frontIter.hasNext() and endIter.hasNext() and not frontIter.peekNext() is endIter.peekNext():
            frontVal = frontIter.peekNext().val 
            endVal = endIter.peekNext().val

            if frontVal+endVal == k:
                return True
            elif frontVal+endVal < k:
                frontIter.nextNode()
            else:
                endIter.nextNode()
        
        return False
    
'''
TC -> O(n)
SC -> O(height)
'''