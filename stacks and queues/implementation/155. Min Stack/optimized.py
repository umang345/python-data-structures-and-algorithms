from collections import deque
from math import *

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = inf

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append(val)
            self.min = val
        else:
            if val < self.min:
                updatedVal = (2*val) - self.min
                self.min = val
                self.stack.append(updatedVal)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] < self.min:
            prevMin = (2*self.min) - self.stack[-1]
            self.min = prevMin
        self.stack.pop()


    def top(self) -> int:
        if self.min > self.stack[-1]:
            return self.min
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()