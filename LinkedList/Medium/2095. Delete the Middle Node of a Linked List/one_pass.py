from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        [1,3,4,7,1,2,6]
        [1,2,3,4,5,6,7,8,9,10,11,12]
        '''

        slow,fast = head, head

        while not fast is None and not fast.next is None and not fast.next.next is None and not fast.next.next.next is None:
            slow = slow.next
            fast = fast.next.next

        if slow is None or slow.next is None:
            return head.next

        slow.next = slow.next.next
        return head