from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = [[-1 for val in range(amount+1)] for index in range(len(coins)+1)]
        for rowIndex in range(len(coins)+1):
            cache[rowIndex][0] = 0

        for rowIndex in range(1, len(coins)+1):
            for amt in range(1, amount+1):

                if coins[rowIndex-1] > amt:
                    cache[rowIndex][amt] = cache[rowIndex-1][amt]
                else:
                    includedResult = cache[rowIndex][amt - coins[rowIndex-1]]
                    excludedResult = cache[rowIndex-1][amt]
                    if includedResult == -1:
                        cache[rowIndex][amt] = excludedResult
                    elif excludedResult ==-1:
                        cache[rowIndex][amt] = 1 + includedResult
                    else:
                        cache[rowIndex][amt] = min(1 + includedResult, excludedResult)

        return cache[len(coins)][amount]