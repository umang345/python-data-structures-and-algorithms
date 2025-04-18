from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    cache = [0 for avl in range(w+1)]

    for rowIndex in range(1, n+1):
        currentRes = [0 for avl in range(w+1)]
        for weightAvl in range(w+1):

            if weight[rowIndex-1] > weightAvl:
                currentRes[weightAvl] = cache[weightAvl]
            else:
                currentRes[weightAvl] = max(
                    currentRes[weightAvl-weight[rowIndex-1]] + profit[rowIndex-1],
                    cache[weightAvl]
                )
        for cacheIndex in range(w+1):
            cache[cacheIndex] = currentRes[cacheIndex]

    return cache[w]