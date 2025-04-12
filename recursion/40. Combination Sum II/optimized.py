class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        currSet = list()
        self.combinationSumHelper(0, sorted(candidates), target, currSet, result)

        return result
        

    def combinationSumHelper(self, index, candidates, target, currSet, result:list[list[int]]):
        if target == 0:
            result.append([num for num in currSet])
            return
        if index>=len(candidates) or target<0:
            return

        for currI in range(index, len(candidates)):
            if target < candidates[currI]:
                break
            if currI!=index and candidates[currI]==candidates[currI-1]:
                continue
            currSet.append(candidates[currI])
            self.combinationSumHelper(currI+1, candidates, target - candidates[currI], currSet, result)
            currSet.pop()