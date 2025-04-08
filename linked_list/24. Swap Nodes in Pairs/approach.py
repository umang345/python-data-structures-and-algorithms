# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        currentNode = head
        nextNode = head.next
        
        remainingNodes = head.next.next

        nextNode.next = currentNode
        currentNode.next = self.swapPairs(remainingNodes)

        return nextNode

        