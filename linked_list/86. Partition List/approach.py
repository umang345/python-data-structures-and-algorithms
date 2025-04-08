# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessThanXHead, lessThanXTail, greaterThanXHead, greaterThanXTail = None, None, None, None

        currentNode = head
        while not currentNode is None:
            if currentNode.val < x:
                if lessThanXTail is None:
                    lessThanXHead, lessThanXTail = currentNode,currentNode
                else:
                    lessThanXTail.next = currentNode
                    lessThanXTail = lessThanXTail.next
                currentNode = currentNode.next
                lessThanXTail.next = None
            else:
                if greaterThanXTail is None:
                    greaterThanXHead,greaterThanXTail = currentNode,currentNode
                else:
                     greaterThanXTail.next = currentNode
                     greaterThanXTail = greaterThanXTail.next
                currentNode = currentNode.next
                greaterThanXTail.next = None
        
        if lessThanXTail is None:
            return greaterThanXHead

        lessThanXTail.next = greaterThanXHead
        return lessThanXHead
