class Node:
    def __init__(self, val):
        self.val = val
        self.min = val
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.head.min = min(self.head.min, self.head.next.min)        

    def pop(self) -> None:
        temp = self.head
        self.head = self.head.next
        del temp
        

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()