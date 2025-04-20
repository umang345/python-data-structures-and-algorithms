class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        cache = [[[0 for txnLeft in range(k+1)] for canBuy in range(2)] for day in range(len(prices)+1)]

        for day in range(len(prices)-1, -1, -1):
            for canBuy in range(2):
                for txnLeft in range(k+1):
                    if canBuy == 1:
                        if txnLeft == 0:
                            cache[day][canBuy][txnLeft] = 0
                        else:
                            cache[day][canBuy][txnLeft] = max(
                                -prices[day] + cache[day+1][0][txnLeft],
                                cache[day+1][1][txnLeft]
                            )
                    else:
                        cache[day][canBuy][txnLeft] = max(
                            prices[day] + cache[day+1][1][txnLeft-1],
                            cache[day+1][0][txnLeft]
                        )
        
        return cache[0][1][k]