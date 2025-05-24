from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        self.stackTop = -1
        self.store = [-1]*n

    def push(self, num: int):
        if self.stackTop+1 < len(self.store):
            self.stackTop+=1
            self.store[self.stackTop] = num
            

    def pop(self) -> int:
        if self.stackTop==-1:
            return -1
        else:
            valuestackTopop = self.store[self.stackTop]
            self.stackTop-=1
            return valuestackTopop

    def top(self) -> int:
        if self.stackTop == -1:
            return -1
        else:
            return self.store[self.stackTop]

    def isEmpty(self) -> int:
        return self.stackTop==-1

    def isFull(self) -> int:
        return self.stackTop == len(self.store)-1