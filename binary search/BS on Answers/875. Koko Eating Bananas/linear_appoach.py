from functools import reduce
from math import ceil
from typing import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [3, 6, 7, 11]   h = 4
        k = 11 
        '''
        largestPile = reduce(lambda acc,x : max(acc,x), piles, piles[0])
        for bananaEatingRate in range(1,largestPile+1):
            hoursNeeded = self.computeHours(piles, bananaEatingRate)
            if hoursNeeded <= h:
                return bananaEatingRate
        
        return -1
    
    def computeHours(self, piles: List[int], eatingRate:int) -> int:
        hours = 0
        for pile in piles:
            hours = hours + ceil(pile/eatingRate)
        
        return hours

        
'''
TC    O(len(piles)) + O(max(piles) * len(piles))
      O(n) + O(max(piles) * n)
'''