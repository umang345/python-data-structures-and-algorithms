class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        minFreq = (len(nums)//2) + 1
        for num in nums:
            currFreq = 0
            for numToCheck in nums:
                if numToCheck == num:
                    currFreq+=1
            if currFreq >= minFreq:
                return num
            

'''
TC -> O(n^2)
SC -> O(1)
'''