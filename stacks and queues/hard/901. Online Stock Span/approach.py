from collections import deque

class StockSpanner:

    def __init__(self):
        self.stack=deque()
        self.day = 0

    def next(self, price: int) -> int:
        self.day+=1
        while self.stack and self.stack[0][1]<=price:
            self.stack.popleft()
        
        result = self.day
        if self.stack:
            result = result - self.stack[0][0]
        
        self.stack.appendleft((self.day, price))
        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)