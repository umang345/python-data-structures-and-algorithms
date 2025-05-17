from typing import *

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        f(n) = count of subarray with sum atmost goal 
        '''
        return self.numSubarrayWithSumAtmostGoal(nums, goal) - self.numSubarrayWithSumAtmostGoal(nums, goal-1)
    
    def numSubarrayWithSumAtmostGoal(self, nums:list, goal:int) -> int:
        count = 0
        
        start = 0
        currSum = 0
        for end in range(len(nums)):
            currSum+=nums[end]
            while currSum > goal and start<=end:
                currSum -= nums[start]
                start+=1
            count+=(end-start+1)
        return count