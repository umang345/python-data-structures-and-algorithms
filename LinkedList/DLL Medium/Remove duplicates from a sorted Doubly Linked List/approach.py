class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    temp = head 

    while not temp is None and not temp.next is None:
        if temp.next.data == temp.data:
            nodeToDel = temp.next 
            if not temp.next.next is None:
                temp.next.next.prev = temp 
            temp.next = temp.next.next 
            del nodeToDel
        else:
            temp = temp.next 
    
    return head