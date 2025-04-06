# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2+3 = 5        3+2=5
# Both will travel same distance and at the end will reach same point
# so if they intersect, they would have travelled same distance till then

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        traversalHeadA = headA
        traversalHeadB = headB

        while not traversalHeadA is traversalHeadB:
            
            if traversalHeadA is None:
                traversalHeadA = headB
            if traversalHeadB is None:
                traversalHeadB = headA

            if traversalHeadA is traversalHeadB:
                return traversalHeadA
            
            traversalHeadA = traversalHeadA.next
            traversalHeadB = traversalHeadB.next

        return traversalHeadA