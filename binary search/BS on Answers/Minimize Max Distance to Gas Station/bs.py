from math import *

def minimiseMaxDistance(arr: list, k: int) -> float:
    
    maxSlot = -1
    for index in range(len(arr)-1):
        slot = arr[index+1]-arr[index]
        if slot > maxSlot:
            maxSlot = slot
    
    low, high = 0,maxSlot

    while (high-low > (10**(-6))):

        mid = low + (high-low)/2

        stationsNeeded = 0

        for index in range(len(arr)-1):
            slot = arr[index+1]-arr[index]
            stationsPossible = slot//mid 
            if (stationsPossible*mid)==slot:
                stationsPossible-=1
            
            stationsNeeded+=stationsPossible
        
        if stationsNeeded <= k:
            high = mid
        else:
            low = mid 
    
    return high