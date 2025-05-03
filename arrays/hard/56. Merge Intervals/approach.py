from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])

        result = [intervals[0]]

        for index in range(1, len(intervals)):
            currStart, currEnd = result[-1][0], result[-1][1]
            if intervals[index][0]<=currEnd:
                result[-1][1] = max(currEnd, intervals[index][1])
            else:
                result.append(intervals[index])

        return result  