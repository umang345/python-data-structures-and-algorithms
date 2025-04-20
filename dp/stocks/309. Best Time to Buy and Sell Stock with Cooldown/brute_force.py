class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.helper(0, 1, prices)

    def helper(self, day:int, canBuy:int, prices: list) -> int:
        if day >= len(prices):
            return 0

        if canBuy==1:
            return max(
                -prices[day] + self.helper(day+1, 0, prices),
                self.helper(day+1, 1, prices)
            )
        else:
            return max(
                prices[day] + self.helper(day+2, 1, prices),
                self.helper(day+1, 0, prices)
            )
