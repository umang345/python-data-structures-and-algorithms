from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currHead = None
        temp = head

        while not temp is None:
            currNode = temp.next 
            temp.next = currHead
            currHead = temp
            temp = currNode
        
        return currHead