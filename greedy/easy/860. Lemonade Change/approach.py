from typing import *

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        c5, c10, c20 = 0,0,0
        count = 0

        for bill in bills:
            if bill == 5:
                c5+=1
                count+=1
            elif bill == 10:
                if c5>0:
                    c10+=1
                    c5-=1
                    count+=1
                else:
                    break
            else:
                if c5>0 and c10>0:
                    c10-=1
                    c5-=1
                    c20+=1
                    count+=1
                elif c5>2:
                    c5-=3
                    c20+=1
                    count+=1
                else:
                    break
        
        return count==len(bills)