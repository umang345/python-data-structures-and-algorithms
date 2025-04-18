from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    cache = [[-1 for avl in range(w+1)] for index in range(n+1)]
    return helper(n,w,profit, weight, cache)

def helper(index:int, weightAvl:int, profit:list, weight:list, cache:list) -> int:

    if index <= 0:
        return 0

    if cache[index][weightAvl]!=-1:
        return cache[index][weightAvl]

    if weight[index-1] > weightAvl:
        cache[index][weightAvl] = helper(index-1, weightAvl, profit, weight, cache)
    else:
        cache[index][weightAvl] = max(
            profit[index-1] + helper(index, weightAvl - weight[index-1], profit, weight, cache),
            helper(index-1, weightAvl, profit, weight, cache)
        )

    return cache[index][weightAvl]