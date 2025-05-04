from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        tail = None 
        temp1, temp2 = l1, l2
        carry = 0

        while not temp1 is None or not temp2 is None or carry==1:

            currSum = carry
            carry = 0

            if not temp1 is None:
                currSum+=temp1.val
                temp1 = temp1.next
            if not temp2 is None:
                currSum+=temp2.val
                temp2 = temp2.next

            if currSum > 9:
                carry = 1 
                currSum = currSum%10
            
            newNode = ListNode(currSum)
            if tail is None:
                head, tail = newNode,newNode
            else:
                tail.next = newNode
                tail = tail.next
        
        return head