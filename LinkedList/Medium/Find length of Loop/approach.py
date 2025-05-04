class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    isCyle, meetInMiddleNode = isCyclePresent(head)
    if not isCyle:
        return 0

    count = 1
    temp = meetInMiddleNode.next 
    while not temp is meetInMiddleNode:
        count+=1
        temp = temp.next 
    
    return count 


def isCyclePresent(head:Node) -> tuple[bool,Node]:
    slow,fast = head, head 

    while not fast is None and not fast.next is None:
        slow = slow.next
        fast = fast.next.next 

        if slow is fast:
            return (True, slow)
        
    return (False, None)

