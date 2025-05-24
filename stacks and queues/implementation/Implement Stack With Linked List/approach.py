class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
        self.top = None
        self.count = 0 
        
    def getSize(self):
        return self.count

    def isEmpty(self):
        return self.count==0 

    def push(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top 
            self.top = newNode
        self.count+=1

    def pop(self):
        if not self.isEmpty():
            temp = self.top 
            self.top = self.top.next 
            del temp 
            self.count-=1

    def getTop(self):
        if self.isEmpty():
            return -1
        
        return self.top.data
