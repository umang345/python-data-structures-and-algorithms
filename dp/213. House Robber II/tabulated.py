class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.helper(nums, 0, len(nums)-2),
            self.helper(nums, 1, len(nums)-1)
        )
    
    def helper(self, nums, startIndex, endIndex):
        if startIndex>endIndex:
            return 0
        if startIndex == endIndex:
            return nums[startIndex]
        if startIndex+1 == endIndex:
            return max(nums[startIndex], nums[endIndex])

        dp = [-1]*(len(nums))
        dp[startIndex] , dp[startIndex+1] = nums[startIndex] , max(nums[startIndex], nums[startIndex+1])

        for index in range(startIndex+2, endIndex+1):
            dp[index] = max(
                nums[index] + dp[index-2],
                dp[index-1]
            )

        return dp[endIndex]