class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for index in range(2, len(nums)):
            computed = max(nums[index] + prev, curr)
            prev = curr
            curr = computed

        return curr