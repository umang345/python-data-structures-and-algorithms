'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):
    temp = head 
    while not temp is None:
        if temp.data == k:
            return 1
        temp = temp.next
    return 0