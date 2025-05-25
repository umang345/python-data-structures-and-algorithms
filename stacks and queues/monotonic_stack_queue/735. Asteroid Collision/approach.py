from collections import deque
from typing import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        [5,10,-5]
        '''

        queue = deque()

        index = 0
        n = len(asteroids)
        while index<n:
            if len(queue)==0:
                queue.append(asteroids[index])
                index+=1
            else:
                if queue[-1]>0 and asteroids[index]<0:
                    if queue[-1]+asteroids[index]<0:
                        queue.pop()
                    elif queue[-1]+asteroids[index]==0:
                        queue.pop()
                        index+=1
                    else:
                        index+=1
                else:
                    queue.append(asteroids[index])
                    index+=1
        
        result = []
        while queue:
            result.append(queue.popleft())

        return result