from typing import *

def countGreater(N: int, Q: int, arr: List[int], query: List[int]) -> List[int]:
    
    result = [0]*Q 

    greaterCount = [0]*N

    for index in range(N):
        count=0
        for nextIndex in range(index+1,N):
            if arr[nextIndex] > arr[index]:
                count+=1
        
        greaterCount[index] = count 
    
    for index,q in enumerate(query):
        result[index] = greaterCount[q]
    
    return result