from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead,_ =  self.helper(head)
        return reversedHead

    def helper(self,head:ListNode) -> tuple[ListNode, ListNode]:
        if head is None or head.next is None:
            return (head,head)
        
        nextHead, nextTail = self.helper(head.next)
        nextTail.next = head
        head.next = None
        nextTail = nextTail.next
        return (nextHead, nextTail)
    

'''
TC  -> O(n)
SC  -> O(n)
'''

        