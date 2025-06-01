import heapq

'''
Sort the lists in reverse order 
So 1st index of both list will always be included
Use a priority queue as max heap
in priority queue, add the element and indexes picked

when popping out element with indexs (i,j)
insert sum with (i, j+1) and (i+1, j)

This will try all possible combinations in reverse order
'''

class Solution:
    def maxCombinations(self, N, K, A, B):
        
        maxHeap = []
        A.sort(reverse = True)
        B.sort(reverse = True)
        
        result = []
        maxHeap.append( (-(A[0]+B[0]), (0,0)) )
        visited = set()
        
        while len(result)<K:
            currSum, indexes = heapq.heappop(maxHeap)
            if indexes in visited:
                continue
            visited.add(indexes)
            result.append(-currSum)
            i,j = indexes
            
            if i+1<N:
                heapq.heappush(maxHeap, (-(A[i+1]+B[j]) , (i+1,j)))
            if j+1<N:
                heapq.heappush(maxHeap, (-(A[i]+B[j+1]) , (i,j+1)))
        
        return result