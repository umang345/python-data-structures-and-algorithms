class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = []
        for index in range(len(nums)):
            indexToUpdate = 1 + self.getIndexByBS(lis, nums[index])
            if indexToUpdate >= len(lis):
                lis.append(nums[index])
            else:
                lis[indexToUpdate] = nums[index]

        return len(lis)

    def getIndexByBS(self,arr:list, target:int) -> int:
        '''
        Find index of largest element less than the target
        '''
        start, end = 0, len(arr)-1
        result = -1
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] < target:
                result = mid
                start = mid+1
            elif arr[mid] > target:
                end = mid-1
            else:
                result = mid-1
                break
        
        return result