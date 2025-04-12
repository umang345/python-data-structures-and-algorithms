class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2:['a','b','c',],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }
        result, currSet = list(), list()

        self.helper(0, digits, currSet, result, mapping)
        return result

    def helper(self, index:int, digits, currSet:list[int], result:list[str], mapping:dict):

        if index >= len(digits) :
            if len(currSet)>0:
                result.append("".join(currSet))
            return
        
        digit = int(digits[index])
        for char in mapping[digit]:
            currSet.append(char)
            self.helper(index+1, digits, currSet, result, mapping)
            currSet.pop()
        
