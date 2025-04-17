class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        cache = [0 for amt in range(amount+1)]

        for rowIndex in range(len(coins)+1):
            cache[0] = 1

        for rowIndex in range(1, len(coins)+1):
            currentVal = [0 for amt in range(amount+1)]
            currentVal[0] = 1
            for amt in range(1, amount+1):

                if coins[rowIndex-1] > amt:
                    currentVal[amt] = cache[amt]
                else:
                    currentVal[amt] = currentVal[amt - coins[rowIndex-1]] + cache[amt]

            for amt in range(1, amount+1):
                cache[amt] = currentVal[amt]
        
        return cache[amount]