# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        lengthOfList = self.getLength(head) 
        if lengthOfList == 0:
            return head
        k = k%(lengthOfList)

        initialNodes,_ = self.getLastKNodes(head,k)
        latterNodes = self.getFirstKNodes(head, lengthOfList-k)

        if initialNodes is None:
            return latterNodes

        temp = initialNodes
        while not temp.next is None:
            temp = temp.next

        temp.next = latterNodes
        return initialNodes


    def getFirstKNodes(self, head:ListNode, k:int) -> ListNode:
        if head is None or k==0:
            return None

        head.next = self.getFirstKNodes(head.next, k-1)
        return head

    def getLastKNodes(self, head:ListNode, k:int) -> (ListNode, int):
        if head is None:
            return head,0

        nextNode, nextIndex = self.getLastKNodes(head.next,k)
        currentIndex = nextIndex+1

        if currentIndex > k:
            return (nextNode, currentIndex)
        
        head.next = nextNode
        return (head, currentIndex)

    def getLength(self, head:ListNode) -> int:
        count = 0
        temp = head
        while not temp is None:
            count+=1
            temp = temp.next

        return count

    
        