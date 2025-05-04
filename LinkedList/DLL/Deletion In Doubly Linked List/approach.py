from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the Node class:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


def deleteNode(head, pos):
    if pos == 0:
        return head.next
    
    temp = head
    jumps = pos-1

    while jumps>0:
        temp = temp.next
        jumps-=1
    
    temp.next = temp.next.next 
    return head
    
