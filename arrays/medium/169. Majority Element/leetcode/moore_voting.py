class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        currMajorityElement = -1
        count = 0

        for num in nums:
            if count == 0:
                currMajorityElement = num
                count = 1
            else:
                if num == currMajorityElement:
                    count+=1
                else:
                    count-=1
        
        return currMajorityElement 
    

'''
TC ->  O(n)
SC ->  O(1)
'''