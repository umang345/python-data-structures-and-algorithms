class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    
    temp = head 
    while not temp is None and not temp.next is None:
        if temp.next.data == k:
            nodeToDel = temp.next
            if not temp.next.next is None:
                temp.next.next.prev = temp.next
            temp.next = temp.next.next 
            del nodeToDel
        else:
            temp = temp.next 
        

    if head.data == k:
        return head.next 
    
    return head