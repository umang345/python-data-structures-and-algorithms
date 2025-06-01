# Definition for singly-linked list.
import heapq
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq = []
        for (index,head) in enumerate(lists):
            if not head is None:
                heapq.heappush(pq, (head.val,index, head)) 
        
        mergedListHead, tail = None, None

        while len(pq)>0:
            _,index, minNode = heapq.heappop(pq)
            if tail is None:
                mergedListHead, tail = minNode, minNode
            else:
                tail.next = minNode
                tail = tail.next
            
            if not minNode.next is None:
                heapq.heappush(pq, (minNode.next.val,index, minNode.next))
            
            tail.next = None
        
        return mergedListHead
            
