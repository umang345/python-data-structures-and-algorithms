from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(0, True, prices)

    def helper(self, index:int, canBuy:bool, prices:list) -> int:
        if index == len(prices):
            return 0

        if canBuy:
            return max(
                -prices[index]+self.helper(index+1, False, prices),
                self.helper(index+1, True, prices)
            )
        else:
            return max(
                prices[index]+self.helper(index+1, True, prices),
                self.helper(index+1, False, prices)
            )