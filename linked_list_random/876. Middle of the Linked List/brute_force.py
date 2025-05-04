# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        countNodes = self.getLengthOfLinkedList(head)
        temp = head
        jumps = countNodes//2

        while jumps>0:
            temp = temp.next
            jumps-=1
        return temp

    def getLengthOfLinkedList(self, head):
        count = 0
        while not head is None:
            count+=1
            head = head.next
        return count