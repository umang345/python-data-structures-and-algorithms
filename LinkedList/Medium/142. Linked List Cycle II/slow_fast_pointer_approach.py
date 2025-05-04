from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        '''
        1 - 2 - 4  -  8 - 7 - 12  - 44 - 9 - 1
                |                            |
                -  -  - -   -  -  -    -   - -

        '''
        # slow, fast = head, head
        isCycle, meetInMiddleNode = self.isCyclePresent(head)
        if not isCycle:
            return None
        
        p1, p2 = head, meetInMiddleNode

        while not p1 is p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        
    def isCyclePresent(self, head:ListNode) -> tuple[bool, ListNode]:
        slow, fast = head, head

        while not fast is None and not fast.next is None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return (True, slow)
        
        return (False, None)