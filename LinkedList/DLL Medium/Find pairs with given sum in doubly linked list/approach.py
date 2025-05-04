class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> [[int]]:
    
    start = head
    tail = head 

    result = []

    while not tail.next is None:
        tail = tail.next 

    while not start is tail:
        currSum = start.data + tail.data
        if currSum==k:
            result.append([start.data, tail.data])
             
        if currSum<=k:
            start = start.next 
        else:
            tail = tail.prev 
    
    return result