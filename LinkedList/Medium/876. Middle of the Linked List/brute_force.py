from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        '''
        [1,2,3,4,5] mid = 5/2 -> 2   jumps = 2
        [1,2,3,4,5,6] mid = 6/2 -> 3   jumps = 3
        '''

        listLen = 0
        temp = head
        while not temp is None:
            listLen+=1
            temp = temp.next

        mid = listLen//2
        jumps = mid
        temp = head
        while jumps>0:
            temp = temp.next
            jumps-=1

'''
TC   -> O(n) + O(n/2)
SC   -> O(1)
'''

