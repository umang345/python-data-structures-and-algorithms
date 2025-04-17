class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cache = [[-2 for val in range(amount+1)] for index in range(len(coins))]
        return self.helper(len(coins)-1,amount, coins, cache)

    def helper(self, index, amount,coins, cache:list[int]) -> int:
        if amount == 0:
            return 0
        if index < 0:
            return -1

        if cache[index][amount]!=-2:
            return cache[index][amount]

        if coins[index] > amount:
             cache[index][amount] = self.helper(index-1, amount, coins,cache)
             return cache[index][amount]
        else:
            includedResult = self.helper(index, amount-coins[index], coins,cache)
            excludedResult = self.helper(index-1, amount, coins,cache)
            if includedResult == -1:
                cache[index][amount] = excludedResult
            elif excludedResult == -1:
                cache[index][amount] = includedResult+1
            else:
                cache[index][amount] = min(includedResult+1, excludedResult)

            return cache[index][amount]