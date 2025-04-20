class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        return self.helper(0,1,fee, prices)

    def helper(self, day:int, canBuy:int, fee:int, prices:list) -> int:
        if day == len(prices):
            return 0

        if canBuy == 1:
            return max(
                -prices[day] + self.helper(day+1, 0, fee, prices), 
                self.helper(day+1, 1, fee, prices)
            )
        else:
            return max(
                prices[day] - fee + self.helper(day+1, 1, fee, prices),
                self.helper(day+1, 0, fee, prices)
            )