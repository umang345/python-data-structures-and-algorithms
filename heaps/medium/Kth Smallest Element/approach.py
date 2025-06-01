from os import *
from sys import *
from collections import *
from math import *
import heapq

def kthSmallest(n, k,arr):
    
    if k > len(arr):
        raise Exception("Invalid input")

    pq = []
    for num in arr:
        heapq.heappush(pq, (num, num))
    
    for _ in range(k-1):
        heapq.heappop(pq)
    
    _, res = heapq.heappop(pq)
    return res

    
