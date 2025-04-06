# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Tracker:
    def __init__(self, head):
        self.head1 = head
        self.head2 = head

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.isPalindromeHelper(Tracker(head))

    def isPalindromeHelper(self, tracker:Tracker) -> bool:
        if tracker.head1 is None:
            return True
        
        current_val = tracker.head1.val
        tracker.head1 = tracker.head1.next
        next_result = self.isPalindromeHelper(tracker)

        current_result = next_result and (current_val == tracker.head2.val)
        tracker.head2 = tracker.head2.next
        return current_result