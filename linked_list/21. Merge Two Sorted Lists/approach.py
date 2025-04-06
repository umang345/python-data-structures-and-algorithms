# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        mergedNodeHead = None
        mergedNodeTail = None
        head1 = list1
        head2 = list2

        while (not head1 is None) and (not head2 is None):
            if head1.val <= head2.val:
                if mergedNodeHead is None:
                    mergedNodeHead = head1
                    mergedNodeTail = head1
                else:
                    mergedNodeTail.next = head1
                    mergedNodeTail = mergedNodeTail.next
                
                head1 = head1.next
                mergedNodeTail.next = None
            
            else:
                if mergedNodeHead is None:
                    mergedNodeHead = head2
                    mergedNodeTail = head2
                else:
                    mergedNodeTail.next = head2
                    mergedNodeTail = mergedNodeTail.next
                
                head2 = head2.next
                mergedNodeTail.next = None
        
        if not head1 is None:
            mergedNodeTail.next = head1
        if not head2 is None:
            mergedNodeTail.next = head2
        
        return mergedNodeHead


                    