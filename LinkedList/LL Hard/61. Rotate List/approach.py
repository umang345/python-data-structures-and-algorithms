from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        count = 0
        temp = head

        while not temp is None:
            count+=1
            temp = temp.next
        
        rotation = count - (k%count)

        currHead, currTail = head, head
        while not currTail.next is None:
            currTail = currTail.next

        
        while rotation > 0:
            rotation-=1
            nextNodeToHead = currHead.next
            currHead.next = None
            currTail.next = currHead
            currTail = currHead
            if nextNodeToHead is None:
                currHead = currTail
            else:
                currHead = nextNodeToHead

        return currHead
