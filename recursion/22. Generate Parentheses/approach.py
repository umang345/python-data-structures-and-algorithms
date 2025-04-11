class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        currentStr = list()

        self.generateParenthesisHelper(n,n, currentStr, result) 
        return result

    def generateParenthesisHelper(self, openingCount:int, closingCount:int,currentStr:List[str], result:List[str]):
        if openingCount == 0 and closingCount == 0:
            result.append("".join(currentStr))
            return

        if openingCount > closingCount:
            return 
        
        if openingCount>0:
            currentStr.append("(")
            self.generateParenthesisHelper(openingCount-1, closingCount, currentStr, result)
            currentStr.pop()

        currentStr.append(")")
        self.generateParenthesisHelper(openingCount, closingCount-1, currentStr, result)
        currentStr.pop()
        return