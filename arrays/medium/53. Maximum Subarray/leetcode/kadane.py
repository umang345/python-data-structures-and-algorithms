class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = None
        currSum = 0

        for num in nums:
            currSum+=num
            
            if currSum < num:
                currSum = num


            if maxSum is None or maxSum < currSum:
                maxSum = currSum
        
        return maxSum
    

'''
TC -> O(n)
SC -> O(1)
'''
        