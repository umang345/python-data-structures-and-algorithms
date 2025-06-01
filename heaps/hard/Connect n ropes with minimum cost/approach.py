import heapq

class Solution:
   def minCost(self, arr):
       
       minHeap = [num for num in arr]
       heapq.heapify(minHeap)
       cost = 0
       
       while len(minHeap)>1:
           min1 = heapq.heappop(minHeap)
           min2 = heapq.heappop(minHeap)
           cost+=(min1+min2)
           heapq.heappush(minHeap, min1+min2)
          
       return cost