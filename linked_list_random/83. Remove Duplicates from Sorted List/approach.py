# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currentNode = head
        while not currentNode is None and not currentNode.next is None:
            if currentNode.val == currentNode.next.val:
                node_to_delete = currentNode.next
                currentNode.next = currentNode.next.next
                del node_to_delete
            else:
                currentNode = currentNode.next
        
        return head