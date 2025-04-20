from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = [[[-1 for txnLeft in range(3)] for canBuy in range(2)] for index in range(len(prices)+1)]
        return self.helper(0, 1, 2, prices, cache)

    def helper(self, day:int, canBuy:int, transactionLeft:int, prices:list, cache) -> int:
        if day == len(prices):
            return 0

        if cache[day][canBuy][transactionLeft]!=-1:
            return cache[day][canBuy][transactionLeft]

        if canBuy==1:
            if transactionLeft == 0:
                cache[day][canBuy][transactionLeft] = 0
            else:
                cache[day][canBuy][transactionLeft] = max(
                    -prices[day] + self.helper(day+1, 0, transactionLeft, prices,cache),
                    self.helper(day+1, 1, transactionLeft, prices,cache)
                )
        else:
            cache[day][canBuy][transactionLeft] = max(
                prices[day] + self.helper(day+1, 1, transactionLeft-1, prices,cache), 
                self.helper(day+1, 0, transactionLeft, prices,cache)
            )
        
        return cache[day][canBuy][transactionLeft]