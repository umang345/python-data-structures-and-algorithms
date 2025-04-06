# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        converted_number,_ = self.__getDecimalValueHelper(head)
        return converted_number

    def __getDecimalValueHelper(self, head:ListNode) -> (int, int):
        if head is None:
            return (0,-1)
        
        number_so_far, weight = self.__getDecimalValueHelper(head.next)
        weight+=1
        number_so_far += (head.val * (2**weight))
        return (number_so_far, weight) 
        