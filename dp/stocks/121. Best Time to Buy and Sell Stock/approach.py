from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyAt = 0

        for day in range(1, len(prices)):
            currentProfit = prices[day] - prices[buyAt]
            maxProfit = max(maxProfit, currentProfit)
            if prices[day] < prices[buyAt]:
                buyAt = day

        return maxProfit
    