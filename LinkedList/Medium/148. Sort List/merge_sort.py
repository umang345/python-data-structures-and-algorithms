from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)

    def getMidNode(self,head:ListNode) -> ListNode:
        slow,fast = head, head
        '''
        [4,2,1]
        '''

        while not fast is None and not fast.next is None and not fast.next.next is None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def mergeSort(self, head:ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        midNode = self.getMidNode(head)
        list1 = head
        list2 = midNode.next
        midNode.next = None

        list1 = self.mergeSort(list1)
        list2 = self.mergeSort(list2)

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        sortedHead, tail = None, None
        if list1.val <= list2.val:
            sortedHead, tail = list1, list1
            list1 = list1.next
        else:
            sortedHead, tail = list2, list2
            list2 = list2.next


        while not list1 is None and not list2 is None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            tail.next = None
        
        if not list1 is None:
            tail.next = list1
        
        if not list2 is None:
            tail.next = list2
        
        return sortedHead