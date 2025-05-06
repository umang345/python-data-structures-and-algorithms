class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

import heapq

def flattenLinkedList(head: Node) -> Node:

    pq = []
    temp = head 
    while not temp is None:
        heapq.heappush(pq, (temp.data, temp))
        temp = temp.next 
    
    newHead, tail = None, None

    while len(pq)>0:
        _, node = heapq.heappop(pq)
        if tail is None:
            newHead, tail = node, node 
        else:
            tail.child = node 
            tail = tail.child

        node = node.child
        tail.child = None  
        if not node is None:
            heapq.heappush(pq,(node.data, node))
    
    return newHead
    
