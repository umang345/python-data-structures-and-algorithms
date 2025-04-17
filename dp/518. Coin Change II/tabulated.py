class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        cache = [[0 for amt in range(amount+1)] for index in range(len(coins)+1)]

        for rowIndex in range(len(coins)+1):
            cache[rowIndex][0] = 1

        for rowIndex in range(1, len(coins)+1):
            for amt in range(1, amount+1):

                if coins[rowIndex-1] > amt:
                    cache[rowIndex][amt] = cache[rowIndex-1][amt]
                else:
                    cache[rowIndex][amt] = cache[rowIndex][amt - coins[rowIndex-1]] + cache[rowIndex-1][amt]
        
        return cache[len(coins)][amount]