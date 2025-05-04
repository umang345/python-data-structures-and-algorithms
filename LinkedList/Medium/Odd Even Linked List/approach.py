from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        oddHead, oddTail = head, head
        evenHead,evenTail = head.next, head.next
        currNode = evenHead.next

        oddHead.next = None
        evenHead.next = None

        while not currNode is None:
            oddTail.next = currNode
            oddTail = oddTail.next
            currNode = currNode.next
            oddTail.next = None
            if not currNode is None:
                evenTail.next = currNode
                evenTail = evenTail.next
                currNode = currNode.next
                evenTail.next = None
        
        oddTail.next = evenHead
        return oddHead