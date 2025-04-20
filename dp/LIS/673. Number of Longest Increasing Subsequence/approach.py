class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        
        dp = [1 for index in range(len(nums))]
        count = [1 for index in range(len(nums))]

        lisLen = 0

        for index in range(len(nums)):
            for compare in range(index):
                if nums[index]>nums[compare]:
                    
                    if dp[index] < 1 + dp[compare]:
                        dp[index] = 1+dp[compare]
                        count[index]=count[compare]
                    elif dp[index] == 1+dp[compare]:
                        count[index]+=count[compare]
                        
                        
            
            if lisLen < dp[index]:
                lisLen = dp[index]
        
        aggregate = 0
        for index, value in enumerate(count):
            if dp[index] == lisLen:
                aggregate+=value 
        return aggregate