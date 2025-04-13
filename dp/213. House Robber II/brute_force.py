class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        return max(
            self.helper(len(nums)-2, nums, 0),
            self.helper(len(nums)-1, nums,1)
        )


    def helper(self, index, nums, startIndex) -> int:
        if index < startIndex:
            return 0
        if index == startIndex:
            return nums[index]
        if index == startIndex+1:
            return max(nums[index], nums[index-1])

        sumIfCurrentSelected = self.helper(index-2, nums, startIndex) + nums[index]
        sumIfCurrentNotSelected = self.helper(index-1, nums, startIndex)
        return max(sumIfCurrentSelected, sumIfCurrentNotSelected)