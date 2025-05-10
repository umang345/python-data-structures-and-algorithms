from functools import reduce
from typing import *
from math import inf

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        totalLoad = reduce(lambda acc,x: acc+x, weights, 0)
        maxWeight = reduce(lambda acc,x: max(acc,x), weights, weights[0])

        low, high = maxWeight, totalLoad
        result = inf
        while low<=high:
            capacity = low + (high-low)//2
            
            if self.computeRequiredDays(weights, capacity) <= days:
                result = min(result, capacity)
                high = capacity - 1
            else:
                low = capacity+1
        
        return result

    def computeRequiredDays(self, weights:List[int], capacity:int) -> int:
        days = 0
        currentLoad = 0
        for weight in weights:
            currentLoad+=weight
            if currentLoad > capacity:
                days+=1
                currentLoad = weight
        
        if currentLoad>0:
            days+=1
        return days

        