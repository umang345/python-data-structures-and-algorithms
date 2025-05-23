from typing import *

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)

        indexToInsert = self.getPositionToInsertInterval(intervals,newInterval)
        
        index = 0
        while index < indexToInsert:
            result.append(intervals[index])
            index+=1
        
        if index==0:
            result.append(newInterval)
        else:
            prev = result[-1]
            curr = newInterval
            if self.checkIfIntervalsOverlap(prev, curr):
                result[-1][0] = min(prev[0], curr[0])
                result[-1][1] = max(prev[1], curr[1])
            else:
                result.append(newInterval)



        while index < n:
            prev = result[-1]
            curr = intervals[index]
            if self.checkIfIntervalsOverlap(prev, curr):
                result[-1][0] = min(prev[0], curr[0])
                result[-1][1] = max(prev[1], curr[1])
            else:
                result.append(curr)
            index+=1
        
        return result
            

    def getPositionToInsertInterval(self,intervals:list, newInterval):
        
        if len(intervals) == 0 or newInterval[0] <= intervals[0][0]:
            return 0
        if newInterval[0] >= intervals[-1][0]:
            return len(intervals)
        
        index = 0
        while index<len(intervals):
            if intervals[index][0]>newInterval[0]:
                return index
            index+=1

    def checkIfIntervalsOverlap(self, interval1, interval2):
        if interval1[0]>=interval2[0] and interval1[0]<=interval2[1]:
            return True
        
        if interval2[0]>=interval1[0] and interval2[0]<=interval1[1]:
            return True
        
        return False

            
        
        
            
        
