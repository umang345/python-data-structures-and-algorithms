class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = [[-1 for last in range(len(nums)+1)] for curr in range(len(nums)+1)]
        return self.helper(0, -1, nums, cache)

    def helper(self, index:int, lastPickedIndex:int, nums:list, cache:list) -> int:
        if index == len(nums):
            return 0
        
        if cache[index][lastPickedIndex]!=-1:
            return cache[index][lastPickedIndex]

        if lastPickedIndex == -1 or nums[index] > nums[lastPickedIndex]:
            cache[index][lastPickedIndex] = max(
                1+self.helper(index+1, index, nums, cache),
                self.helper(index+1, lastPickedIndex, nums, cache)
            )
        else:
            cache[index][lastPickedIndex] = self.helper(index+1, lastPickedIndex, nums, cache)

        return cache[index][lastPickedIndex]
                