from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLengthOfList(head)

        if n == length:
            return head.next

        jumps = (length - n - 1)
        temp = head
        while jumps > 0:
            temp = temp.next
            jumps-=1

        temp.next = temp.next.next
        return head         

    def getLengthOfList(self, head:ListNode) -> int:
        count = 0
        temp = head
        while not temp is None:
            temp = temp.next
            count+=1
        
        return count