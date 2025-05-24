from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        
        valToReturn = self.q1.popleft()

        while len(self.q2) > 0:
            self.q1.append(self.q2.popleft())
        
        return valToReturn


    def top(self) -> int:
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        
        valToReturn = self.q1[0]
        self.q2.append(self.q1.popleft())

        while len(self.q2) > 0:
            self.q1.append(self.q2.popleft())
        
        return valToReturn

    def empty(self) -> bool:
        return len(self.q1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()