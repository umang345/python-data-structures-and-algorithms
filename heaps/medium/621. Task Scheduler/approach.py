from typing import *
from math import *

'''
Time complexity: O(n) + O(n^2)
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = dict()
        for task in tasks:
            if freqMap.get(task) is None:
                freqMap[task] = [1,-(n+1)]
            else:
                freqMap[task][0]+=1
        

        currTime = 0

        while len(freqMap)>0:
            currTime+=1
            currTask, currMaxCount = None, -inf
            for task, pair in freqMap.items():
                count, lastExec = pair
                if (currTime-lastExec)>n:
                    if currMaxCount < count:
                        currMaxCount = count
                        currTask = task
            
            if not currTask is None:
                if freqMap[currTask][0] == 1:
                    del freqMap[currTask]
                else:
                    freqMap[currTask][0]-=1
                    freqMap[currTask][1] = currTime
        
        return currTime
