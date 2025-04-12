class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        [1,3,0,0,12]

        [   1  , 3   ,   12   ,  0    ,   0   ]
        
        [1,3,12,0,0]
        '''
        currentIndex, traversalIndex = 0,0

        while traversalIndex < len(nums):
            if nums[traversalIndex]!=0:
                nums[currentIndex], nums[traversalIndex] = nums[traversalIndex], nums[currentIndex]
                currentIndex+=1
            
            traversalIndex+=1
        
        