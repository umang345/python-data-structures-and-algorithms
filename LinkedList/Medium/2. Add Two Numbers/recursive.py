from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(l1, l2)
        
    def helper(self, list1:ListNode, list2:ListNode, carry=0) -> ListNode:
        if list1 is None and list2 is None and carry==0:
            return None
        
        currSum = carry
        carry = 0
        nextList1Node, nextList2Node = None, None
        if not list1 is None:
            currSum+=list1.val
            nextList1Node = list1.next
        if not list2 is None:
            currSum+=list2.val
            nextList2Node = list2.next
        
        if currSum > 9:
            carry = 1 
            currSum = currSum%10
        
        newNode = ListNode(currSum)
        newNode.next = self.helper(nextList1Node, nextList2Node, carry)
        return newNode