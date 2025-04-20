class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cache = [[-1 for canBuy in range(2)] for day in range(len(prices)+1)]
        return self.helper(0, 1, prices, cache)

    def helper(self, day:int, canBuy:int, prices: list, cache:list) -> int:
        if day >= len(prices):
            return 0

        if cache[day][canBuy] != -1:
            return cache[day][canBuy]

        if canBuy==1:
            cache[day][canBuy] = max(
                -prices[day] + self.helper(day+1, 0, prices, cache),
                self.helper(day+1, 1, prices, cache)
            )
        else:
            cache[day][canBuy] = max(
                prices[day] + self.helper(day+2, 1, prices, cache),
                self.helper(day+1, 0, prices, cache)
            )
        
        return cache[day][canBuy]
