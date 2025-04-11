class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        currentSet, result = list(), list()
        self.combinationSumHelper(0, candidates, target, currentSet, result)
        return result
        

    def combinationSumHelper(self, index:int, candidates: List[int], target:int,currentSet:List[int], result: List[List[int]]):

        if target == 0:
            result.append([number for number in currentSet])
            return
        
        if target<0 or index >= len(candidates):
            return

        if candidates[index]>target:
            self.combinationSumHelper(index+1, candidates, target, currentSet, result)
        else:
            currentSet.append(candidates[index])
            self.combinationSumHelper(index, candidates, target-candidates[index], currentSet, result)
            currentSet.pop()
            self.combinationSumHelper(index+1, candidates, target, currentSet, result)