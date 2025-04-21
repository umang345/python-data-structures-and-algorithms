class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        return self.helper(0,n, cuts)

    def helper(self, start:int, end:int, cuts:list) -> int:

        if start == end or start+1==end:
            return 0

        currLen = end - start
        currentMin = None

        for index in cuts:
            if index > start and index < end:
                currCost = self.helper(start,index, cuts) + self.helper(index,end, cuts) + currLen
                if currentMin is None or currentMin > currCost:
                    currentMin = currCost
        
        if currentMin is None:
            return 0

        return currentMin