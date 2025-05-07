class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        result,start,end = len(nums),0,len(nums)-1

        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] >= target:
                result = mid
                end = mid-1
            else:
                start = mid+1

        return result