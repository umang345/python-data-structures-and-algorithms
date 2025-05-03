from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        temp = set()
        arr = sorted(nums)
        for i in range(len(nums)):
            if i!=0 and arr[i]==arr[i-1]:
                continue
            hashSet = set()
            target = -arr[i]
            

            for nextIndex in range(i+1, len(nums)):
                numToCheck = target - arr[nextIndex]
                if numToCheck in hashSet:
                    lis = [arr[i], numToCheck, arr[nextIndex]]
                    lis.sort()
                    temp.add(tuple(lis))
                
                hashSet.add(arr[nextIndex])
        
        for t in temp:
            result.append(list(t))

        return result
    

'''
TC   O(nlogn)  +   O(n^2)
SC   O(n)   
'''