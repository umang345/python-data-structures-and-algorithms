import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []    

    def addNum(self, num: int) -> None:
        if (not self.maxHeap) or (-self.maxHeap[0]) > num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        
        while len(self.maxHeap) > len(self.minHeap)+1:
            element = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -element)

        while len(self.maxHeap) < len(self.minHeap):
            element = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -element)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            mid1 = self.minHeap[0]
            mid2 = -self.maxHeap[0]
            return (mid1+mid2)/2
        else:
            return -self.maxHeap[0]
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()