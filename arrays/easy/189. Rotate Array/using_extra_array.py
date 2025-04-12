class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%(len(nums))

        copyArray = [0]*len(nums)
        copyIndex = 0
        for index in range(len(nums)-k, len(nums)):
            copyArray[copyIndex] = nums[index]
            copyIndex+=1

        for index in range(len(nums)-k):
            copyArray[copyIndex] = nums[index]
            copyIndex+=1

        for index in range(len(nums)):
            nums[index] = copyArray[index]

