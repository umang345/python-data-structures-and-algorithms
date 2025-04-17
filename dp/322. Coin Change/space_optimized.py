from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = [-1 for val in range(amount+1)]
        cache[0]=0

        for rowIndex in range(1, len(coins)+1):
            currentRes = [-1 for val in range(amount+1)]
            currentRes[0] = 0
            for amt in range(1, amount+1):

                if coins[rowIndex-1] > amt:
                    currentRes[amt] = cache[amt]
                else:
                    includedResult = currentRes[amt - coins[rowIndex-1]]
                    excludedResult = cache[amt]
                    if includedResult == -1:
                        currentRes[amt] = excludedResult
                    elif excludedResult ==-1:
                        currentRes[amt] = 1 + includedResult
                    else:
                        currentRes[amt] = min(1 + includedResult, excludedResult)

            for amt in range(1, amount+1):
                cache[amt] = currentRes[amt]

        return cache[amount]