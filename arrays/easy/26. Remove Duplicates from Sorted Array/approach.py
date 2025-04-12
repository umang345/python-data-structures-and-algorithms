class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        currentIndex, traversalIndex = 0,0

        while traversalIndex < len(nums):
            if nums[currentIndex]==nums[traversalIndex]:
                traversalIndex+=1
                continue
        
            currentIndex+=1
            nums[currentIndex] = nums[traversalIndex]
            
        return currentIndex+1
        