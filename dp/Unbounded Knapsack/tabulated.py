from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    cache = [[-1 for avl in range(w+1)] for index in range(n+1)]
    
    for wAvl in range(w+1):
        cache[0][wAvl] = 0

    for rowIndex in range(1, n+1):
        for weightAvl in range(w+1):

            if weight[rowIndex-1] > weightAvl:
                cache[rowIndex][weightAvl] = cache[rowIndex-1][weightAvl]
            else:
                cache[rowIndex][weightAvl] = max(
                    cache[rowIndex][weightAvl-weight[rowIndex-1]] + profit[rowIndex-1],
                    cache[rowIndex-1][weightAvl]
                )

    return cache[n][w]