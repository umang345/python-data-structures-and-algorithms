class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        [1,1,0,1,1,1]


        [0,0,0,0,1,1,0,1]
        '''
        maxOnes = 0
        start,traversal = 0,0
        while traversal<len(nums):
            if nums[traversal] == 1:
                if nums[start]==0:
                    start = traversal
                else:
                    traversal+=1
            else:
                currentOnesCount = traversal - start
                if maxOnes < currentOnesCount:
                    maxOnes = currentOnesCount
                traversal+=1
                start = traversal
        
        currentOnesCount = traversal - start
        if maxOnes < currentOnesCount:
            maxOnes = currentOnesCount
        
        return maxOnes