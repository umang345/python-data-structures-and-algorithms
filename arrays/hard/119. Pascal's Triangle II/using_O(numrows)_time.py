# Challenge is to use only O(rowIndex) time
from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        

        '''
        0C0
        1C0   1C1
        2C0   2C1  2C2
        3C0   3C1  3C2  3C3

        4C0   4C1   4C2   4C3

        1     1*4    4*3   4*3*2
        1     1*1    1*2   1*2*3
        '''
        result = [1]
        numer, deno = 1,1
        n,r = rowIndex,1
        for index in range(1, rowIndex+1):
            numer*=(n)
            deno*=(r)
            n-=1
            r+=1
            result.append(numer//deno)
        
        return result
