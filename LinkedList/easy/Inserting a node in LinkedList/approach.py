from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the linkedList class structure:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert(head:Node, n:int, pos:int, val:int):
    newNode = Node(val)
    if pos == 0:
        newNode.next = head 
        return newNode 
    
    temp = head
    jumps = pos-1
    while jumps>0:
        temp = temp.next 
        jumps-=1
    
    nextNode = temp.next 
    temp.next = newNode 
    newNode.next = nextNode 
    return head