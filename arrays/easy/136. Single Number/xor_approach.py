class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda acc, x: acc ^ x, nums,0)
