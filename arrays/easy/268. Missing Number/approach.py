class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lengthOfArray = len(nums)
        sumOfFirstNNumbers = (lengthOfArray*(lengthOfArray+1))//2

        sumOfArrayElements = 0
        for num in nums:
            sumOfArrayElements+=num

        return  sumOfFirstNNumbers - sumOfArrayElements