from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = [[-1 for colIndex in range(2)] for rowIndex in range(len(prices)+1)]
        return self.helper(0, True, prices, cache)

    def helper(self, index:int, canBuy:int, prices:list, cache:list) -> int:
        if index == len(prices):
            return 0

        if cache[index][canBuy] != -1:
            return cache[index][canBuy]

        if canBuy==1:
            cache[index][canBuy] = max(
                -prices[index]+self.helper(index+1, 0, prices, cache),
                self.helper(index+1, 1, prices, cache)
            )
        else:
            cache[index][canBuy] = max(
                prices[index]+self.helper(index+1, 1, prices, cache),
                self.helper(index+1, 0, prices, cache)
            )

        return cache[index][canBuy]