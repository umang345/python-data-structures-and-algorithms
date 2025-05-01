class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyDay = 0
        maxProfit = 0
        for day in range(1, len(prices)):
            profit = prices[day] - prices[buyDay]
            if profit > maxProfit:
                maxProfit = profit

            if prices[day] < prices[buyDay]:
                buyDay = day

        return maxProfit