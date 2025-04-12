class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        '''
        [1,1,0,1,1,1]
        '''

        maxOnes = 0
        for startIndex in range(len(nums)):
            if nums[startIndex]==1:
                currentCount = 0
                for currentIndex in range(startIndex, len(nums)):
                    if nums[currentIndex]==0:
                        break
                    currentCount+=1

                if maxOnes < currentCount:
                    maxOnes = currentCount
        return maxOnes