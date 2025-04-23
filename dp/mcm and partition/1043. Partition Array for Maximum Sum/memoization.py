class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        cache = [-1 for index in range(len(arr))]
        return self.helper(0, arr, k,cache)

    def helper(self, index, arr, k, cache) -> int:
        if index >= len(arr) or k==0:
            return 0

        if cache[index]!=-1:
            return cache[index]

        maxSum = 0
        maxElementSoFar = None
        arrSizeSoFar = 0
        for partitionIndex in range(index, min(index+k, len(arr))):
            arrSizeSoFar+=1
            if maxElementSoFar is None or maxElementSoFar < arr[partitionIndex]:
                maxElementSoFar = arr[partitionIndex]
            currentSubarraySum = arrSizeSoFar * maxElementSoFar

            currSum = currentSubarraySum + self.helper(partitionIndex+1, arr, k, cache)
            if currSum > maxSum:
                maxSum = currSum

        cache[index] = maxSum
        return cache[index]

        