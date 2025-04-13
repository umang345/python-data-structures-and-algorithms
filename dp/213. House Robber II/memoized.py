class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        return max(
            self.helper(len(nums)-2, nums, 0, [-1]*(len(nums))),
            self.helper(len(nums)-1, nums,1, [-1]*(len(nums)))
        )


    def helper(self, index, nums, startIndex, dp) -> int:
        if index < startIndex:
            return 0
        if index == startIndex:
            return nums[index]
        if index == startIndex+1:
            return max(nums[index], nums[index-1])

        if dp[index]!=-1:
            return dp[index]
        sumIfCurrentSelected = self.helper(index-2, nums, startIndex,dp) + nums[index]
        sumIfCurrentNotSelected = self.helper(index-1, nums, startIndex,dp)
        dp[index] =  max(sumIfCurrentSelected, sumIfCurrentNotSelected) 
        return dp[index]