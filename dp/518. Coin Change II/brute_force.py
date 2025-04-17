class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        return self.helper(len(coins)-1, amount, coins)

    def helper(self, index:int, amount:int, coins:list[int]) -> int:
        if amount == 0:
            return 1
        
        if index < 0:
            return 0

        if coins[index] > amount :
            return self.helper(index-1, amount,coins)
        else:
            return self.helper(index, amount-coins[index], coins) + self.helper(index-1, amount, coins)