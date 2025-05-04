class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Brute Force
        while not headA is None:
            traversalHeadB = headB
            while not traversalHeadB is None:
                if headA is traversalHeadB:
                    return traversalHeadB
                traversalHeadB = traversalHeadB.next
            
            headA = headA.next
        return None