from typing import List

def findMaxFruits(arr: List[int], n: int) -> int:
    
    maxLen = 0
    for startIndex in range(n):
        currLen = 0
        fruits = set()
        for index in range(startIndex,n):
            fruits.add(arr[index])
            if len(fruits) > 2:
                break
            currLen+=1
            maxLen = max(maxLen, currLen)

    return maxLen
