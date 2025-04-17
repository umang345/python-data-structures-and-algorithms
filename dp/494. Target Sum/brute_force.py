class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(len(nums)-1, target, nums)

    def helper(self, index, target, nums) -> int:
        if index<0:
            if target==0:
                return 1
            return 0
        
        return self.helper(index-1, target-nums[index], nums) + self.helper(index-1, target+nums[index], nums)