from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()        

    def push(self, x: int) -> None:
        self.stack1.appendleft(x)

    def pop(self) -> int:
        while len(self.stack1)>1:
            self.stack2.appendleft(self.stack1.popleft())
        
        valToReturn = self.stack1.popleft()
        while len(self.stack2)>0:
            self.stack1.appendleft(self.stack2.popleft())
        
        return valToReturn
            

    def peek(self) -> int:
        while len(self.stack1)>1:
            self.stack2.appendleft(self.stack1.popleft())
        
        valToReturn = self.stack1[0]
        self.stack2.appendleft(self.stack1.popleft())

        while len(self.stack2)>0:
            self.stack1.appendleft(self.stack2.popleft())
        
        return valToReturn

    def empty(self) -> bool:
        return len(self.stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()