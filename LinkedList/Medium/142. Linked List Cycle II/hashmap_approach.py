from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not self.isCyclePresent(head):
            return None

        hashSet = set()
        temp = head

        while True:
            if temp in hashSet:
                return temp
            
            hashSet.add(temp)
            temp = temp.next

        

    def isCyclePresent(self, head:ListNode) -> bool:
        slow, fast = head, head

        while not fast is None and not fast.next is None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        return False
    
'''
TC   -> O(n) + O(n)
SC   -> O(n)
'''