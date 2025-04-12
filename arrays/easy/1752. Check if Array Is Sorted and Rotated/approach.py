class Solution:
    def check(self, nums: List[int]) -> bool:
        '''
        []   -> T
        [1,5,3,6,2]  -> F
        [1,2,4,5,8]  -> T
        [4,5,7,1,2]  -> T
        [1,2,3,3,4]  -> T
        [3,4,1,2,3]  -> T
        '''

        dipFound:bool = False 
        minElement = -1

        for index, element in enumerate(nums):
            if index == 0:
                minElement = element
                continue
            
            if element < nums[index-1]:
                return self.checkForSortedAndLessThanEqualToK(index, nums, minElement)
                    

        return True

    def checkForSortedAndLessThanEqualToK(self, indexToStart:int,nums:list[int], minElement:int) -> bool :
        if indexToStart >= len(nums):
            return True

        if nums[indexToStart] > minElement:
            return False

        for index in range(indexToStart+1, len(nums)):
            if nums[index]<nums[index-1] or nums[index]>minElement:
                return False

        return True
    

        