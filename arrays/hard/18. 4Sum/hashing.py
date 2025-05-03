from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
        a + b + c + d = target
        c+d = target - a - b
        c+d = newTarget
        c = newTarget - d
        '''

        arr = sorted(nums)
        tempSet = set()
        result = []
        n = len(nums)
        for a in range(n):
            if a!=0 and arr[a]==arr[a-1]:
                continue
            for b in range(a+1,n):
                if b!=a+1 and arr[b]==arr[b-1]:
                    continue
                
                hashSet = set()
                newTarget = target - arr[a] - arr[b]
                for index in range(b+1, n):
                    elementToSearch = newTarget - arr[index]
                    if elementToSearch in hashSet:
                        quad = [arr[a], arr[b], elementToSearch, arr[index]]
                        quad.sort()
                        tempSet.add(tuple(quad))

                    hashSet.add(arr[index])

        for t in tempSet:
            result.append(list(t))

        return result
    

'''
TC -> O(nlogn)  + O(n^3)
SC -> O(n-2) + O(4*k) 
'''