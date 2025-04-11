class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currentSet, result = list(), list()
        self.generateSubsets(0, nums, currentSet, result)
        return result

    def generateSubsets(self, index:int, nums: List[int], currentSet: List[int], result: List[List[int]]):
        if index >= len(nums):
            result.append([number for number in currentSet])
            return 

        currentSet.append(nums[index])
        self.generateSubsets(index+1, nums, currentSet, result)
        currentSet.pop()
        self.generateSubsets(index+1, nums, currentSet, result)
    