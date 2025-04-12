class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        currentSet, result = list(), set()
        self.combinationSumHelper(0, sorted(candidates), target, currentSet, result)
        return [list(t) for t in result]

    def combinationSumHelper(self, index:int, candidates:List[int], target:int, currentSet:List[int], result: set[tuple[int,...]]):

        if target == 0:
            currentTupleToCheck = tuple(currentSet)
            if not currentTupleToCheck in result:
                result.add(currentTupleToCheck)
            return 
        
        if index >= len(candidates):
            return

        if candidates[index]>target:
            self.combinationSumHelper(index+1, candidates, target, currentSet, result)
        else:
            currentSet.append(candidates[index])
            self.combinationSumHelper(index+1, candidates, target - candidates[index], currentSet, result)
            currentSet.pop()
            self.combinationSumHelper(index+1, candidates, target, currentSet, result)

    
        