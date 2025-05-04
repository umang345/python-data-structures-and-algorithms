# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        updated_list, _ = self.removeNthFromEndHelper(head, n)
        return updated_list

    
    def removeNthFromEndHelper(self, head:ListNode, n) -> (ListNode, int):
        if head is None:
            return (head,0)

        nextNode, nextVal = self.removeNthFromEndHelper(head.next, n)
        currentVal = nextVal+1

        if currentVal==n:
            return (nextNode, currentVal)
        
        head.next = nextNode
        return (head, currentVal)
        