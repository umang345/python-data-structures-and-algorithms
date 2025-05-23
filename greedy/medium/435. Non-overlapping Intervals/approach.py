from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals)==0:
            return 0

        intervals.sort(key = lambda x : x[1])
        currEndTime = intervals[0][1]
        countOfRemovingIntervals = 0

        for index in range(1, len(intervals)):
            if currEndTime <= intervals[index][0]:
                currEndTime = intervals[index][1]
            else:   
                countOfRemovingIntervals+=1
        
        return countOfRemovingIntervals