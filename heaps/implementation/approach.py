from typing import *

class MinPriorityQueue:
    def __init__(self):
        self.pq = []
        self.count = 0

    def add(self, value):
        self.pq.append(value)
        self.count+=1
        self.__adjustForLast()
    
    def pop(self)->int:
        self.count-=1
        removedElement = self.pq[0]
        self.pq[0] = self.pq[-1]
        self.pq.pop()
        self.__adjustForRoot()
        return removedElement

    def __adjustForRoot(self):
        currIndex = 0

        while currIndex<len(self.pq):
            leftChildIndex = (2*currIndex)+1
            rightChildIndex = (2*currIndex)+2

            if leftChildIndex >= len(self.pq):
                return
            
            if rightChildIndex >= len(self.pq):
                if self.pq[leftChildIndex] < self.pq[currIndex]:
                    self.pq[leftChildIndex], self.pq[currIndex] = self.pq[currIndex], self.pq[leftChildIndex]
                    currIndex = leftChildIndex
                else:
                    return
            
            else:
                if self.pq[leftChildIndex] <= self.pq[currIndex] and self.pq[leftChildIndex] <= self.pq[rightChildIndex]:
                    self.pq[leftChildIndex], self.pq[currIndex] = self.pq[currIndex], self.pq[leftChildIndex]
                    currIndex = leftChildIndex
                elif self.pq[rightChildIndex] <= self.pq[currIndex] and self.pq[rightChildIndex] <= self.pq[leftChildIndex]:
                    self.pq[rightChildIndex], self.pq[currIndex] = self.pq[currIndex], self.pq[rightChildIndex]
                    currIndex = rightChildIndex 
                else:
                    return

    def __adjustForLast(self):
        currIndex = len(self.pq)-1

        while currIndex>0:
            parent = (currIndex-1)//2 if currIndex%2!=0 else (currIndex-1)//2
            if self.pq[currIndex] < self.pq[parent]:
                self.pq[currIndex], self.pq[parent] = self.pq[parent], self.pq[currIndex]
                currIndex = parent
            else:
                return

    def __len__(self):
        return self.count
        