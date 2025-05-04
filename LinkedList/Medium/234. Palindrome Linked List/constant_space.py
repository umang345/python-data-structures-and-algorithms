from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        '''
        [1,2]
        '''
        lenOfList = 0
        temp = head

        while not temp is None:
            temp = temp.next
            lenOfList+=1

        midIndex = (lenOfList+1)//2
        jumps = midIndex
        secondList = head
        while jumps>0:
            secondList = secondList.next
            jumps-=1

        secondList = self.reverseList(secondList)
        temp = head
        while not secondList is None:
            if temp.val != secondList.val:
                return False
            secondList = secondList.next
            temp = temp.next

        return True

    def reverseList(self, head:ListNode) -> ListNode:
        reversedHead = None
        currNode = head

        while not currNode is None:
            temp = currNode.next 
            currNode.next = reversedHead
            reversedHead = currNode
            currNode = temp
        
        return reversedHead


        