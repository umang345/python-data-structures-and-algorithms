from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodesLeft = k
        currHead, tail = head,head
        reversedHead, reversedTail = None, None

        while not tail is None:
            if nodesLeft == 1:
                nextNode = tail.next
                tail.next = None
                currRevHead = self.reverseList(currHead)
                if reversedTail is None:
                    reversedTail = currHead
                    reversedHead = currRevHead
                else:
                    reversedTail.next = currRevHead
                    reversedTail = currHead
                currHead = nextNode
                tail = nextNode
                nodesLeft = k
            else:
                nodesLeft-=1
                tail = tail.next
        
        if reversedTail is None:
            return currHead
        
        reversedTail.next = currHead
        return reversedHead


    def reverseList(Self, head:ListNode) -> ListNode:
        currHead = None
        temp = head

        while not temp is None:
            nextNode = temp.next
            temp.next = currHead
            currHead = temp
            temp = nextNode
        
        return currHead