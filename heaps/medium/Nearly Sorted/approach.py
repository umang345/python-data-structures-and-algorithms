from os import *
from sys import *
from collections import *
from math import *
import heapq

def nearlySorted(arr, k):

    pq = []
    
    for index in range(k+1):
        heapq.heappush(pq, (arr[index], arr[index]))

    result = []
    for index in range(k+1, len(arr)):
        _, poppedNum = heapq.heappop(pq)
        result.append(poppedNum)
        heapq.heappush(pq, (arr[index], arr[index]))
    
    while len(pq)>0:
        _, poppedNum = heapq.heappop(pq)
        result.append(poppedNum)

    return result
            
    