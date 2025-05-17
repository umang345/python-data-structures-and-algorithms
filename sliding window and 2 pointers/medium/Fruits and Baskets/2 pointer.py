from typing import List

'''
TC  O(n + n)
'''

def findMaxFruits(arr: List[int], n: int) -> int:
    maxLen = 0
    start, end = 0,0
    fruits = dict()

    while end < n:
        fruits[arr[end]] = fruits.get(arr[end],0)+1

        if len(fruits.keys()) > 2:
            while len(fruits.keys()) > 2:
                fruits[arr[start]]-=1
                if fruits[arr[start]]==0:
                    del fruits[arr[start]]
                start+=1
        
        currLen = end-start+1
        maxLen = max(currLen, maxLen)
        end+=1
    
    return maxLen