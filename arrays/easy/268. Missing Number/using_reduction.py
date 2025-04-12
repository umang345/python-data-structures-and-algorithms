class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lengthOfArray = len(nums)
        sumOfFirstNNumbers = (lengthOfArray*(lengthOfArray+1))//2

        sumOfArrayElements = reduce(lambda acc, x : acc+x, nums, 0)
        return sumOfFirstNNumbers - sumOfArrayElements