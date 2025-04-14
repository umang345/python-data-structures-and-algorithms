class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumOfElements = reduce(lambda acc,x : acc+x, nums,0)
        if sumOfElements%2!=0:
            return False

        return self.helper(0, sumOfElements/2, nums)

    def helper(self, index, target, nums):
        if target == 0:
            return True

        if index >= len(nums):
            return False

        if nums[index]>target:
            return self.helper(index+1, target, nums)
        else:
            return self.helper(index+1, target-nums[index], nums) or self.helper(index+1, target, nums)