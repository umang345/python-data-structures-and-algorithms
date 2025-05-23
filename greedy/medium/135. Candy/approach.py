from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        left = [1]*n
        right = [1]*n
        result = [0]*n

        for index in range(1,n):
            if ratings[index]>ratings[index-1]:
                left[index] = left[index-1]+1
        
        for index in range(n-2,-1,-1):
            if ratings[index]>ratings[index+1]:
                right[index] = right[index+1]+1
        
        for index in range(n):
            result[index] = max(left[index], right[index])
    
        return sum(result)


        