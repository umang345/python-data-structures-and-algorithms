class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(len(nums)-1, nums, [-1]*(len(nums)+1))

    def helper(self, index, nums, dp) -> int:
        if index == 0:
            return nums[0]
        if index == 1:
            return max(nums[0], nums[1])

        if dp[index]!=-1:
            return dp[index]

        currentElementPicked = nums[index] + self.helper(index-2, nums,dp)
        currentElementNotPicked = self.helper(index-1,nums,dp)

        dp[index] = max(currentElementPicked, currentElementNotPicked)
        return dp[index]