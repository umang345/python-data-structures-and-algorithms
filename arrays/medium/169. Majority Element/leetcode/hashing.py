class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        hash = dict()
        minFreq = (len(nums)//2)+1

        for num in nums:
            hash[num] = hash.get(num,0)+1
            if hash[num] >= minFreq:
                return num
            

'''
TC -> O(n)
SC -> O(n/2)
'''