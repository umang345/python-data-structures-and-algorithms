class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hashSet = set([number for number in range(0, len(nums)+1)])
        for number in nums:
            hashSet.remove(number)

        iterable = iter(hashSet)
        return next(iterable)