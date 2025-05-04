# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head

        temp = head
        while not temp is None and not temp.next is None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                break

        return self.deleteDuplicates(head.next)

        