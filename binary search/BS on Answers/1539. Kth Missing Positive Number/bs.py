from typing import *

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        [2,3,4,7,11]
        [1,1,1,3,6]

        [1,2,3,4]
        [0,0,0,0]
        '''

        missingTill = [0]*(len(arr))

        for index in range(len(arr)):
            currDif = arr[index] - (index+1)
            missingTill[index] = currDif

        low,high = 0, len(arr)-1
        while low<=high:
            mid = low + (high-low)//2
            if missingTill[mid] < k:
                low = mid+1
            else:
                high = mid-1
        
        return low + k