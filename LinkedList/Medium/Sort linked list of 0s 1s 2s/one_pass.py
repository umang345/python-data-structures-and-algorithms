'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def sortList(head):
    head0, head1, head1 = None, None, None 
    tail0, tail1, tail2 = None, None, None 
    temp = head

    while not temp is None:
        if temp.data == 0:
            if tail0 is None:
                head0, tail0 = temp,temp
            else:
                tail0.next = temp
                tail0 = tail0.next
            temp = temp.next  
            tail0.next = None 
        
        elif temp.data == 1:
            if tail1 is None:
                head1, tail1 = temp,temp
            else:
                tail1.next = temp 
                tail1 = tail1.next 
            temp = temp.next 
            tail1.next = None
        else:
            if tail2 is None:
                head2, tail2 = temp,temp
            else:
                tail2.next = temp 
                tail2 = tail2.next 
            temp = temp.next 
            tail2.next = None
    
    sortedHead = None 
    sortedTail = None 
    if not tail0 is None:
        sortedHead, sortedTail = head0, tail0
    
    if not tail1 is None:
        if sortedTail is None:
            sortedHead, sortedTail = head1, tail1
        else:
            sortedTail.next = head1 
            sortedTail = tail1 
    
    if not tail2 is None:
        if sortedTail is None:
            sortedHead, sortedTail = head2, tail2
        else:
            sortedTail.next = head2 
            sortedTail = tail2
    
    return sortedHead