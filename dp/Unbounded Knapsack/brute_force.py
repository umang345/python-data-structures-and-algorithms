from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    return helper(n,w,profit, weight)

def helper(index:int, weightAvl:int, profit:list, weight:list) -> int:

    if index <= 0:
        return 0

    if weight[index-1] > weightAvl:
        return helper(index-1, weightAvl, profit, weight)
    else:
        return max(
            profit[index-1] + helper(index, weightAvl - weight[index-1], profit, weight),
            helper(index-1, weightAvl, profit, weight)
        )