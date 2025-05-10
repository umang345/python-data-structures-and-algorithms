from functools import reduce
from math import *
from typing import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [3, 6, 7, 11]   h = 4
        k = 11 
        '''
        
        maxPile = reduce(lambda acc,x : max(acc,x), piles, piles[0])
        low, high = 1, maxPile
        minRateNeeded = inf

        while low <= high:
            currEatingRate = low + (high - low)//2
            
            hoursNeeded = self.computeHours(piles, currEatingRate)
            if hoursNeeded <= h:
                minRateNeeded = min(minRateNeeded, currEatingRate)
                high = currEatingRate-1
            else:
                low = currEatingRate+1
        
        return minRateNeeded
    
    def computeHours(self, piles:List[int], eatingRate:int) -> int:
        hours = 0
        for pile in piles:
            hours += (ceil(pile/eatingRate))
        return hours

