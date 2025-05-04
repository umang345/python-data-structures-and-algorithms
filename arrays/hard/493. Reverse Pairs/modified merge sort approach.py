from typing import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.helper(nums,0,len(nums)-1)

    def helper(self,nums: List[int], start:int, end:int) -> int:

        if start>=end:
            return 0

        mid = start + (end-start)//2

        leftSubArrayCount = self.helper(nums, start, mid)
        rightSubArrayCount = self.helper(nums, mid+1, end)

        currCount = 0
        index1, index2 = start, mid+1
        while index1<=mid and index2<=end:
            if nums[index1] > 2*nums[index2]:
                currCount+=(mid-index1+1)
                index2+=1
            else:
                index1+=1
        
        temp = [-1]*(end-start+1)
        tempIndex,index1, index2 = 0,start,mid+1

        while index1<=mid and index2<=end:
            if nums[index1]<=nums[index2]:
                temp[tempIndex] = nums[index1]
                index1+=1
            else:
                temp[tempIndex] = nums[index2]
                index2+=1
            tempIndex+=1
        
        while index1<=mid:
            temp[tempIndex] = nums[index1]
            index1+=1
            tempIndex+=1
        
        while index2<=end:
            temp[tempIndex] = nums[index2]
            index2+=1
            tempIndex+=1

        for index in range(start, end+1):
            nums[index] = temp[index-start]
        
        return currCount + leftSubArrayCount + rightSubArrayCount

'''
TC ->  O(nlogn)
SC ->  O(n)
'''