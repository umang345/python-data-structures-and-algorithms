class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        cache = [[-1 for amt in range(amount+1)] for index in range(len(coins))]
        return self.helper(len(coins)-1, amount, coins, cache)

    def helper(self, index:int, amount:int, coins:list[int], cache:list) -> int:
        if amount == 0:
            return 1
        
        if index < 0:
            return 0

        if cache[index][amount]!=-1:
            return cache[index][amount]

        if coins[index] > amount :
            cache[index][amount] = self.helper(index-1, amount,coins,cache)
        else:
            cache[index][amount] = self.helper(index, amount-coins[index], coins, cache) + self.helper(index-1, amount, coins, cache)
        
        return cache[index][amount]