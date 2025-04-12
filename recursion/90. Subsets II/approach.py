class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result, currSet = set(), list()
        self.subsetHelper(0, sorted(nums), currSet, result)
        return [list(tpl) for tpl in result]
    
    def subsetHelper(self,index:int, nums: list[int], currSet:list[int],result:set[tuple[int]]):
        if index == len(nums):
            currTuple = tuple(currSet)
            if not currTuple in result:
                result.add(currTuple)
            return

        for currI in range(index, len(nums)):
            if currI != index and nums[currI]!=nums[currI-1]:
                continue
            currSet.append(nums[currI])
            self.subsetHelper(currI+1, nums, currSet, result)
            currSet.pop()

        self.subsetHelper(index+1, nums, currSet, result)

            