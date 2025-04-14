from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    dp = [[False for tar in range(k+1)] for rowIndex in range(n+1)]

    for rowIndex in range(n+1):
        dp[rowIndex][0] = True

    for rowIndex in range(1,n+1):
        for colIndex in range(1,k+1):
            
            if arr[rowIndex-1] > colIndex:
                dp[rowIndex][colIndex] = dp[rowIndex-1][colIndex]
            else:
                dp[rowIndex][colIndex] = dp[rowIndex-1][colIndex] or dp[rowIndex-1][colIndex - arr[rowIndex-1]]

    return dp[n][k]
    
    

