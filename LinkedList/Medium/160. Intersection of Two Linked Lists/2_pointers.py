from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA is None or headB is None:
            return None

        a,b = headA, headB

        while not a is b:
            a = a.next
            b = b.next

            if a is None and not b is None:
                a = headB
            if b is None and not a is None:
                b = headA
            
            if a is None and b is None:
                return None
        
        return a