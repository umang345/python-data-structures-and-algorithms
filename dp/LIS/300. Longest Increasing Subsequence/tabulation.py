class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = [[0 for last in range(len(nums)+1)] for curr in range(len(nums)+1)]

        for index in range(len(nums)-1, -1,-1):
            for lastPicked in range(-1, len(nums)-1):
                if lastPicked == -1 or nums[index] > nums[lastPicked]:
                    cache[index][lastPicked] = max(
                        1 + cache[index+1][index],
                        cache[index+1][lastPicked]
                    )
                else:
                    cache[index][lastPicked] = cache[index+1][lastPicked] 

        return cache[0][-1]