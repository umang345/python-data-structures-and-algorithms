# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersHelper(l1,l2,0)
        
    
    def addTwoNumbersHelper(self, list1: Optional[ListNode], list2: Optional[ListNode], carry) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            if carry != 0:
                return ListNode(carry)
            else:
                return None
        
        currentNode = ListNode(-1)

        if list1 is None and not list2 is None:
            current_sum = list2.val + carry
            if current_sum>9:
                carry = 1
                current_sum-=10
            else:
                carry = 0
            currentNode.val = current_sum
            currentNode.next = self.addTwoNumbersHelper(list1, list2.next, carry)
        
        elif list2 is None and not list1 is None:
            current_sum = list1.val + carry
            if current_sum>9:
                carry = 1
                current_sum-=10
            else:
                carry = 0
            currentNode.val = current_sum
            currentNode.next = self.addTwoNumbersHelper(list1.next, list2, carry)
        else:
            current_sum = list1.val + list2.val + carry
            if current_sum>9:
                carry = 1
                current_sum-=10
            else:
                carry = 0
            currentNode.val = current_sum
            currentNode.next = self.addTwoNumbersHelper(list1.next, list2.next, carry)

        return currentNode
    
        