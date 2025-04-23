class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        return self.helper(0, arr, k)

    def helper(self, index, arr, k) -> int:
        if index >= len(arr) or k==0:
            return 0

        maxSum = 0
        maxElementSoFar = None
        arrSizeSoFar = 0
        for partitionIndex in range(index, min(index+k, len(arr))):
            arrSizeSoFar+=1
            if maxElementSoFar is None or maxElementSoFar < arr[partitionIndex]:
                maxElementSoFar = arr[partitionIndex]
            currentSubarraySum = arrSizeSoFar * maxElementSoFar

            currSum = currentSubarraySum + self.helper(partitionIndex+1, arr, k)
            if currSum > maxSum:
                maxSum = currSum

        return maxSum

        