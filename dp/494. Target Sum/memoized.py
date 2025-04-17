class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        return self.helper(len(nums)-1, 0, target, nums, dict())

    def helper(self, index:int, currentValue:int, target:int, nums:list[int], cache:dict) -> int:
        if index < 0:
            if currentValue == target:
                return 1
            return 0

        key = f"{index}-{currentValue}"
        if not cache.get(key) is None:
            return cache[key]

        cache[key] = self.helper(index-1, currentValue-nums[index], target, nums, cache) + self.helper(index-1, currentValue+nums[index], target, nums, cache)

        return cache[key]