from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Tracker:
    def __init__(self, head:ListNode):
        self.start = head
        self.end = head

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tracker = Tracker(head)
        return self.helper(tracker)

    def helper(self, tracker:Tracker) -> bool:
        if tracker.end is None:
            return True
        
        currEndNode = tracker.end
        tracker.end = tracker.end.next
        nextRes = self.helper(tracker)

        currRes = tracker.start.val == currEndNode.val
        tracker.start = tracker.start.next

        return currRes and nextRes
    

'''
TC   -> O(n)
SC   -> O(n)
'''