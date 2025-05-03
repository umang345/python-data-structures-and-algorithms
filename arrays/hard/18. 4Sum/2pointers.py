from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
        a + b + c + d = target
        c+d = target - a - b
        c+d = newTarget
        c = newTarget - d
        '''

        result = []
        n = len(nums)
        arr = sorted(nums)
        for a in range(n):
            if a!=0 and arr[a]==arr[a-1]:
                continue
            for b in range(a+1,n):
                if b!=a+1 and arr[b]==arr[b-1]:
                    continue
                
                constantSum = arr[a]+arr[b]
                c,d = b+1,n-1
                while c<d:
                    currSum = constantSum + arr[c]+arr[d]
                    if currSum == target:
                        result.append([arr[a], arr[b], arr[c], arr[d]])
                        c+=1
                        while c<d and arr[c]==arr[c-1]:
                            c+=1
                    elif currSum < target:
                        c+=1
                        while c<d and arr[c]==arr[c-1]:
                            c+=1
                    else:
                        d-=1
                        while c<d and arr[d]==arr[d+1]:
                            d-=1
        return result
    
'''
TC -> O(nlogn) +  O(n^3)
SC -> O(1)
'''