from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(0, 1, 2, prices)

    def helper(self, day:int, canBuy:int, transactionLeft:int, prices:list) -> int:
        if day == len(prices):
            return 0

        if canBuy==1:
            if transactionLeft == 0:
                return 0
            else:
                return max(
                    -prices[day] + self.helper(day+1, 0, transactionLeft, prices),
                    self.helper(day+1, 1, transactionLeft, prices)
                )
        else:
            return max(
                prices[day] + self.helper(day+1, 1, transactionLeft-1, prices), 
                self.helper(day+1, 0, transactionLeft, prices)
            )