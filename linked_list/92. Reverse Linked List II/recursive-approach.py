# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Tracker:
    def __init__(self):
        self.initialListHead = None
        self.initialListTail = None
        self.reversdHead = None
        self.reversedTail = None
        self.endList = None

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tracker = Tracker()
        self.reverseBetweenHelper(head,1,left, right,tracker)

        updatedHead = None
        
        if not tracker.endList is None:
            tracker.reversedTail.next = tracker.endList
        
        if not tracker.initialListTail is None:
            tracker.initialListTail.next = tracker.reversdHead
            return tracker.initialListHead

        else:
            return tracker.reversdHead
        

    def reverseBetweenHelper(self,head:ListNode, currentIndex,left, right, tracker = Tracker()):
        if head is None:
            return

        if currentIndex > right:
            tracker.endList = head
            return

        elif currentIndex < left:
            nextNode = head.next
            if tracker.initialListTail is None:
                tracker.initialListHead, tracker.initialListTail = head,head
            else:
                tracker.initialListTail.next = head
                tracker.initialListTail = tracker.initialListTail.next

            tracker.initialListTail.next = None
            self.reverseBetweenHelper(nextNode, currentIndex+1, left, right, tracker)
        
        else:
            nextNode = head.next
            if tracker.reversedTail is None:
                tracker.reversdHead, tracker.reversedTail = head, head
                tracker.reversedTail.next = None
            else:
                temp = tracker.reversdHead
                tracker.reversdHead = head
                tracker.reversdHead.next = temp
            
            self.reverseBetweenHelper(nextNode, currentIndex+1, left, right, tracker)


        

        
        

