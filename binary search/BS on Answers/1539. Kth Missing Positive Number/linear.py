from typing import *

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        currMissingNumber = 1

        missNumberCount = k
        arrIndex = 0
        while missNumberCount > 0 and arrIndex < len(arr):
            if currMissingNumber == arr[arrIndex]:
                arrIndex+=1
                currMissingNumber+=1
            else:
                currMissingNumber+=1
                missNumberCount-=1
        
        return currMissingNumber + missNumberCount -1
    

'''
TC -> O(max(arr))
'''