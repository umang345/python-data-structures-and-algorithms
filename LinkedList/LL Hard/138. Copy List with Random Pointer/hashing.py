from typing import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = dict()
        newHead,tail = None,None
        temp = head 

        while not temp is None:
            newNode = Node(temp.val)
            if tail is None:
                newHead, tail = newNode, newNode
            else:
                tail.next = newNode
                tail = tail.next 
            
            hashMap[temp] = tail
            temp = temp.next

        temp1, temp2 = head, newHead
        while not temp1 is None:
            if not temp1.random is None:
                nodeToPoint = hashMap[temp1.random]
                temp2.random = nodeToPoint

            temp1 = temp1.next
            temp2 = temp2.next

        return newHead 
