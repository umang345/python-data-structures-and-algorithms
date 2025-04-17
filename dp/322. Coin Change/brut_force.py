class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.helper(len(coins)-1,amount, coins)

    def helper(self, index, amount,coins) -> int:
        if amount == 0:
            return 0
        if index < 0:
            return -1

        if coins[index] > amount:
            return self.helper(index-1, amount, coins)
        else:
            includedResult = self.helper(index, amount-coins[index], coins)
            excludedResult = self.helper(index-1, amount, coins)
            if includedResult == -1:
                return excludedResult
            if excludedResult == -1:
                return includedResult+1
            return min(includedResult+1, excludedResult)