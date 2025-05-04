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


def insert(k, val, head):
    
    newNode = Node(val)
    if k==0:
        newNode.next = head 
        head.prev = newNode 
        return newNode 
    
    temp = head 
    jumps = k-1
    while jumps>0:
        temp = temp.next 
        jumps-=1

    if temp.next is None:
        temp.next = newNode 
        newNode.prev = temp 
    else:
        newNode.next = temp.next 
        temp.next.prev = newNode
        newNode.prev = temp 
        temp.next = newNode
    return head