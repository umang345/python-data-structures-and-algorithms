from functools import reduce
from math import inf 
from typing import *

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3

        wait 7 day
        [7,7,7,7,_,7,7]
        [7,7,7,7,_, 7,7]

        TC  ->  O(n)+O(m) + (O(log(max-min+1))*n)

        '''
        if m*k > len(bloomDay):
            return -1

        minBloomTime = reduce(lambda acc,x : min(acc,x), bloomDay, bloomDay[0])
        maxBloomTime = reduce(lambda acc,x : max(acc,x), bloomDay, bloomDay[0])

        low, high = minBloomTime, maxBloomTime
        minBloomTime = inf
        isArrangementPossible = False

        while low<=high:
            waitTime = low + (high-low)//2
            
            isPossible = self.helper(bloomDay, waitTime,m,k)
            if isPossible:
                isArrangementPossible = True
                minBloomTime = min(minBloomTime, waitTime)
                high = waitTime-1
            else:
                low = waitTime+1
                
        if not isArrangementPossible:
            return -1
        return minBloomTime

        

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