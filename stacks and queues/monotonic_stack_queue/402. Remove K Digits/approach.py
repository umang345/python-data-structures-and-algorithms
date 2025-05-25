from collections import *

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        queue = deque()
        index = 0
        removal = k
        result = []

        while index < len(num) and removal>0:
            while queue and removal>0 and int(queue[-1])>int(num[index]):
                queue.pop()
                removal-=1
            
            queue.append(num[index])
            index+=1

        while index < len(num):
            queue.append(num[index])
            index+=1
        
        while removal>0:
            queue.pop()
            removal-=1
        
        while queue and queue[0]=="0":
            queue.popleft()
        
        while queue:
            result.append(queue.popleft())

        if result:
            return "".join(result)
        
        return "0"
        


