from typing import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        temp = head
        while not temp is None:
            newNode = Node(temp.val)
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next

        temp = head
        while not temp is None:
            if not temp.random is None:
                originalRandomNode = temp.random
                temp.next.random = originalRandomNode.next

            temp = temp.next.next
        
        newHead, tail = None, None
        temp = head

        while not temp is None:
            if tail is None:
                newHead, tail = temp.next, temp.next
            else:
                tail.next = temp.next
                tail = tail.next
            temp.next = tail.next
            temp = temp.next
            tail.next = None

        return newHead