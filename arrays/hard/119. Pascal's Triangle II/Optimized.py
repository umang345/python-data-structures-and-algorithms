# The follow up is to use only O(numRows) extra space

from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]*(rowIndex+1)
        if rowIndex == 0:
            return result
        
        for index in range(1,rowIndex+1):
            
            for rowIndex in range(index-1, 0, -1):
                result[rowIndex] = (result[rowIndex-1]+result[rowIndex])
        
        return result
