class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cache = [[0 for canBuy in range(2)] for day in range(len(prices)+1)]
        
        for day in range(len(prices)-1,-1,-1):
            for canBuy in range(2):
                if canBuy == 1:
                    cache[day][canBuy] = max(
                        -prices[day] + cache[day+1][0],
                        cache[day+1][1]
                    )
                else:
                    cache[day][canBuy] = max(
                        prices[day] - fee + cache[day+1][1],
                        cache[day+1][0]
                    )
        
        return cache[0][1]