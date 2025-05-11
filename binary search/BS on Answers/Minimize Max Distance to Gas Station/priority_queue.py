from math import *
import heapq


class PQEntity:
    def __init__(self,slot, index,stations=0):
        self.slot = slot 
        self.index = index 
        self.stations = stations

def priority_queue_func(pqEntity:PQEntity):
    return (-pqEntity.slot, pqEntity.index)


def minimiseMaxDistance(arr: list, k: int) -> float:
    pq = []
    for index in range(len(arr)-1):
        entity = PQEntity(arr[index+1]-arr[index], index)
        heapq.heappush(pq,(priority_queue_func(entity), entity))
    
    for gasStation in range(k):
        poppedEntity = heapq.heappop(pq)
        slot = poppedEntity[1].slot 
        index = poppedEntity[1].index
        stations = poppedEntity[1].stations

        stations+=1
        slot = (arr[index+1]-arr[index])/(stations+1)
        updatedEntity = PQEntity(slot, index, stations)
        heapq.heappush(pq,(priority_queue_func(updatedEntity), updatedEntity))
    
    maxSlotEntity = heapq.heappop(pq)
    return maxSlotEntity[1].slot