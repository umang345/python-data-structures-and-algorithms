from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        result = []
        for i in range(len(arr)):
            if i!=0 and arr[i]==arr[i-1]:
                continue
            j,k = i+1, len(arr)-1
            while(j<k):
                currSum = arr[i]+arr[j]+arr[k]
                if currSum == 0:
                    result.append([arr[i], arr[j], arr[k]])
                    j+=1
                    # Move j until we find a unique j
                    while j < k and arr[j]==arr[j-1]:
                        j+=1
                elif currSum < 0:
                    j+=1
                    # Move j until we find a unique j
                    while j < k and arr[j]==arr[j-1]:
                        j+=1
                else:
                    k-=1
                    # Move k until we find a unique k
                    while j<k and arr[k]==arr[k+1]:
                        k-=1

        return result
    
'''
TC -> O(nlogn) + O(n^2)
SC -> O(1)
'''