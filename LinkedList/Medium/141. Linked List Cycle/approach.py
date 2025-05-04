from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head

        while not fast is None and not fast.next is None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        
        return False