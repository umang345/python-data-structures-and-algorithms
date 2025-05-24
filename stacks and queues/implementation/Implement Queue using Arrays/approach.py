from typing import List

class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.arr= [0] * 100000
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        
        if (self.rear+1)%100000 == self.front:
            return
        
        self.rear = (self.rear+1)%100000
        
        if self.front == -1:
            self.front = self.rear
        
        self.arr[self.rear] = e


    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        
        if self.front == -1:
            return -1 
        
        valToReturn = self.arr[self.front]
        
        if self.front == self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front = (self.front+1)%10000
        
        return valToReturn
