from typing import *
from math import *

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1, count1 = inf,0
        element2, count2 = inf,0

        for num in nums:
            if count1==0 and num!=element2:
                element1 = num
                count1+=1
            elif count2==0 and num!=element1:
                element2 = num
                count2+=1
            elif element1==num:
                count1+=1
            elif element2==num:
                count2+=1
            else:
                count1-=1
                count2-=1

        count1,count2 = 0,0
        for num in nums:
            if num == element1:
                count1+=1
            if num == element2:
                count2+=1
        n = len(nums)
        result = []
        if count1 > (n//3):
            result.append(element1)
        if count2 > (n//3):
            result.append(element2)
        
        return result