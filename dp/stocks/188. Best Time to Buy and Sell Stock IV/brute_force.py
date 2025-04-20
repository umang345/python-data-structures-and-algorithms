class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        return self.helper(0,1,k, prices)

    def helper(self, day:int, canBuy:int, txnLeft:int, prices:int) -> int:
        if day == len(prices):
            return 0

        if canBuy == 1:
            if txnLeft == 0:
                return 0
            else:
                return max(
                    -prices[day] + self.helper(day+1, 0, txnLeft, prices),
                    self.helper(day+1, 1, txnLeft, prices)
                )
        else:
            return max(
                prices[day] + self.helper(day+1, 1, txnLeft-1, prices),
                self.helper(day+1, 0, txnLeft, prices)
            )