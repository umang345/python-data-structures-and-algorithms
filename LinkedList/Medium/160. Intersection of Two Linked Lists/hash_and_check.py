from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None:
            return headaA
        if headB is None:
            return headB

        hashSet = set()
        temp = headA
        while not temp is None:
            hashSet.add(temp)
            temp = temp.next
        
        temp = headB
        while not temp is None:
            if temp in hashSet:
                return temp
            temp = temp.next
        return None

