from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    dp = [[[False, False] for tar in range(k+1)] for rowIndex in range(n+1)]
    return helper(n-1, k, arr, dp)

def helper(index:int, target:int, arr:list[int], dp:list)->bool:
    if target==0:
        return True 
    
    if index<0:
        return False

    if dp[index][target][0]:
        return dp[index][target][1]

    dp[index][target][0] = True 
    

    if arr[index] > target:
        dp[index][target][1] =  helper(index-1,target, arr, dp)
    else:
        dp[index][target][1] = helper(index-1, target-arr[index], arr, dp) or helper(index-1, target, arr, dp)

    return dp[index][target][1]