from math import *


def minimiseMaxDistance(arr: list, k: int) -> float:
    
    '''
    [ 0  0   0  0  0  0]
    [1, 2, 3, 4, 5, 6, 7]
    '''
    stations = [0]*(len(arr)-1)

    for gasStation in range(k):

        nextMaxIndex = -1
        maxSlot = -inf
        for index in range(len(arr)-1):
            diff = arr[index+1]-arr[index]
            slotSize = diff/(stations[index]+1)
            if slotSize > maxSlot:
                maxSlot = slotSize
                nextMaxIndex = index 
        
        stations[nextMaxIndex]+=1
    
    maxDistance = -inf 
    for index in range(len(arr)-1):
        diff = arr[index+1] - arr[index]
        slot = diff/(stations[index]+1)
        if slot > maxDistance:
            maxDistance = slot
    
    return maxDistance

'''
TC     O(n*n) + O(n)
SC     O(n)
'''