class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        cache = [[-1 for col in range(len(nums)+2)] for row in range(len(nums)+2)]
        return self.helper(-1, len(nums), nums, cache)

    def helper(self,start, end, nums,cache) -> int:
        if end-start<=1:
            return 0

        if cache[start+1][end+1]!=-1:
            return cache[start+1][end+1]

        maxCoins = 0
        for index in range(start+1, end):
            leftNeighbour = 1 if start<0 else nums[start]
            rightNeighbour = 1 if end>=len(nums) else nums[end]
            burst =  leftNeighbour * rightNeighbour * nums[index]
            currCoins = burst + self.helper(start, index, nums,cache) + self.helper(index, end, nums,cache)
            if maxCoins < currCoins:
                maxCoins = currCoins

        cache[start+1][end+1] = maxCoins
        return cache[start+1][end+1]