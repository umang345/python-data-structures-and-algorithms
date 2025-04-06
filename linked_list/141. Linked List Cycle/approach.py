# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        
        slow = head
        fast = head.next

        while (not slow is None) and (not fast is None) and (not fast.next is None):
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
        