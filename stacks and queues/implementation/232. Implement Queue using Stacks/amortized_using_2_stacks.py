from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()        

    def push(self, x: int) -> None:
        self.stack1.appendleft(x)

    def pop(self) -> int:
        if len(self.stack2)>0:
            return self.stack2.popleft()
        
        while len(self.stack1)>0:
            self.stack2.appendleft(self.stack1.popleft())
        
        return self.stack2.popleft()
            

    def peek(self) -> int:
        if len(self.stack2)>0:
            return self.stack2[0]
        
        while len(self.stack1)>0:
            self.stack2.appendleft(self.stack1.popleft())
        
        return self.stack2[0]

    def empty(self) -> bool:
        return len(self.stack1)+len(self.stack2)==0