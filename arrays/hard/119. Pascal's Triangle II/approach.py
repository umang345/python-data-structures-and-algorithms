from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex == 0:
            return result
        
        for index in range(1,rowIndex+1):
            currRow = [1]
            for rowIndex in range(1,index):
                currRow.append(result[rowIndex-1]+result[rowIndex])
            currRow.append(1)
            result = currRow
        
        return result
