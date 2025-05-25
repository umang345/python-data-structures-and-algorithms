from collections import deque 
from typing import * 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        result = [-1]*(len(nums)-k+1)

        for index in range(k):
            while queue and queue[-1][1] < nums[index]:
                queue.pop()
            
            queue.append((index, nums[index]))
        
        result[0] = queue[0][1]
        currIndex = 1
        left, right = 0,  k-1

        while right<len(nums)-1:
            left+=1
            right+=1

            while queue and queue[0][0]<left:
                queue.popleft()
            
            while queue and queue[-1][1] < nums[right]:
                queue.pop()
            
            queue.append((right,nums[right]))

            result[currIndex] = queue[0][1]
            currIndex+=1
        
        return result





