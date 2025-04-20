class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        return self.helper(0, -1, nums)

    def helper(self, index:int, lastPickedIndex:int, nums:list) -> int:
        if index == len(nums):
            return 0

        if lastPickedIndex == -1 or nums[index] > nums[lastPickedIndex]:
            return max(
                1+self.helper(index+1, index, nums),
                self.helper(index+1, lastPickedIndex, nums)
            )
        else:
            return self.helper(index+1, lastPickedIndex, nums)
                
        