# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        shortHead,shortLen, longHead, longLen = self.getLongAndShortNodeRefs(headA, headB)

        lenDiff = longLen - shortLen

        while lenDiff>0:
            longHead = longHead.next
            lenDiff-=1
        
        while not shortHead is None and not longHead is None:
            if shortHead is longHead:
                return shortHead
            shortHead = shortHead.next
            longHead = longHead.next

        return None

        


    def getLongAndShortNodeRefs(self, headA:ListNode, headB:ListNode) -> (ListNode,int,ListNode, int):

        traversalA, traversalB = headA, headB
        lenA,lenB = 0,0
        lenA = self.getListLength(traversalA)
        lenB = self.getListLength(traversalB)
        if lenA<=lenB:
            return (headA,lenA, headB, lenB)
        else:
            return (headB,lenB, headA, lenA)

    
    def getListLength(self, head:ListNode) -> int:
        count = 0
        while not head is None:
            count+=1
            head = head.next
        return count 