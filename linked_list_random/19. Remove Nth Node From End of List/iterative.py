# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        stack = list()
        updatedHead = None

        temp = head
        while not temp is None:
            stack.append(temp)
            temp = temp.next

        while n>1:
            updatedHead = stack.pop()
            n-=1

        stack.pop()
        if len(stack)!=0:
            stack[len(stack)-1].next = updatedHead

        while len(stack)!=0:
            updatedHead = stack.pop()

        return updatedHead

        