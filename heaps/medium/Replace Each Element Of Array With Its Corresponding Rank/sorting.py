from typing import List

def replaceWithRank(arr: List[int],n : int) -> List[int]:
    
    indexNumList = []
    for index, num in enumerate(arr):
        indexNumList.append((num, index))
    
    indexNumList.sort(key=lambda x : (x[0],x[1]))

    result = [-1]*n 

    rank = 1
    for pIndex, pair in enumerate(indexNumList):
        if pIndex>0 and pair[0] > indexNumList[pIndex-1][0]:
            rank+=1
        result[pair[1]] = rank 
    
    return result
