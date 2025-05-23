from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        result = [1]*n

        for index in range(1,n):
            if ratings[index] > ratings[index-1]:
                result[index] = result[index-1]+1
        
        for index in range(n-2,-1,-1):
            if ratings[index] > ratings[index+1]:
                minNumReq = result[index+1]+1
                result[index] = max(result[index], minNumReq)
        
        return sum(result)