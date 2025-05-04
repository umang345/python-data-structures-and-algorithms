from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        array = []
        temp = head
        while not temp is None:
            array.append((temp.val,temp))
            temp = temp.next
        
        array.sort(key=lambda x : x[0])

        sortedHead,sortedTail = array[0][1], array[0][1]
        sortedHead.next = None

        for index in range(1,len(array)):
            sortedTail.next = array[index][1]
            sortedTail = sortedTail.next
            sortedTail.next = None
        
        return sortedHead

        