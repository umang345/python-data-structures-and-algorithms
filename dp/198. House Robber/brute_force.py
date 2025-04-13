class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(len(nums)-1, nums)

    def helper(self, index, nums) -> int:
        if index == 0:
            return nums[0]
        if index == 1:
            return max(nums[0], nums[1])

        currentElementPicked = nums[index] + self.helper(index-2, nums)
        currentElementNotPicked = self.helper(index-1,nums)

        return max(currentElementPicked, currentElementNotPicked)
        