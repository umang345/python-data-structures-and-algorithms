'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverseDLL(head):
    reversedHead,_ = helper(head)
    return reversedHead

def helper(head) -> tuple[Node, Node]:
    if head is None:
        return (head,head)
    if head.next is None:
        head.prev = None
        return (head, head)
    
    nextHead, nextTail = helper(head.next)
    head.prev = nextTail
    head.next = None 
    nextTail.next = head 
    nextTail = nextTail.next
    return (nextHead, nextTail) 