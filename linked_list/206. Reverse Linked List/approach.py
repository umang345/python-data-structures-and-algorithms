# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        reverse_head = None
        while not head is None:
            if reverse_head is None:
                reverse_head = head
                head = head.next
                reverse_head.next = None
            else:
                temp = reverse_head
                reverse_head = head
                head = head.next
                reverse_head.next = temp
        return reverse_head
        