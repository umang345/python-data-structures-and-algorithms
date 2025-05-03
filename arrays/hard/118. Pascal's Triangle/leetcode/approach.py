from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]

        1) 1 added by default
        2) if numRow > 1, 1 added at end by default
        3) No. of elements in each row = index of that row
        4) for numRow > 1, all element other than 1st and last
        a[i][j] = a[i-1][j-1]+a[i-1][j]
        '''
        result = list()
        result.append([1])
        if numRows == 1:
            return result

        for index in range(2,numRows+1):
            currRow = [1]
            for rowIndex in range(1,index-1):
                currRow.append(result[-1][rowIndex-1] + result[-1][rowIndex])
            
            currRow.append(1)
            result.append(currRow)
        
        return result
