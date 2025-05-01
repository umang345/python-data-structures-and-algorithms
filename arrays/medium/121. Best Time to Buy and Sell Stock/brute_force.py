class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buyDay in range(0, len(prices)-1):
            for sellDay in range(buyDay+1, len(prices)):
                profit = prices[sellDay] - prices[buyDay]
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit