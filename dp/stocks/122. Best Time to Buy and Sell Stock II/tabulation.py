class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = [[0 for colIndex in range(2)] for rowIndex in range(len(prices)+1)]
        n = len(prices)
        
        for day in range(n-1, -1, -1):
            cache[day][1] = max(
                -prices[day] + cache[day+1][0],
                cache[day+1][1]
            )

            cache[day][0] = max(
                prices[day] + cache[day+1][1],
                cache[day+1][0]
            )

        return cache[0][1]