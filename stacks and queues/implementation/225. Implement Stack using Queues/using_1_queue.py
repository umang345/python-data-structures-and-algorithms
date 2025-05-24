from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        currLen = len(self.q1)

        while currLen>1:
            currLen-=1
            self.q1.append(self.q1.popleft())
        
        valToReturn = self.q1.popleft()
        
        return valToReturn


    def top(self) -> int:
        currLen = len(self.q1)

        while currLen>1:
            currLen-=1
            self.q1.append(self.q1.popleft())
        
        valToReturn = self.q1[0]
        self.q1.append(self.q1.popleft())
        return valToReturn

    def empty(self) -> bool:
        return len(self.q1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()