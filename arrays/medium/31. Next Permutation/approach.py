class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dipIndex = -1
        for index in range(len(nums)-2, -1, -1):
            if nums[index]<nums[index+1]:
                dipIndex = index
                break

        if dipIndex == -1:
            nums.reverse()
        else:
            swapIndex = -1
            for index in range(len(nums)-1, dipIndex, -1):
                if nums[index] > nums[dipIndex]:
                    nums[index], nums[dipIndex] = nums[dipIndex], nums[index]
                    break
            
            start, end = dipIndex+1, len(nums)-1

            while start<=end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        