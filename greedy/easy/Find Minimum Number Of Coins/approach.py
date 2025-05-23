from typing import *

def MinimumCoins(n: int) -> List[int]:
    
    coins = [1000, 500, 100, 50, 20, 10, 5,2,1]

    result,coinIndex = [],0
    amount = n

    while amount>0 and coinIndex < len(coins):

        count = amount//coins[coinIndex]
        amount = amount%coins[coinIndex]
        for c in range(count):
            result.append(coins[coinIndex])
        coinIndex+=1

    return result