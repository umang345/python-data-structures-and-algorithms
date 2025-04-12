class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = list()
        currSet = list()
        nums = [num for num in range(1,10)]
        self.combinationSumHelper(0, nums, k,n, 0, currSet, result)
        return result

    def combinationSumHelper(self, index, nums:list[int], k:int, targetSum:int,currSum:int, currSet:list[int] ,result:list[list[int]]):
        
        if len(currSet) == k :
            if currSum == targetSum:
                result.append([num for num in currSet])
            return 
        
        if len(currSet)>k or targetSum < currSum or index>=len(nums):
            return

        if nums[index] <= (targetSum-currSum):
            currSet.append(nums[index])
            self.combinationSumHelper(index+1, nums, k, targetSum, currSum+nums[index], currSet, result)
            currSet.pop()
        
        self.combinationSumHelper(index+1, nums, k, targetSum ,currSum, currSet, result)


