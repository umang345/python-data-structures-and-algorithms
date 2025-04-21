class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        return self.helper(-1, len(nums), nums)

    def helper(self,start, end, nums) -> int:
        if end-start<=1:
            return 0

        maxCoins = 0
        for index in range(start+1, end):
            leftNeighbour = 1 if start<0 else nums[start]
            rightNeighbour = 1 if end>=len(nums) else nums[end]
            burst =  leftNeighbour * rightNeighbour * nums[index]
            currCoins = burst + self.helper(start, index, nums) + self.helper(index, end, nums)
            if maxCoins < currCoins:
                maxCoins = currCoins

        return maxCoins