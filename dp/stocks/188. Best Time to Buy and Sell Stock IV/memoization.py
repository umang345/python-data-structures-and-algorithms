class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        cache = [[[-1 for txnLeft in range(k+1)] for canBuy in range(2)] for day in range(len(prices))]
        return self.helper(0,1,k, prices, cache)

    def helper(self, day:int, canBuy:int, txnLeft:int, prices:int, cache:list) -> int:
        if day == len(prices):
            return 0

        if cache[day][canBuy][txnLeft] != -1:
            return cache[day][canBuy][txnLeft]

        if canBuy == 1:
            if txnLeft == 0:
                cache[day][canBuy][txnLeft] = 0
            else:
                cache[day][canBuy][txnLeft] = max(
                    -prices[day] + self.helper(day+1, 0, txnLeft, prices, cache),
                    self.helper(day+1, 1, txnLeft, prices, cache)
                )
        else:
            cache[day][canBuy][txnLeft] = max(
                prices[day] + self.helper(day+1, 1, txnLeft-1, prices, cache),
                self.helper(day+1, 0, txnLeft, prices, cache)
            )
        
        return cache[day][canBuy][txnLeft]