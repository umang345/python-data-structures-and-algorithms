from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        if not root is None:
            self.queue.appendleft(root)
        self.__adjust()        

    def next(self) -> int:
        if self.hasNext():
            currNode = self.queue.popleft()
            if not currNode.right is None:
                self.queue.appendleft(currNode.right)
                self.__adjust()
            return currNode.val
        
        raise Exception("No more element exist")

    def hasNext(self) -> bool:
        return len(self.queue)>0

    def __adjust(self):
        if len(self.queue) > 0:
            while not self.queue[0].left is None:
                self.queue.appendleft(self.queue[0].left)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()