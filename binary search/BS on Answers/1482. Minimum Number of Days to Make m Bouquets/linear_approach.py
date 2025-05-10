from functools import reduce
from typing import *


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3

        wait 7 day
        [7,7,7,7,_,7,7]
        [7,7,7,7,_, 7,7]


        '''
        if m*k > len(bloomDay):
            return -1

        minBloomTime = reduce(lambda acc,x : min(acc,x), bloomDay, bloomDay[0])
        maxBloomTime = reduce(lambda acc,x : max(acc,x), bloomDay, bloomDay[0])

        for bloomTime in range(minBloomTime, maxBloomTime+1):

            isPossible = self.helper(bloomDay, bloomTime,m,k)
            if isPossible:
                return bloomTime
        
        return -1

    def helper(self, bloomDay:List[int], bloomTime:int, m:int, k:int) -> bool:
        count = 0

        currAdjFlowerCount = 0 
        for day in bloomDay:
            if day<=bloomTime:
                currAdjFlowerCount+=1
            else:
                count += (currAdjFlowerCount//k)
                currAdjFlowerCount = 0

        count += (currAdjFlowerCount//k)
        
        return count>=m
        

'''
k = max-min+1
TC -> O(n) + O(n) + O(k * n)
SC -> O(1)
'''

