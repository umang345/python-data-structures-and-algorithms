class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        cache = [0 for index in range(len(arr)+1)]

        for index in range(len(arr)-1, -1, -1):
            maxSum = 0
            maxElementSoFar = None
            arrSizeSoFar = 0
            for partitionIndex in range(index, min(index+k, len(arr))):
                arrSizeSoFar+=1
                if maxElementSoFar is None or maxElementSoFar < arr[partitionIndex]:
                    maxElementSoFar = arr[partitionIndex]
                currentSubarraySum = arrSizeSoFar * maxElementSoFar

                currSum = currentSubarraySum + cache[partitionIndex+1]
                if currSum > maxSum:
                    maxSum = currSum

            cache[index] = maxSum
        
        return cache[0]