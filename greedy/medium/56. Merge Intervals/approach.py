from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return []
        
        intervals.sort(key = lambda x : (x[0],x[1]))
        result = []
        result.append(intervals[0])

        currIndex = 1
        while currIndex < len(intervals):
            prev = result[-1]
            curr = intervals[currIndex]
            if self.checkIfIntervalsOverlap(prev, curr):
                result[-1][0] = min(prev[0], curr[0])
                result[-1][1] = max(prev[1], curr[1])
            else:
                result.append(intervals[currIndex])
            currIndex+=1
        
        return result
            
    def checkIfIntervalsOverlap(self, int1:list, int2:list) -> bool:
        if int1[0] >= int2[0] and int1[0] <= int2[1]:
            return True
        if int2[0] >= int1[0] and int2[0] <= int1[1]:
            return True
        return False