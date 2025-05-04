from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        front, follow = head, head

        jumps = n
        while jumps > 0:
            front = front.next
            jumps-=1
        
        if front is None:
            return head.next
        
        while not front.next is None:
            front = front.next
            follow = follow.next
        
        follow.next = follow.next.next
        return head