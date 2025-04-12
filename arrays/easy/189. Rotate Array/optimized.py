class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,2,3,4,5,6,7]
        [4,3,2,1,7,6,5]
        [5,6,7,1,2,3,4]
        [5,6,7,1,2,3,4]
        """
        k = k%(len(nums))
        self.reverseBetweenIndexs(nums, 0, len(nums)-k-1)
        self.reverseBetweenIndexs(nums, len(nums)-k, len(nums)-1)
        self.reverseBetweenIndexs(nums, 0, len(nums)-1)
        

    def reverseBetweenIndexs(self, nums:list[int], startIndex:int, endIndex:int) -> None:
        while startIndex<=endIndex:
            nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
            startIndex+=1
            endIndex-=1


        