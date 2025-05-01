class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)//2

        positiveNums = [0]*n
        negativeNums = [0]*n

        pIndex, nIndex = 0,0
        for num in nums:
            if num > 0:
                positiveNums[pIndex] = num
                pIndex+=1
            else:
                negativeNums[nIndex] = num
                nIndex+=1
        
        for index in range(0, len(nums), 2):
            nums[index] = positiveNums[(index//2)]
            nums[index+1] = negativeNums[(index//2)]

        return nums